---
type: Reference
id: https://w3id.org/lmodel/oscal/knowledge/references/linkml
title: LinkML
description: "LinkML, the Linked Data Modeling Language the OSCAL schema is written in: the repository was built from linkml-project-copier v0.5.0, uv.lock pins linkml and linkml-runtime 1.11.1, and its recipes run LinkML's generators (gen-project, gen-pydantic, gen-doc, gen-java, gen-owl), linkml-lint, linkml-validate and linkml-run-examples; the tests record where the generated code falls short."
resource: https://linkml.io/
timestamp: "2026-08-05T00:00:00Z"
about: []
genre: reference
relatedTo:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-schema
  - https://w3id.org/lmodel/oscal/knowledge/datasets/generated-artefacts
sources:
  - id: readme.md
    resource: README.md
    title: the Credits section
  - id: copier-answers.yml
    resource: .copier-answers.yml
    title: _src_path and _commit
  - id: pyproject.toml
    resource: pyproject.toml
    title: the dependencies
  - id: uv.lock
    resource: uv.lock
    title: the linkml and linkml-runtime entries
  - id: justfile
    resource: justfile
    title: the generator, lint and test recipes
  - id: test_data.py
    resource: tests/test_data.py
    title: the alias workarounds and the allow-other tests
  - resource: src/oscal/schema/oscal.yaml
    title: the linkml prefix and the linkml:types import
  - resource: SECURITY.md
    title: Not covered
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:56:26Z"
---

# LinkML

The OSCAL schema is a LinkML schema: every schema file in `src/oscal/schema/` binds the prefix `linkml:` to `https://w3id.org/linkml/` and imports `linkml:types`. The README says that the repository was built from the linkml-project-copier template, which it credits by the DOI `10.5281/zenodo.15163584`.[^readme.md] `.copier-answers.yml` records the template's address, `https://github.com/linkml/linkml-project-copier`, at `v0.5.0`.[^copier-answers.yml]

## Versions

`pyproject.toml` requires `linkml-runtime` 1.9.4 or later, and its `dev` group `linkml` 1.9.3 or later and `jsonschema`.[^pyproject.toml] `uv.lock` pins `linkml` 1.11.1 and `linkml-runtime` 1.11.1.[^uv.lock]

## The tools the recipes run

The justfile runs LinkML's `gen-project` for most generated formats, and `gen-pydantic`, `gen-java`, `gen-typescript` and `gen-owl` on their own. It runs `gen-yaml` and `gen-doc` for the documentation, `linkml-lint` for `just lint`, and `linkml-run-examples` in `just test`.[^justfile] `project.justfile` runs `linkml-validate` over the example data and many further generators: [Generated artefacts](../datasets/generated-artefacts.md) lists them, and notes the patched scripts in `scripts/issues/` that work around generator bugs.

## Where the generated code falls short

`tests/test_data.py` records two limits of the generated Python code.[^test_data.py] Some generated classes read hyphenated alias keys during construction, so the test loader injects those keys by hand for a few classes, and its docstring says that issues were raised upstream with LinkML. A generated enum class does not accept a value outside its declared set, even for an enum that allows other values, and the tests mark that as an expected failure. SECURITY.md says that problems in LinkML, its generators and its runtime are reported to LinkML.

[^readme.md]: README.md, the Credits section
[^copier-answers.yml]: .copier-answers.yml, `_src_path` and `_commit`
[^pyproject.toml]: pyproject.toml, dependencies and dependency-groups
[^uv.lock]: uv.lock, the linkml and linkml-runtime packages
[^justfile]: justfile, the gen-project, gen-python, gen-doc, `_gen-yaml`, lint and `_test-examples` recipes
[^test_data.py]: tests/test_data.py, the docstring of `_validate_schema` and the allow-other tests
