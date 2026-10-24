# AGENTS.md

Instructions for coding agents working in this repository. Humans: see [CONTRIBUTING.md](CONTRIBUTING.md).

## Setup

```sh
pip install -r requirements-ci.txt
npm install -g markdownlint-cli2   # or use npx
```

## Checks (the CI `test` job runs all of these)

```sh
python scripts/validate.py          # schema self-test: examples, tests/valid, tests/compat, tests/invalid
npx markdownlint-cli2 "**/*.md"
```

## Layout

- `docs/spec.md`: meaning of every field. `schemas/manifest.schema.json`: strict rules. `schemas/manifest.lenient.schema.json`: v0.1.0 rules, never edit.
- `tests/valid/` pass strict; `tests/invalid/` fail strict; `tests/compat/` pass lenient and, except the v0.1.0 example, fail strict.
- `action.yml`: composite action wrapping `scripts/validate.py`.

## Rules

- Spec, schema and fixtures change together in one PR. Every new rule gets an invalid fixture; every field gets a `description`.
- Never make lenient validation reject a manifest it accepted before. New constraints go into the strict schema only.
- Add a CHANGELOG entry under Unreleased (Keep a Changelog).
- Pin actions to a version; keep workflow permissions at `contents: read` unless a job needs more.
- `main` is protected: open a PR, `test` must pass, squash merge, signed commits.
- No placeholder text and no marketing language.
