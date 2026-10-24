# Schema reference

Fields of `.living/manifest.yaml` as enforced in strict mode. Lenient mode (the default) checks only required fields and basic types; see [validation modes](spec.md#validation-modes).

<!-- BEGIN GENERATED: fields -->

| Field | Type | Required | Allowed | Description |
| --- | --- | --- | --- | --- |
| `protocol_version` | string | yes | pattern `^v\d+\.\d+\.\d+(-[0-9A-Za-z.-]+)?$` | Protocol version the manifest targets: v followed by SemVer, for example v0.1.0-draft. |
| `project_id` | string | yes | pattern `^[a-z0-9][a-z0-9-]{0,62}$` | Stable repository identifier: lowercase letters, digits and hyphens, at most 63 characters. |
| `agent_capabilities` | array of strings | yes | `run_tasks`, `publish_state`, `open_pull_requests`, `snapshot_restore`, `handoff`, `read_secrets` | What the agent may do. A runtime must refuse to start an agent that declares a capability it does not support. |
| `isolation_profile` | string | yes | `dedicated-vm`, `container`, `sandbox-process` | How the runtime isolates the agent. |
| `state_publication` | object | yes | - | Where the agent publishes its state. |
| `state_publication.target` | string | yes | `control-process`, `file`, `webhook` | control-process, file or webhook. |
| `state_publication.path` | string | no | - | State file path relative to the repository root. Required when target is file. |
| `state_publication.url` | string | no | pattern `^https://` | https URL that receives state. Required when target is webhook. |
| `logging_requirements` | object | yes | - | How the agent logs. |
| `logging_requirements.structured` | boolean | yes | - | true means one JSON object per log line. |
| `logging_requirements.level` | string | no | `debug`, `info`, `warn`, `error` | Minimum log level. Default info. |
| `snapshot` | object | no | - | What the runtime snapshots and how long it keeps snapshots. Used with the snapshot_restore capability. Optional. |
| `snapshot.paths` | array of strings | yes | - | Paths relative to the repository root to include in each snapshot. |
| `snapshot.retention_days` | integer | no | - | Days to keep each snapshot. Default 7. |
| `secrets` | array of strings | no | - | Names of the secrets the agent needs, never their values. Requires the read_secrets capability. Optional. |

Generated from [`schemas/manifest.schema.json`](https://github.com/ao3575911/living-repos-protocol/blob/main/schemas/manifest.schema.json) by `scripts/gen_readme.py`. Top-level keys starting with `x-` are allowed as extensions.

<!-- END GENERATED: fields -->
