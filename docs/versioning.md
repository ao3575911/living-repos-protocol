# Versioning
Semantic versioning; breaking changes require major bump.

## Two version numbers

- **Protocol version** (`protocol_version` in a manifest, for example `v0.1.0-draft`): the version of the manifest format a file targets.
- **Repository release** (Git tag, for example `v0.2.0`): a release of this repository, which ships the spec, schema, fixtures and action together.

A repository release can change tooling without changing the protocol. The CHANGELOG states which protocol version each release defines.

## What counts as breaking

Breaking (major bump after 1.0, minor bump before 1.0):

- Removing a field, capability, isolation profile or state target.
- Making an optional field required.
- Narrowing an allowed pattern or value set so that a previously valid manifest fails.

Not breaking (minor bump):

- Adding an optional field, capability, isolation profile or state target.
- Widening a pattern or value set.

Patch: wording fixes in the spec, new fixtures and tooling fixes that do not change what validates.

## Pre-1.0

Until 1.0 the protocol is a draft. Breaking changes bump the minor version and are listed under a **Breaking** heading in the CHANGELOG.

## Decisions

- The schema is the source of truth for validation; the spec is the source of truth for meaning.
- Every rule in the schema has at least one invalid fixture in `tests/invalid/`.

## Older manifests

A runtime that implements protocol `vX.Y` MUST accept a manifest whose `protocol_version` has the same major version `X` and a minor version at or below `Y`, for example a `v0.3` runtime accepts `v0.1.0-draft`, `v0.2.0` and `v0.3.0` manifests. It MUST refuse a manifest with a newer minor or a different major version. Pre-release and patch parts are ignored for this rule.

This holds before 1.0 too: every minor release so far only added optional fields and values, and the lenient schema keeps v0.1.0 manifests valid. If a future minor release is breaking, its CHANGELOG entry will say which older manifests stop being accepted.

Fixtures: `tests/runtime/match-older-minor` (accepted) and `tests/runtime/newer-minor` (refused).

## Schema URLs

Every release tag has a frozen copy of the schemas on the docs site:

- `https://ao3575911.github.io/living-repos-protocol/schemas/<tag>/manifest.schema.json` (strict)
- `https://ao3575911.github.io/living-repos-protocol/schemas/<tag>/manifest.lenient.schema.json` (lenient, from v0.2.1)

These files never change once published. `https://ao3575911.github.io/living-repos-protocol/schemas/manifest.schema.json` always tracks `main`. The `$id` of each schema with a frozen copy (`manifest.schema.json`, and `runtime.schema.json` from v0.4.0) is the URL for the latest release; CI checks that it matches the newest version in `CHANGELOG.md`. The lenient schema keeps its v0.1.0 content unchanged.
