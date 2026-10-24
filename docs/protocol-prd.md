# Protocol PRD
Define portable, versioned runtime/agent protocol for living repositories.

## Problem

A repository that wants its own cloud agent has no standard way to say what that agent may do, how it must be isolated, or where it reports state. Each runtime invents its own config, so repositories are tied to one runtime.

## Goal

One small manifest, `.living/manifest.yaml`, that any compliant runtime can read to start, isolate and observe a repository's agent.

## Users

- Repository maintainers, who write the manifest.
- Runtime authors, who read it and enforce it.
- Reviewers, who need to see an agent's permissions in one file.

## Scope for v0.x

- The manifest format: [spec](spec.md) and [schema](../schemas/manifest.schema.json).
- Conformance fixtures that any validator can run.
- A GitHub Action that validates manifests in CI.

Out of scope: the runtime itself, authentication, billing and scheduling.

## Success criteria

- At least one example repository in [living-repos](https://github.com/ao3575911/living-repos) validates in CI with the published action.
- Every schema rule is covered by a fixture.
- A maintainer can write a valid manifest from the spec alone.

## Open questions

None open. Settled in v0.4.0: runtimes advertise support in a [runtime capability document](runtime.md); secrets access is the `read_secrets` capability with a `secrets` field ([spec](spec.md#secrets)).
