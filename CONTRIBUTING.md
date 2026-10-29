# Contributing to oscal

*This file is a checklist, not a design log. Each rule is a line or two that links to where its reasoning lives: a code comment, a workflow header, or a linked page. `lint-and-docs.yaml` holds the file to a word budget so it stays that way.*

## What this project is

A LinkML schema of NIST's Open Security Controls Assessment Language (OSCAL) 1.2.3, so LinkML's tools validate OSCAL documents and a knowledge bundle can type its concepts with OSCAL's models.

| Path | Holds |
| --- | --- |
| `src/oscal/schema/*.yaml` | The LinkML schema: the umbrella and one module per OSCAL model. Edit these. |
| `src/oscal/schema/metaschema/` | OSCAL's metaschema sources at the pinned release. Never edit. |
| `src/oscal/datamodel/`, `project/`, `docs/schema/` | Artefacts generated from the schema. |
| `docs/` | The documentation site's pages. |
| `tests/`, `tests/data/` | Python tests; example data and third-party OSCAL documents. |
| `.lokf/knowledge/` | This repository's knowledge bundle. |

## Development setup

You need Python 3.10+, [uv](https://docs.astral.sh/uv/) and [just](https://github.com/casey/just).

```bash
git clone https://github.com/lmodel/oscal.git
cd oscal
uv sync --group dev
just --list
```

`just gen-project` regenerates `project/` and the Python datamodel; `just gen-doc` regenerates `docs/schema/` and the element pages.

### Agent skills (optional, only for this repo's `.lokf/` bundle)

The bundle is maintained with the Knowledge Trust Ladder (KTL) skills, **installed, never committed**; CI installs the librarian skill at run time, pinned to a release. Nothing in the schema depends on them. [The install page](https://w3id.org/ktl/docs/install/) lists every route; with npm:

```bash
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-librarian --yes   # derive concepts
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-curator --yes     # confirm them as a person
```

## Before opening a pull request

- **Edit the schema, then regenerate.** Edit `src/oscal/schema/`, run `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit the output; `project/`, `src/oscal/datamodel/`, `docs/schema/` and `.lokf/oscal.yaml` are generated.
- **Render what OSCAL defines.** Name the metaschema definition an element renders in the pull request, and give each enum the lists it renders in `oscal_allowed_values`; [AI_COVENANT.md](AI_COVENANT.md) says why. `tests/test_schema_rules.py` holds each enum to its lists.
- **Leave `src/oscal/schema/metaschema/` as upstream wrote it.** Replace it whole from one OSCAL release instead and move the pins in `scripts/check_upstream_release.py` and the schema header; `upstream-watch.yaml` checks the copy.
- **Keep names apart from LOKF's, slsa's and github-actions'**: a host imports the copies together, so a shared name carries the same IRI. `tests/test_schema_rules.py` checks, and lists the keys OSCAL shares.
- **Run the tests**: `just test` (schema generation, `pytest` and `linkml-validate` over `tests/data/`). Example data goes in `tests/data/valid/` and `tests/data/invalid/`, named `ClassName-suffix.yaml`, with an invalid example per constraint.
- **Follow the schema's conventions**: UpperCamelCase classes and enums, OSCAL's own keys as slot names (`.linkmllint.yaml` says why), a short description on every element. `just lint` checks.
- **Run the pre-commit hooks** on what you staged (`uvx pre-commit run`): ruff, yamllint, codespell, typos and the `uv.lock` check.
- **Lock files are part of the change.** CI installs with `uv sync --locked`; a dependency edit that does not update `uv.lock` (or `.lokf/uv.lock`) fails the run.
- **Knowledge-bundle changes**: `cd .lokf && just lokf-validate` must pass, and `knowledge-registrar.yaml` runs on any `.lokf/**` change.
- **`lint-and-docs.yaml` is easy to trip locally**: ShellCheck, actionlint, markdownlint against `.markdownlint-cli2.jsonc`, link-checking against `lychee.toml`, and codespell over every `*.md`.
- **Actions are pinned to commit SHAs**, the version in a trailing comment, and bumped by Dependabot, never by hand to a tag.
- **The skills pin moves with the sidecar copies.** When moving `TRUST_LADDER_SKILLS_REF` in `.github/workflows/knowledge-librarian.yaml`, copy the other `knowledge-*.yaml` workflows and `.lokf/scripts/` and `.lokf/m365/` from that release's `skills/ktl-sidecar/templates/` in the same pull request.
- **If your change alters behaviour** (not just wording), add an entry under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md).
- Keep changes focused, and fill in the pull request template's checklist.

## Code of conduct

Participation here is covered by the [Contributor Covenant](CODE_OF_CONDUCT.md).

## Using AI tools

AI assistance is welcome; [AI_COVENANT.md](AI_COVENANT.md) sets the rules, for people and the scheduled `knowledge-librarian` agent alike. You are the author of what you submit, and a claim about what OSCAL defines must be checked against its metaschema.

## Reporting issues

Use the [issue tracker](https://github.com/lmodel/oscal/issues) for problems with the schema and requests for new elements. A problem in OSCAL itself belongs [upstream](https://github.com/usnistgov/OSCAL/issues).

## Releasing (maintainers)

- Write `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md) as you go; the release job refuses an empty one (`.github/scripts/changelog-release.mjs check`).
- Type the commit ([Conventional Commits](https://www.conventionalcommits.org/)) for what the change *is*. Only `feat:`, `fix:`, `security:` and a breaking `!` start a release; other types leave their entries for the next release that does. A pull request that would release must carry a releasing type in its title too, since a squash merge takes its subject from it.
- On merge, [`semantic-release.yml`](.github/workflows/semantic-release.yml) retitles the section to `## [X.Y.Z] - YYYY-MM-DD`, commits `CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub Release. No file is bumped. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches `.github/workflows/knowledge-release.yaml`, which attaches the schema copy and the bundle when the bundle changed; run it with `force` when only the schema did.
- That step runs behind the `release` GitHub Environment; configure required reviewers on it in Settings → Environments, or every qualifying merge is released unattended.
- Below 1.0.0: push the `v0.0.0` baseline tag on `main` before the first releasing merge, which then releases 0.1.0; both release jobs refuse to run without a `v*` tag, as semantic-release would otherwise start at 1.0.0. `.releaserc.json` maps `breaking: true` to `minor`; reaching 1.0.0 means removing that rule in a pull request of its own.
- A branch rule requiring pull requests, status checks or signed commits would reject the release job's own push to `main`; leave them off. [SECURITY.md](SECURITY.md) says what holds `main` instead, and the shared design is on [KTL's releasing page](https://github.com/noelmcloughlin/knowledge-trust-ladder/blob/main/docs/releasing.md).

## License

By contributing, you agree that your contributions are licensed under the [Apache License 2.0](LICENSE). The metaschema copy and the third-party fixtures are under their own terms; [NOTICE](NOTICE) lists them, so update it when you add something new from elsewhere.
