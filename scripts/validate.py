"""Validate Living Repository manifests.

Default (lenient): a manifest fails only if it breaks the v0.1.0 rules
(schemas/manifest.lenient.schema.json: required fields and basic types).
Violations of the full rules (schemas/manifest.schema.json: unknown fields,
values outside the allowed sets, patterns) are printed as warnings.

--strict: violations of the full rules fail too (v0.2.0 behaviour).

Usage:
  python scripts/validate.py [--strict] [PATH_OR_GLOB ...]
With no paths it runs the self-test over examples/ and tests/.
"""
import glob, json, pathlib, sys
import jsonschema, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent


def load(name):
    schema = json.loads((ROOT / "schemas" / name).read_text())
    jsonschema.Draft7Validator.check_schema(schema)
    return jsonschema.Draft7Validator(schema)


LENIENT = load("manifest.lenient.schema.json")
STRICT = load("manifest.schema.json")
RUNTIME = load("runtime.schema.json")


def check(path, strict):
    """Return (errors, warnings) as lists of strings."""
    doc = yaml.safe_load(pathlib.Path(path).read_text())
    errors = [f"{e.json_path}: {e.message}" for e in LENIENT.iter_errors(doc)]
    # Strict rules are only meaningful once the v0.1.0 rules pass.
    extra = [f"{e.json_path}: {e.message}" for e in STRICT.iter_errors(doc)] if not errors else []
    return (errors + extra, []) if strict else (errors, extra)


def report(path, strict):
    errors, warnings = check(path, strict)
    print(("ok   " if not errors else "FAIL ") + path)
    for m in errors:
        print(f"     error: {m}")
    for m in warnings:
        print(f"     warning: {m}")
    return not errors


def files(pattern):
    return sorted(glob.glob(str(ROOT / pattern)))


def undescribed(node, path="$"):
    """Yield paths of schema properties that lack a description."""
    for key in ("properties", "patternProperties"):
        for name, sub in node.get(key, {}).items():
            here = f"{path}.{name}"
            if "description" not in sub:
                yield here
            yield from undescribed(sub, here)
    if isinstance(node.get("items"), dict):
        yield from undescribed(node["items"], path + "[]")


def self_test():
    missing = list(undescribed(STRICT.schema)) + list(undescribed(RUNTIME.schema))
    for m in missing:
        print(f"FAIL no description: {m}")
    ok = not missing
    import re
    m = re.search(r"^## \[(\d+\.\d+\.\d+)\]", (ROOT / "CHANGELOG.md").read_text(), re.M)
    want = f"https://ao3575911.github.io/living-repos-protocol/schemas/v{m.group(1)}/manifest.schema.json"
    id_ok = STRICT.schema.get("$id") == want
    ok &= id_ok
    print(("ok   " if id_ok else f"FAIL want {want}, got ") + f"$id {STRICT.schema.get('$id')}")
    for p in files("examples/*.yaml") + files("tests/valid/*.yaml"):
        e, w = check(p, strict=True)
        ok &= not e
        print(("ok   strict " if not e else "FAIL strict ") + p)
    for p in files("tests/compat/*.yaml"):
        lenient_ok = not check(p, strict=False)[0]
        strict_ok = not check(p, strict=True)[0]
        expect_strict = "v0.1.0-example" in p
        good = lenient_ok and strict_ok == expect_strict
        ok &= good
        print(("ok   " if good else "FAIL ") + f"compat lenient={'pass' if lenient_ok else 'fail'} strict={'pass' if strict_ok else 'fail'} {p}")
    for p in files("tests/invalid/*.yaml"):
        rejected = bool(check(p, strict=True)[0])
        ok &= rejected
        print(("ok   strict rejected " if rejected else "FAIL strict accepted ") + p)
    import match
    for d in files("tests/runtime/*/"):
        name = pathlib.Path(d).name
        runtime, errors = match.load_runtime(pathlib.Path(d) / "runtime.yaml")
        manifest_errors = check(str(pathlib.Path(d) / "manifest.yaml"), strict=True)[0]
        problems = [] if errors else match.mismatches(runtime, yaml.safe_load((pathlib.Path(d) / "manifest.yaml").read_text()))
        good = not errors and not manifest_errors and (not problems) == name.startswith("match")
        ok &= good
        print(("ok   " if good else "FAIL ") + f"runtime {'match' if not problems else 'mismatch'} {d}" + "".join(f"\n     {e}" for e in errors + manifest_errors))
    return ok


args = sys.argv[1:]
strict = "--strict" in args
paths = [a for a in args if a != "--strict"]
if not paths:
    sys.exit(0 if self_test() else 1)
ok = True
for pattern in paths:
    for p in sorted(glob.glob(pattern)) or [pattern]:
        ok &= report(p, strict)
sys.exit(0 if ok else 1)
