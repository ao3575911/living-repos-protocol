# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

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
