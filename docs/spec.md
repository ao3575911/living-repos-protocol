# Protocol Spec (Draft v0.1.0)
Required fields: protocol_version, project_id, agent_capabilities, isolation_profile, state_publication, logging_requirements.

## Scope

This document defines the Living Repository manifest: a YAML file at `.living/manifest.yaml` in the repository root. A runtime reads it to decide how to start, isolate and observe the repository's agent. The machine-readable form is [`schemas/manifest.schema.json`](../schemas/manifest.schema.json). Where this document and the schema disagree, the schema is a bug and gets fixed.

The key words MUST, MUST NOT, SHOULD and MAY are used as described in RFC 2119.

## Fields

| Field | Type | Required | Rule |
| --- | --- | --- | --- |
| `protocol_version` | string | yes | Protocol version the manifest targets, as `v` plus SemVer, for example `v0.1.0-draft`. Pattern: `^v\d+\.\d+\.\d+(-[0-9A-Za-z.-]+)?$`. |
| `project_id` | string | yes | Stable identifier for the repository. Lowercase letters, digits and hyphens, starting with a letter or digit, at most 63 characters. |
| `agent_capabilities` | array of strings | yes | At least one entry, no duplicates. Allowed values are listed below. |
| `isolation_profile` | string | yes | One of `dedicated-vm`, `container`, `sandbox-process`. |
| `state_publication` | object | yes | Where the agent publishes its state. See below. |
| `logging_requirements` | object | yes | How the agent logs. See below. |

### Optional fields

| Field | Type | Rule |
| --- | --- | --- |
| `snapshot` | object | What the runtime snapshots when the agent declares `snapshot_restore`. Added in release v0.3.0. See below. |

### `agent_capabilities` values

- `run_tasks`: the agent runs tasks in the repository.
- `publish_state`: the agent publishes state to the `state_publication` target.
- `open_pull_requests`: the agent opens pull requests against the repository.
- `snapshot_restore`: the runtime can snapshot and restore the agent's environment.
- `handoff`: the agent can hand a running session to another runtime.

A runtime MUST refuse to start an agent that declares a capability it does not support.

### `state_publication`

| Key | Type | Required | Rule |
| --- | --- | --- | --- |
| `target` | string | yes | One of `control-process`, `file`, `webhook`. |
| `path` | string | when `target` is `file` | Path relative to the repository root. |
| `url` | string | when `target` is `webhook` | An `https://` URL. |

### `logging_requirements`

| Key | Type | Required | Rule |
| --- | --- | --- | --- |
| `structured` | boolean | yes | `true` means one JSON object per log line. |
| `level` | string | no | One of `debug`, `info`, `warn`, `error`. Default `info`. |

### `snapshot`

| Key | Type | Required | Rule |
| --- | --- | --- | --- |
| `paths` | array of strings | yes | At least one entry, no duplicates. Each a path relative to the repository root, not starting with `/` and without `..`. |
| `retention_days` | integer | no | At least 1. Default 7. |

A manifest that declares `snapshot_restore` SHOULD include `snapshot`. Without it, the runtime decides what to snapshot. A runtime that does not support snapshots MAY ignore `snapshot` when the capability is not declared.

## Unknown fields

A manifest MUST NOT contain fields not listed here, at the top level or inside the nested objects. The one exception is extension fields: top-level keys starting with `x-` MAY appear and MUST be ignored by runtimes that do not understand them. Validators MUST report any other unknown field.

## Validation modes

- **Lenient (default):** a manifest fails only if it breaks the v0.1.0 rules ([`manifest.lenient.schema.json`](../schemas/manifest.lenient.schema.json): required fields and basic types). Unknown fields, values outside the allowed sets and pattern mismatches are reported as warnings. Every manifest valid under v0.1.0 passes.
- **Strict (`--strict`):** every rule in this document is enforced ([`manifest.schema.json`](../schemas/manifest.schema.json)), and the warnings above become errors. New manifests SHOULD pass strict mode.

## Annotated example

```yaml
protocol_version: v0.1.0-draft     # targets this draft of the protocol
project_id: hello                  # stable id, lowercase and hyphens
agent_capabilities:                # what the agent may do
  - run_tasks
  - publish_state
isolation_profile: dedicated-vm    # one VM per agent
state_publication:
  target: file                     # publish state to a file in the repo
  path: .living/state.json
logging_requirements:
  structured: true                 # JSON lines
  level: info
x-team: platform                   # extension field, ignored if unknown
```

## Versioning

Changes to this document follow [versioning.md](versioning.md).
