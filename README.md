# Living Repositories Protocol
Canonical protocol/specification repository for Living Repositories.
Initial target: `v0.1.0-draft`

[![CI](https://github.com/ao3575911/living-repos-protocol/actions/workflows/ci.yml/badge.svg)](https://github.com/ao3575911/living-repos-protocol/actions/workflows/ci.yml) [![Release](https://img.shields.io/github/v/release/ao3575911/living-repos-protocol)](https://github.com/ao3575911/living-repos-protocol/releases) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

![Living Repositories Protocol](docs/social-preview.png)

## What it is

The specification for Living Repositories: repositories that bring their own cloud agent runtime. It defines the `.living/manifest.yaml` format and publishes a JSON Schema for it.

## Quickstart

Validate a manifest against the schema:

```sh
git clone https://github.com/ao3575911/living-repos-protocol
cd living-repos-protocol
pip install -r requirements-ci.txt
python scripts/validate.py examples/manifest.yaml
```

## GitHub Action

Validate a repository's manifest in CI:

```yaml
- uses: actions/checkout@v7.0.1
- uses: ao3575911/living-repos-protocol@v0.2.0
  with:
    manifests: .living/manifest.yaml
```

`manifests` takes space-separated paths or glob patterns. The job fails if any manifest is invalid.

## Docs

- [Specification](docs/spec.md)
- [Protocol PRD](docs/protocol-prd.md)
- [Versioning](docs/versioning.md)
- [Manifest schema](schemas/manifest.schema.json)

## Status

Draft. Protocol version `v0.1.0-draft`; repository release v0.1.0.

## Related

- [living-repos](https://github.com/ao3575911/living-repos): examples and demos that implement this protocol.

## Licence

[MIT](LICENSE). See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute.
