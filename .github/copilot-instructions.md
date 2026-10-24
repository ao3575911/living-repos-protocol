# Copilot review instructions

Follow [AGENTS.md](../AGENTS.md). Review strictly and request changes for:

- Lenient validation rejecting anything it accepted before (protocol), or edits to `schemas/manifest.lenient.schema.json`.
- Spec, schema, fixtures or examples changed without the others they depend on.
- A schema field without a `description`, or a new rule without an invalid fixture.
- Missing CHANGELOG entry under Unreleased.
- Protocol pin out of sync across `PROTOCOL_VERSION`, `PROTOCOL.md` and the CI action ref (living-repos).
- Unpinned actions, or workflow permissions broader than the job needs.
- Placeholder text, marketing language or broken relative links.
- Secrets, tokens or credentials in any file.

Do not comment on style that markdownlint or the validator already enforce.
