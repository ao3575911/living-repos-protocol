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

## Open questions

- Whether runtimes should accept manifests that target an older minor version than they implement.
- Whether to publish the schema at a stable URL per protocol version.
