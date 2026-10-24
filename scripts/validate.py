"""Validate manifests against schemas/manifest.schema.json.

With paths: each file must be valid.
Without paths: examples/*.yaml and tests/valid/*.yaml must be valid,
and every tests/invalid/*.yaml must be rejected.
"""
import glob, json, pathlib, sys
import jsonschema, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
schema = json.loads((ROOT / "schemas/manifest.schema.json").read_text())
jsonschema.Draft7Validator.check_schema(schema)
validator = jsonschema.Draft7Validator(schema)


def errors(path):
    return list(validator.iter_errors(yaml.safe_load(pathlib.Path(path).read_text())))


failed = False
if sys.argv[1:]:
    valid = [p for pattern in sys.argv[1:] for p in sorted(glob.glob(pattern)) or [pattern]]
    invalid = []
else:
    valid = sorted(glob.glob(str(ROOT / "examples/*.yaml")) + glob.glob(str(ROOT / "tests/valid/*.yaml")))
    invalid = sorted(glob.glob(str(ROOT / "tests/invalid/*.yaml")))
for p in valid:
    errs = errors(p)
    print(("ok   " if not errs else "FAIL ") + p)
    for e in errs:
        print(f"     {e.json_path}: {e.message}")
    failed |= bool(errs)
for p in invalid:
    errs = errors(p)
    print(("ok   rejected " if errs else "FAIL accepted ") + p)
    failed |= not errs
sys.exit(1 if failed else 0)
