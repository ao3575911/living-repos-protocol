# Contributing

- Open an issue before proposing a protocol change.
- Any schema change needs a CHANGELOG entry and follows [versioning](docs/versioning.md).
- Keep `examples/` valid against `schemas/`; CI checks this.
- Run `python scripts/validate.py examples/manifest.yaml` before opening a PR.
