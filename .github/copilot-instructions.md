# Copilot review instructions

Review strictly. Flag:

- Changes to the manifest schema or required fields without a CHANGELOG entry and SemVer reasoning.
- Examples or docs that drift from the protocol in [living-repos-protocol](https://github.com/ao3575911/living-repos-protocol).
- Unpinned GitHub Actions or workflow permissions broader than `contents: read`.
- Placeholder text, hype, or broken relative links in Markdown.
- Secrets, tokens or credentials in any file.
