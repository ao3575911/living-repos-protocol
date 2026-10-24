# Runtime capability document

A runtime publishes a capability document that lists what it supports. Tools compare it with a manifest before starting an agent, so a runtime can refuse a manifest it cannot honour without running it.

## Format and location

- YAML or JSON, validated by [`runtime.schema.json`](schemas/runtime.schema.json).
- A runtime SHOULD ship the document with its distribution and SHOULD state where it is in its own docs.
- A runtime that serves HTTP MAY serve it at `/.well-known/living-repos-runtime.json`.

## Fields

| Field | Type | Rule |
| --- | --- | --- |
| `runtime` | string | Name of the runtime. |
| `protocol_versions` | array of strings | Protocol versions implemented, as `vMAJOR.MINOR`, for example `v0.3`. At least one. |
| `agent_capabilities` | array of strings | Supported `agent_capabilities` values. May be empty. |
| `isolation_profiles` | array of strings | Isolation profiles the runtime can provide. At least one. |
| `state_publication_targets` | array of strings | Accepted `state_publication.target` values. At least one. |

Top-level keys starting with `x-` are extensions and MUST be ignored by consumers that do not understand them. Other unknown fields are invalid.

## Matching

A runtime supports a manifest when all of these hold:

1. The manifest's `protocol_version`, reduced to `vMAJOR.MINOR`, is accepted under the rules in [Versioning](versioning.md).
2. Every value in the manifest's `agent_capabilities` is in the document's `agent_capabilities`.
3. The manifest's `isolation_profile` is in `isolation_profiles`.
4. The manifest's `state_publication.target` is in `state_publication_targets`.

A runtime MUST refuse to start an agent when any rule fails, and SHOULD report every failing rule.

## Reference check

```bash
python scripts/match.py runtime.yaml .living/manifest.yaml
```

It exits 0 on a match and 1 otherwise, printing one line per failing rule. Fixtures are in `tests/runtime/`: a directory named `match*` must match; any other directory must not.

## Example

```yaml
runtime: example-runtime
protocol_versions: [v0.1]
agent_capabilities: [run_tasks, publish_state]
isolation_profiles: [container, sandbox-process]
state_publication_targets: [control-process, file]
```
