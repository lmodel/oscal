---
type: Playbook
id: https://w3id.org/lmodel/oscal/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test the schema
description: "How to change the OSCAL schema: set up with uv and just, edit src/oscal/schema/ but never the metaschema copy, give each enum its oscal_allowed_values, regenerate with just gen-project, gen-doc and lokf-adapt, add examples, then run just test, just lint, just lokf-adapt-check and the pre-commit hooks, as the Build and test workflow does on Python 3.10 to 3.14."
resource: CONTRIBUTING.md
about:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-schema
references:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/generated-artefacts
  - https://w3id.org/lmodel/oscal/knowledge/datasets/test-data
  - https://w3id.org/lmodel/oscal/knowledge/workflows/main
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Development setup and Before opening a pull request
  - id: justfile
    resource: justfile
    title: the _wsl2_compat_check, update, test and lint recipes
  - id: copier-answers.yml
    resource: .copier-answers.yml
    title: _src_path and _commit
  - id: main.yaml
    resource: .github/workflows/main.yaml
    title: the test job
  - resource: .linkmllint.yaml
    title: the standard_naming rule
  - resource: .pre-commit-config.yaml
    title: the exclude list
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:56:26Z"
  revision: 928ef231c9fe1766b5f38ad26ece260a7ab1d870
status: draft
---

# Regenerate and test the schema

## Set up

CONTRIBUTING.md asks for Python 3.10 or later, uv and just.[^contributing.md] Clone `https://github.com/lmodel/oscal.git`, run `uv sync --group dev` in it, and list the recipes with `just --list`. On WSL2, run `export JUST_TEMPDIR=/tmp` first, because the justfile's shebang recipes otherwise fail with permission errors.[^justfile] `.copier-answers.yml` records that the project was made from `https://github.com/linkml/linkml-project-copier` at `v0.5.0`.[^copier-answers.yml] `just update` runs `copier update` and upgrades `linkml` and `linkml-runtime` in `uv.lock`.

## Change the schema

1. Edit the files in `src/oscal/schema/`. Leave `src/oscal/schema/metaschema/` as upstream wrote it: [Move the upstream pins](update-upstream-pins.md) says how to replace it.
2. Render what OSCAL defines. Name in the pull request the metaschema definition that an element renders, and give each enum the lists it renders in `oscal_allowed_values`.
3. Follow the schema's conventions: UpperCamelCase classes and enums, OSCAL's own keys as slot names, a short description on every element, and no name shared with LOKF's, slsa's or github-actions' copies. [Element names and the shared namespace](../explanations/element-names.md) explains these.
4. Regenerate. `just gen-project` writes `project/` and the Python datamodel, `just gen-doc` writes `docs/schema/` and the element pages, and `just lokf-adapt` writes `.lokf/oscal.yaml`. Commit the output. [Generated artefacts](../datasets/generated-artefacts.md) lists what each writes.
5. Add example data to `tests/data/valid/` and `tests/data/invalid/`, named `ClassName-suffix.yaml`, with an invalid example for each constraint. [Test data and schema tests](../datasets/test-data.md) describes the folders.
6. If the change alters behaviour, not just wording, add an entry under `## [Unreleased]` in `CHANGELOG.md`.

## Check it

- `just test` runs schema generation, pytest and `linkml-validate` over `tests/data/`, and the check of the Luigi Carpio fixture.
- `just lint` runs `linkml-lint --ignore-warnings` on the schema directory, so it fails on errors only.
- `just lokf-adapt-check` fails when `.lokf/oscal.yaml` is stale against the schema or `.lokf/lokf.yaml`.
- `uvx pre-commit run` runs the hooks on what is staged, which CONTRIBUTING.md names as ruff, yamllint, codespell, typos and the `uv.lock` check. The hooks leave alone the metaschema copy, the generated files, `.lokf/lokf.yaml` and the adapt copy, the sidecar's scripts, `tests/neighbours/` and the third-party fixtures.
- Update `uv.lock`, or `.lokf/uv.lock`, in the same change as a dependency edit, because CI installs with `uv sync --locked` and fails otherwise.
- Run `cd .lokf && just lokf-validate` after a change to the knowledge bundle.

[Build and test](../workflows/main.md) runs `just test` on Python 3.10 to 3.14, and `just lint` and `just lokf-adapt-check` on Python 3.13 only.[^main.yaml] CONTRIBUTING.md says that [Lint & docs](../workflows/lint-and-docs.md) is easy to trip locally: it runs ShellCheck, actionlint, markdownlint, link checking and codespell over every Markdown file.

[^contributing.md]: CONTRIBUTING.md, Development setup and Before opening a pull request
[^justfile]: justfile, the `_wsl2_compat_check`, update, test and lint recipes
[^copier-answers.yml]: .copier-answers.yml, `_src_path` and `_commit`
[^main.yaml]: .github/workflows/main.yaml, the test job
