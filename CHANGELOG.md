# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Runtime capability document: `docs/runtime.md`, `schemas/runtime.schema.json`, the reference check `scripts/match.py` and fixtures in `tests/runtime/` ([#17](https://github.com/ao3575911/living-repos-protocol/issues/17)).
- Frozen copies of the schemas at every release tag on the docs site, at `/schemas/<tag>/` ([#18](https://github.com/ao3575911/living-repos-protocol/issues/18)).
- Invalid fixture: webhook target without `url` ([#21](https://github.com/ao3575911/living-repos-protocol/issues/21)).

### Changed

- The strict schema's `$id` is now the versioned docs-site URL of the latest release; the self-test checks it against `CHANGELOG.md`.

## [0.3.0] - 2026-10-25

Defines protocol version `v0.3.0`. Additive over v0.2.1: every manifest valid under v0.1.0, v0.2.0 or v0.2.1 still validates in lenient mode.

### Added
- Optional `snapshot` field (`paths`, `retention_days`) for agents that declare `snapshot_restore`, with spec text, strict schema rules, one valid and four invalid fixtures. Lenient validation is unchanged, so every v0.2.1 manifest still passes.
- Every strict schema field has a description; the self-test fails if one is missing.
- `scripts/gen_readme.py` generates README badges, the manifest field table and the docs schema reference from the schema. CI fails on drift.
- GitHub Pages site: <https://ao3575911.github.io/living-repos-protocol/>, with the spec, schema reference, versioning policy and raw schemas.
- STRATEGY.md (problem, audience, non-goals, alternatives, principles) and AGENTS.md.
- Labels as code with a sync workflow, a Spec change (RFC) issue form, and a manually triggered Release Please workflow that proposes the next version without tagging.

### Changed
- Copilot review instructions point at AGENTS.md and list the changes to block.
- Bug and feature forms apply type and triage labels.

## [0.2.1] - 2026-10-25

### Fixed
- 0.2.0 rejected manifests that were valid under v0.1.0. Validation is now lenient by default: every manifest valid under v0.1.0 passes, and unknown fields, values outside the allowed sets and pattern mismatches are reported as warnings.

### Added
- `--strict` flag for `scripts/validate.py` and `strict` input for the action (default `false`). Strict mode is the 0.2.0 behaviour.
- `schemas/manifest.lenient.schema.json`: the v0.1.0 schema, used for lenient validation.
- Compatibility fixtures in `tests/compat/`: the v0.1.0 example plus manifests with unknown fields and values. CI checks they pass in lenient mode and that strict mode rejects all but the example.

### Changed
- `docs/spec.md` describes the two validation modes.

## [0.1.0] - 2026-10-24

### Added
- Initial protocol draft v0.1.0: specification, PRD, versioning policy and the manifest JSON Schema.
- CI job `test`: Markdown lint and schema self-check plus validation of the example manifest.
- Licence, contributing guide, security policy, code of conduct, issue and PR templates.

[Unreleased]: https://github.com/ao3575911/living-repos-protocol/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ao3575911/living-repos-protocol/releases/tag/v0.1.0
