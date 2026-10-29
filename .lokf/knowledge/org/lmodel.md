---
type: Organization
id: https://w3id.org/lmodel/oscal/knowledge/org/lmodel
title: lmodel
description: lmodel, the GitHub organization that holds this repository (github.com/lmodel/oscal), its documentation site at lmodel.github.io/oscal and the schema's w3id namespace under w3id.org/lmodel/oscal/, and the publisher of this bundle; lmodel/slsa and lmodel/github-actions release the adapt copies the tests read as neighbours.
resource: https://github.com/lmodel
timestamp: "2026-08-05T00:00:00Z"
sources:
  - id: copier-answers.yml
    resource: .copier-answers.yml
    title: github_org
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Development setup
  - id: readme.md
    resource: README.md
    title: Documentation Website and Influences
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the comment above COPY
  - id: notice
    resource: NOTICE
    title: the copyright line
  - resource: pyproject.toml
    title: the authors
  - resource: .lokf/knowledge/index.md
    title: the publisher key
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:53:56Z"
---

# lmodel

**lmodel** is the GitHub organization that holds this repository: `.copier-answers.yml` records `github_org: lmodel`, and CONTRIBUTING.md clones `https://github.com/lmodel/oscal.git`.[^copier-answers.yml] [^contributing.md] The README gives the documentation site's address as `https://lmodel.github.io/oscal`, and the schema's namespace is `https://w3id.org/lmodel/oscal/`.[^readme.md] The bundle's root `index.md` names lmodel as the bundle's publisher.

The README says that the schema's module layout, release asset and governance files follow lmodel/slsa. `tests/test_schema_rules.py` reads the adapt copies that two other lmodel repositories release, slsa v0.7.0 and github-actions v0.1.0.[^test_schema_rules.py] NOTICE gives the copyright as 2026 Noel McLoughlin, whom `pyproject.toml` names as the author.[^notice]

The organization's page is <https://github.com/lmodel>.

[^copier-answers.yml]: .copier-answers.yml, github_org
[^contributing.md]: CONTRIBUTING.md, Development setup
[^readme.md]: README.md, Documentation Website and Influences
[^test_schema_rules.py]: tests/test_schema_rules.py, the comment above COPY
[^notice]: NOTICE, the copyright line
