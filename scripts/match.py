"""Check whether a runtime can run a manifest.

Usage:
  python scripts/match.py RUNTIME_DOC MANIFEST
Exits 0 when the runtime supports everything the manifest declares,
1 otherwise, printing one line per mismatch. Rules: docs/runtime.md.
"""
import json, pathlib, re, sys
import jsonschema, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
RUNTIME = jsonschema.Draft7Validator(
    json.loads((ROOT / "schemas" / "runtime.schema.json").read_text())
)


def minor(version):
    m = re.match(r"^v(\d+)\.(\d+)", str(version))
    return (int(m.group(1)), int(m.group(2))) if m else None


def mismatches(runtime, manifest):
    out = []
    want = minor(manifest.get("protocol_version"))
    have = {minor(v) for v in runtime["protocol_versions"]}
    if want not in have:
        out.append(f"protocol_version {manifest.get('protocol_version')} not in {runtime['protocol_versions']}")
    for cap in manifest.get("agent_capabilities", []):
        if cap not in runtime["agent_capabilities"]:
            out.append(f"capability {cap} not supported")
    iso = manifest.get("isolation_profile")
    if iso not in runtime["isolation_profiles"]:
        out.append(f"isolation_profile {iso} not supported")
    target = (manifest.get("state_publication") or {}).get("target")
    if target not in runtime["state_publication_targets"]:
        out.append(f"state_publication target {target} not supported")
    return out


def load_runtime(path):
    doc = yaml.safe_load(pathlib.Path(path).read_text())
    errors = [e.message for e in RUNTIME.iter_errors(doc)]
    return doc, errors


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    runtime, errors = load_runtime(sys.argv[1])
    if errors:
        for e in errors:
            print(f"FAIL runtime document: {e}")
        sys.exit(1)
    manifest = yaml.safe_load(pathlib.Path(sys.argv[2]).read_text())
    problems = mismatches(runtime, manifest)
    for p in problems:
        print(f"FAIL {p}")
    if not problems:
        print("ok   runtime supports manifest")
    sys.exit(1 if problems else 0)
