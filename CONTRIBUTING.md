# Contributing

- Open an issue before proposing a protocol change.
- Any schema change needs a CHANGELOG entry and follows [versioning](docs/versioning.md).
- Keep `examples/` valid against `schemas/`; CI checks this.
- Run `python scripts/validate.py examples/manifest.yaml` before opening a PR.

## Generated README sections

Parts of README.md between `BEGIN GENERATED` and `END GENERATED` markers come from source files. Edit the source, then run `python scripts/gen_readme.py`. CI fails if they drift.

## Releases

Run the Release Please workflow to open a PR with the next SemVer version from Conventional Commit titles. Before merging, move the CHANGELOG Unreleased entries under the new version. In the same PR, set the `$id` of `schemas/manifest.schema.json` and `schemas/runtime.schema.json` to the new version's URL (the self-test checks this). After merge, a maintainer tags the merge commit, publishes the release with the CHANGELOG notes, and runs the Pages workflow (`gh workflow run pages.yml`) so the frozen schemas appear at `/schemas/<tag>/`. Tag pushes do not deploy Pages because the `github-pages` environment only allows `main`.
