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


def check(path, strict):
    """Return (errors, warnings) as lists of strings."""
    doc = yaml.safe_load(pathlib.Path(path).read_text())
    fmt = lambda e: f"{e.json_path}: {e.message}"
    errors = [fmt(e) for e in LENIENT.iter_errors(doc)]
    extra = [fmt(e) for e in STRICT.iter_errors(doc)] if not errors else []
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


def self_test():
    ok = True
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
