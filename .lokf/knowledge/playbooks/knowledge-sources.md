---
type: Playbook
id: https://w3id.org/lmodel/oscal/knowledge/playbooks/knowledge-sources
title: Knowledge Sources
description: "The librarian's scrape map: every repository location and external page this bundle derives concepts from (schema, metaschema copy, adapt copy, generated artefacts, tests and fixtures, workflows, website, governance files), the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose."
timestamp: "2026-08-05T00:00:00Z"
resource: .
genre: reference
sources:
  - resource: README.md
  - resource: docs/about.md
  - resource: docs/index.md
  - resource: src/oscal/schema
  - resource: src/oscal/schema/metaschema
  - resource: src/oscal/datamodel
  - resource: project.justfile
  - resource: .lokf/oscal.yaml
  - resource: .lokf/justfile
  - resource: NOTICE
  - resource: LICENSE
  - resource: scripts/check_upstream_release.py
  - resource: scripts/issues
  - resource: .github/scripts
  - resource: .github/workflows
  - resource: .github/dependabot.yml
  - resource: justfile
  - resource: config.yaml
  - resource: config.public.mk
  - resource: .linkmllint.yaml
  - resource: .copier-answers.yml
  - resource: .pre-commit-config.yaml
  - resource: project
  - resource: docs/schema
  - resource: docs/elements
  - resource: tests
  - resource: examples/README.md
  - resource: CONTRIBUTING.md
  - resource: .releaserc.json
  - resource: CHANGELOG.md
  - resource: pyproject.toml
  - resource: uv.lock
  - resource: website
  - resource: SECURITY.md
  - resource: AI_COVENANT.md
  - resource: lychee.toml
  - resource: .markdownlint-cli2.jsonc
  - resource: .github/ISSUE_TEMPLATE
  - resource: .github/pull_request_template.md
  - resource: .github/PULL_REQUEST_TEMPLATE
  - resource: CODE_OF_CONDUCT.md
  - resource: .gitignore
  - resource: .editorconfig
  - resource: .yamllint.yaml
  - resource: src/README.md
  - resource: docs/templates-linkml
  - resource: src/oscal/__init__.py
  - resource: src/oscal/_version.py
  - resource: llms.txt
  - resource: knowledge_bundle
generated:
  by: process:ktl-librarian
  at: "2026-10-29T01:15:40Z"
verified:
  - by: process:ktl-librarian
    at: "2026-10-29T01:19:01Z"
---

# Knowledge Sources

Steady-state refresh runs re-verify these sources instead of discovering them again. Update this map whenever a knowledge source in the repository is added, moved or removed.

Each concept derived from a file or folder of this repository names it by its path from the repository root, in `resource` and in `sources`, with the commit it was read at in `generated.revision`. `knowledge-report.sh worklist` lists the concepts whose source moved since their stamp. It never fetches a page, so re-read the external pages this table names when the release they describe moves.

| Source | Yields | Re-check by |
| --- | --- | --- |
| `src/oscal/schema/oscal.yaml`, `src/oscal/schema/README.md`, `config.public.mk` | `datasets/oscal-schema` | re-read the header's `version`, `source`, annotations, `see_also` and comment, and the imports |
| the eight `src/oscal/schema/oscal_*.yaml` modules | the eight module concepts in `datasets/` | re-read each header's `id`, title, `version`, `source`, imports and `see_also`, each subset, and the required slots of each model class and its document class |
| `project.justfile` (the knowledge bundle recipes), `.lokf/oscal.yaml`, `.lokf/justfile`, the README's Knowledge Trust Ladder (KTL) section | the domain schema section of `datasets/oscal-schema`, `explanations/element-names` | re-read the `--root` list, the `LOKF_CMD` note, the copy's header and last note, the `schema :=` line, the renamed classes and keys and the seven shared keys |
| `README.md` (What it models, Influences, Mappings, Not modelled here), `docs/about.md`, `.linkmllint.yaml`, the `class_` comment in `oscal_catalog.yaml` | `explanations/scope-and-influences`, `explanations/element-names`, `references/nist-oscal` | re-read each section and comment |
| `src/oscal/schema/metaschema/`, the OSCAL metaschema section of `NOTICE` | `datasets/metaschema-copy` | re-read the commit and release NOTICE names, and list the folder; the upstream watch compares the blobs weekly |
| `scripts/check_upstream_release.py`, `.github/scripts/report-issue.sh` | `playbooks/update-upstream-pins`, `workflows/upstream-watch` | re-read `PINNED_TAG`, `PINNED_COMMIT`, `PINNED_PATH`, `ELSEWHERE`, the report's instructions and the issue title |
| `justfile`, `config.yaml`, `project/`, `src/oscal/datamodel/`, `docs/schema/`, `docs/elements/`, `scripts/issues/`, `.pre-commit-config.yaml`, `.gitignore` | `datasets/generated-artefacts` | re-read the `gen-project`, `gen-python`, `gen-doc`, `_gen-yaml` and `gen-project-extended` recipes and the `excludes`; re-list `project/*/` |
| `tests/data/`, `tests/test_data.py`, `tests/test_schema_rules.py`, `tests/neighbours/`, `examples/README.md`, the test recipes of `justfile` and `project.justfile` | `datasets/test-data`, `datasets/cncf-ai-benchmarks`, `datasets/luigi-carpio-component-definition`, `playbooks/validate-data` | re-count `valid/`, `invalid/` and `problem/`; re-read the naming rule, the tests, the comment on the neighbours, and each fixture's metadata, README and licence |
| `CONTRIBUTING.md`, `.copier-answers.yml`, the `update`, `test` and `lint` recipes of `justfile` | `playbooks/regenerate-and-test` | confirm the setup, the checklist and the recipes |
| `.releaserc.json`, `.github/scripts/changelog-release.mjs`, `CHANGELOG.md`, `pyproject.toml`, the Releasing section of `CONTRIBUTING.md` | `playbooks/release` | re-read the release rules, the commands, the baseline paragraph and the versioning settings |
| the nine files in `.github/workflows/` | the nine `workflows/` concepts | re-read each file's `on` key and top-level `permissions`, and each job's id, `name`, `runs-on`, `permissions` and `environment` |
| `website/`, `lychee.toml`, `.markdownlint-cli2.jsonc` | `services/documentation-site`, `workflows/lint-and-docs` | re-read `site.config.mjs`, `website/README.md` and the link check's exclusions |
| `NOTICE`, `LICENSE`, `website/NOTICE`, the licence files of the metaschema copy and the Luigi Carpio fixture, the License sections of `README.md` and `CONTRIBUTING.md` | `policies/license-and-attribution` | re-read each third-party entry |
| `SECURITY.md`, `.github/dependabot.yml` | `policies/security-policy` | re-read the table of surfaces and the settings not yet in force |
| `AI_COVENANT.md` | `policies/ai-covenant` | re-read the project note and the section on agent automation |
| `.copier-answers.yml`, `pyproject.toml`, `uv.lock` | `org/lmodel`, `references/linkml` | re-read `github_org`, the authors, the dependencies and the locked LinkML versions |
| `https://pages.nist.gov/OSCAL/`, `https://linkml.io/` | `references/nist-oscal`, `references/linkml` | external pages, which these concepts describe from the repository's own files; re-read those files, and the upstream watch reports a newer OSCAL release |

These are not knowledge sources, and are left out:

- `.github/ISSUE_TEMPLATE/`, `.github/pull_request_template.md` and `CODE_OF_CONDUCT.md` (governance text);
- `.editorconfig` and `.yamllint.yaml` (tooling);
- `src/README.md`, `docs/index.md`, `docs/templates-linkml/` and `project/README.md` (text from the project template);
- `src/oscal/__init__.py`, `src/oscal/_version.py` and `tests/__init__.py` (package and test plumbing);
- `llms.txt` (the pointer that sends agents to this bundle);
- the `knowledge_bundle` link, which belongs to the sidecar, as does everything under `.lokf/` apart from the domain schema and the justfile's `schema :=` line.
