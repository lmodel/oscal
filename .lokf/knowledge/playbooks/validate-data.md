---
type: Playbook
id: https://w3id.org/lmodel/oscal/knowledge/playbooks/validate-data
genre: how-to
title: Validate OSCAL data against the schema
description: How to check an OSCAL document against the schema with linkml-validate, naming the module and the class (-s src/oscal/schema/oscal_catalog.yaml -C Catalog), after rewriting native OSCAL JSON's hyphenated keys with underscores; what the generated JSON Schema and the dataclasses check, and the metaschema constraints no tool here checks.
resource: project.justfile
about:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-schema
references:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/test-data
  - https://w3id.org/lmodel/oscal/knowledge/explanations/scope-and-influences
sources:
  - id: project.justfile
    resource: project.justfile
    title: _test-linkml-validate
  - id: test_data.py
    resource: tests/test_data.py
    title: the docstring, the key normalisation, the validators and the allow-other tests
  - id: readme.md
    resource: README.md
    title: Not modelled here
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:56:26Z"
  revision: 3d2fe54c16b683d245e50f5a3c95087554bd641e
status: draft
---

# Validate OSCAL data against the schema

The `_test-linkml-validate` recipe in `project.justfile`, which `just test` runs, validates each example with `linkml-validate`. It names the module that defines the example's class, and the class itself.[^project.justfile] For one file, the command is:

```bash
uv run linkml-validate -s src/oscal/schema/oscal_catalog.yaml -C Catalog tests/data/valid/Catalog-001.yaml
```

The recipe checks a class that its map gives no module against the umbrella, `src/oscal/schema/oscal.yaml`.

## OSCAL's hyphenated keys

A comment in the recipe says that native OSCAL JSON uses hyphenated keys, and that the schema uses underscores. So the recipe rewrites every key of a CNCF fixture with underscores before it validates the fixture as a `ComponentDefinitionDocument`. `tests/test_data.py` does the same before it checks a fixture against the generated JSON Schema, and rewrites keys only, never values such as the property name `fedramp-high`.[^test_data.py] Its docstring says that the keys of the fixtures in `tests/data/valid/` and `tests/data/invalid/` were migrated to underscores for JSON Schema compatibility.

## What each check covers

`tests/test_data.py` checks every example two ways:

- against the class's definition in the generated JSON Schema, `project/jsonschema/oscal.schema.json`, which a test's docstring calls the schema-level backstop for pattern, strict-enum and other constraints;
- by loading it into the generated dataclasses in `oscal.datamodel.oscal`, which check less. A comment says that the dataclasses check no minimum, and four counter-examples, such as `AtFrequency-zero-period.yaml`, load into them without an error.

A generated enum class raises on a value outside its declared set, even for an enum that allows other values, and the tests mark that as an expected failure. A dataclass, on the other hand, stores any string for an `Observation`'s `methods`, which `problem/invalid/Observation-bad-enum.yaml` documents as a known limitation.

## What no tool here checks

The README says that the schema does not check the keys an `index`, `index-has-key` or `is-unique` constraint names, `expect` tests or `has-cardinality` counts. So a document that passes it can still fail NIST's own validators.[^readme.md] [Scope, influences and mappings](../explanations/scope-and-influences.md) says what else the schema leaves out.

[^project.justfile]: project.justfile, the `_test-linkml-validate` recipe and its comments
[^test_data.py]: tests/test_data.py, the docstring, `_normalize_keys`, NON_FAILING_INVALID_FIXTURES and the allow-other tests
[^readme.md]: README.md, the Not modelled here section
