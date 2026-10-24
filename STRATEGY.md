# Strategy

## Problem

Coding agents now run in the cloud against a repository, but the repository has no standard place to say what that agent may do, how it must be isolated or where it reports state. Each runtime keeps that in its own config, so permissions are invisible in review and a repository is tied to one runtime.

## Audience

- Maintainers who want an agent's permissions visible in one reviewed file.
- Runtime authors who need a portable contract to enforce.
- Reviewers and security teams who audit what agents can do.

## What this repository ships

A manifest format (`.living/manifest.yaml`), its specification, a JSON Schema in lenient and strict forms, conformance fixtures and a GitHub Action that validates manifests.

## Non-goals

- A runtime, scheduler or hosting service.
- Agent instructions or prompts. That is what AGENTS.md is for.
- Authentication, secrets management or billing.
- Replacing dev environment definitions such as devcontainer.json.

## Alternatives and how this differs

| Alternative | What it covers | Gap this protocol fills |
| --- | --- | --- |
| [AGENTS.md](https://agents.md/) | Free-form Markdown instructions for coding agents: setup commands, style, conventions. | No schema and no permissions. A runtime cannot enforce it. A manifest can sit next to it. |
| [devcontainer.json](https://containers.dev/) | A reproducible development container: image, features, tooling. | Describes the environment, not what an agent may do in it or where it reports state. |
| [copilot-setup-steps.yml](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment) | Setup steps for GitHub Copilot's cloud agent. | Specific to one vendor's agent; no capability or isolation declaration. |
| [Dependabot](https://docs.github.com/code-security/dependabot) and [Renovate](https://docs.renovatebot.com/) config | Config-as-code for one bot's update behaviour. | Each bot has its own format. This protocol aims at one format for any repository agent. |
| [OpenSSF Scorecard](https://github.com/ossf/scorecard) | Automated checks of a repository's security practices. | Measures practices after the fact; does not declare agent permissions. A Scorecard-style check of manifests is a possible later addition. |
| [Template repositories](https://docs.github.com/repositories/creating-and-managing-repositories/creating-a-template-repository) | A starting point copied once. | No ongoing contract. [living-repos](https://github.com/ao3575911/living-repos) uses examples as templates, but the manifest is the contract. |

## Principles

1. **Small.** Six required fields. Every addition needs a use case in [living-repos](https://github.com/ao3575911/living-repos).
2. **Backward compatible by default.** Lenient validation accepts every manifest valid under v0.1.0. Stricter rules arrive behind `--strict` first.
3. **Schema and spec in lockstep.** Every rule has a fixture, and every field has a description.
4. **Enforceable.** A runtime must be able to refuse a manifest, not just read it.
5. **Vendor-neutral.** No field names a specific agent or cloud.
