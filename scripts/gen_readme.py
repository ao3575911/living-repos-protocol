"""Regenerate the README sections between BEGIN/END GENERATED markers.

Sources: schemas/manifest.schema.json (field table) and the repository
name (badges). Also renders the same markers in docs/schema-reference.md. Run with --check to fail on drift.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO = "ao3575911/living-repos-protocol"


def badges():
    base = f"https://github.com/{REPO}"
    return (f"[![CI]({base}/actions/workflows/ci.yml/badge.svg)]({base}/actions/workflows/ci.yml) "
            f"[![Release](https://img.shields.io/github/v/release/{REPO})]({base}/releases) "
            "[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)")


def allowed(prop):
    if "enum" in prop:
        return ", ".join(f"`{v}`" for v in prop["enum"])
    if "items" in prop and "enum" in prop["items"]:
        return ", ".join(f"`{v}`" for v in prop["items"]["enum"])
    if "pattern" in prop:
        return f"pattern `{prop['pattern']}`"
    return "-"


def kind(prop):
    if "type" in prop:
        return prop["type"] if prop["type"] != "array" else "array of strings"
    return "string"


def fields():
    schema = json.loads((ROOT / "schemas/manifest.schema.json").read_text())
    required = set(schema["required"])
    rows = ["| Field | Type | Required | Allowed | Description |", "| --- | --- | --- | --- | --- |"]
    def walk(props, req, prefix=""):
        for name, prop in props.items():
            rows.append(f"| `{prefix}{name}` | {kind(prop)} | {'yes' if name in req else 'no'} | "
                        f"{allowed(prop).replace('|', '&#124;')} | {prop.get('description', '')} |")
            if "properties" in prop:
                walk(prop["properties"], set(prop.get("required", [])), f"{prefix}{name}.")
    walk(schema["properties"], required)
    rows.append("")
    rows.append("Generated from [`schemas/manifest.schema.json`](schemas/manifest.schema.json) by `scripts/gen_readme.py`. Top-level keys starting with `x-` are allowed as extensions.")
    return "\n".join(rows)


SECTIONS = {"badges": badges, "fields": fields}


def render(text):
    for name, fn in SECTIONS.items():
        text = re.sub(rf"(<!-- BEGIN GENERATED: {name} -->\n).*?(\n<!-- END GENERATED: {name} -->)",
                      lambda m: m.group(1) + "\n" + fn() + "\n" + m.group(2), text, flags=re.S)
    return text


TARGETS = ["README.md", "docs/schema-reference.md"]
stale = []
for name in TARGETS:
    path = ROOT / name
    current = path.read_text()
    new = render(current)
    if new == current:
        continue
    if "--check" in sys.argv:
        stale.append(name)
    else:
        path.write_text(new)
if stale:
    sys.exit(f"Out of date: {', '.join(stale)}. Run: python scripts/gen_readme.py")
print("ok generated sections up to date")
