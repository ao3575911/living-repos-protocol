"""Validate manifests against schemas/manifest.schema.json."""
import json, pathlib, sys
import jsonschema, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
schema = json.loads((ROOT / "schemas/manifest.schema.json").read_text())
jsonschema.Draft7Validator.check_schema(schema)
paths = sys.argv[1:] or [str(p) for p in (ROOT / "examples").glob("*.yaml")]
for path in paths:
    jsonschema.validate(yaml.safe_load(pathlib.Path(path).read_text()), schema)
    print(f"ok {path}")
