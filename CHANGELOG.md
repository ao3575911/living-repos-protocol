# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.4.0] - 2026-10-25

Defines protocol version `v0.4.0`. Additive over v0.3.0: every manifest valid under v0.3.0 still validates in strict mode, and every manifest valid under v0.1.0 still validates in lenient mode.

### Added

- `read_secrets` capability and optional `secrets` field (secret names only); a manifest with `secrets` must declare `read_secrets` ([#19](https://github.com/ao3575911/living-repos-protocol/issues/19)).
- Runtime capability document: `docs/runtime.md`, `schemas/runtime.schema.json`, the reference check `scripts/match.py` and fixtures in `tests/runtime/` ([#17](https://github.com/ao3575911/living-repos-protocol/issues/17)).
- Frozen copies of the schemas at every release tag on the docs site, at `/schemas/<tag>/` ([#18](https://github.com/ao3575911/living-repos-protocol/issues/18)).
- Invalid fixture: webhook target without `url` ([#21](https://github.com/ao3575911/living-repos-protocol/issues/21)).

### Changed

- Runtimes accept manifests that target an older minor version of the same major version, and refuse newer ones; documented in `docs/versioning.md` with a fixture pair ([#20](https://github.com/ao3575911/living-repos-protocol/issues/20)).
- The strict schema's `$id` is now the versioned docs-site URL of the latest release; the self-test checks it against `CHANGELOG.md`.

### Fixed

- Links from `docs/` to `schemas/` were broken on the docs site; they now use absolute URLs. CI runs an offline link and anchor check (lychee).
- Spec title no longer says "Draft v0.1.0".
- Pages no longer triggers on tag pushes, which the `github-pages` environment refuses; the release steps in `CONTRIBUTING.md` run the Pages workflow after tagging instead. `runtime.schema.json` also gets a versioned `$id`, checked by the self-test.

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

## [0.2.0] - 2026-10-25

This entry was missing when v0.2.0 was released and was added in v0.4.0, from the merged pull requests.

### Added
- Full manifest specification in `docs/spec.md` ([#7](https://github.com/ao3575911/living-repos-protocol/pull/7)).
- The schema enforces the spec's field rules: allowed values, patterns and no unknown fields ([#8](https://github.com/ao3575911/living-repos-protocol/pull/8)). Version 0.2.1 made this opt-in with `--strict`.
- Conformance fixtures in `tests/valid/` and `tests/invalid/` ([#9](https://github.com/ao3575911/living-repos-protocol/pull/9)).
- Reusable GitHub Action for validating manifests (`action.yml`) ([#10](https://github.com/ao3575911/living-repos-protocol/pull/10)).

### Changed
- Completed the PRD and the versioning policy ([#11](https://github.com/ao3575911/living-repos-protocol/pull/11)).
- Dependency updates: actions/checkout 7.0.1, markdownlint-cli2-action 24.2.0, setup-python 7.1.0, jsonschema 4.26.0, PyYAML 6.0.3.

## [0.1.0] - 2026-10-24

### Added
- Initial protocol draft v0.1.0: specification, PRD, versioning policy and the manifest JSON Schema.
- CI job `test`: Markdown lint and schema self-check plus validation of the example manifest.
- Licence, contributing guide, security policy, code of conduct, issue and PR templates.

[Unreleased]: https://github.com/ao3575911/living-repos-protocol/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/ao3575911/living-repos-protocol/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/ao3575911/living-repos-protocol/compare/v0.2.1...v0.3.0
[0.2.1]: https://github.com/ao3575911/living-repos-protocol/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/ao3575911/living-repos-protocol/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/ao3575911/living-repos-protocol/releases/tag/v0.1.0
