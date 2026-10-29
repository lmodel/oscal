---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/test-data
genre: reference
title: Test data and schema tests
description: "Example instances of the OSCAL schema in tests/data/: 36 valid files and 26 counter-examples, each named after the class it instantiates (Catalog-001.yaml, Profile-missing-imports.yaml), with an example and a counter-example for every model, the problem/ fixtures and two third-party OSCAL sets; tests/test_data.py and just test hold them to the dataclasses, the generated JSON Schema and linkml-validate, and tests/test_schema_rules.py holds the schema to the metaschema copy and the adapt copy's names apart from LOKF's, slsa's and github-actions'."
resource: tests/data
about:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-schema
hasPart:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/cncf-ai-benchmarks
  - https://w3id.org/lmodel/oscal/knowledge/datasets/luigi-carpio-component-definition
references:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/metaschema-copy
sources:
  - id: data-readme.md
    resource: tests/data/README.md
    title: the folders and the naming conventions
  - id: changelog.md
    resource: CHANGELOG.md
    title: the item on examples
  - id: test_data.py
    resource: tests/test_data.py
    title: the docstring, the fixture tests and the allow-other tests
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the seven tests and the comment on the neighbours
  - id: justfile
    resource: justfile
    title: the test recipe and its parts
  - id: project.justfile
    resource: project.justfile
    title: _test-linkml-validate and test-luigi-carpio
  - resource: tests/neighbours
    title: the slsa and github-actions adapt copies
  - resource: examples/README.md
    title: the examples/output folder
  - resource: CONTRIBUTING.md
    title: the rule on example data
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:56:26Z"
  revision: 57a6e461e82c2896a6fceb786029f75b32ec8668
status: draft
---

# Test data and schema tests

`tests/data/README.md` sorts the example data into folders:[^data-readme.md]

- `valid/` holds YAML fixtures that conform to the datamodel;
- `invalid/` holds YAML fixtures that must fail validation, and `invalid/cncf-ai-benchmarks/`;
- `problem/` holds fixtures that document known model quirks not yet handled correctly, split into `problem/valid/` and `problem/invalid/`, which individual tests reference directly;
- `cncf-ai-benchmarks/` and `luigi_carpio/` hold third-party OSCAL component definitions: see [CNCF AI Ecosystem OSCAL Benchmarks](cncf-ai-benchmarks.md) and [NIST 800-53 Rev 5 to AWS Service Mapping (Luigi Carpio)](luigi-carpio-component-definition.md).

A file in `valid/` or `invalid/` is named `ClassName-suffix.yaml`. The part before the first hyphen is an exact class name from the schema, and the suffix is a number or any other string a file name allows. CONTRIBUTING.md asks for an invalid example for each constraint.

## The examples

`tests/data/valid/` holds 36 files and `tests/data/invalid/` holds 26 counter-examples. Each of the eight models, from `Catalog` to `MappingCollection`, has at least one of each, which CHANGELOG.md describes as an example of each model and a counter-example for each one's required content.[^changelog.md] The counter-examples include `Profile-missing-imports.yaml`, `SystemSecurityPlan-missing-system-characteristics.yaml`, `MappingCollection-missing-provenance.yaml` and `AtFrequency-zero-period.yaml`. `problem/valid/` holds 5 files and `problem/invalid/` holds 3.

## tests/test_data.py

The module's docstring says that every class is loaded from `oscal.datamodel.oscal`, the dataclasses generated from `src/oscal/schema/oscal.yaml`.[^test_data.py] Its tests do four things:

- load each valid file into the dataclass its name gives, and check it against that class's definition in the generated JSON Schema, `project/jsonschema/oscal.schema.json`;
- check that each counter-example fails to load into its dataclass and fails the generated JSON Schema. Four counter-examples are skipped for the dataclass, because the Python model cannot enforce their constraint: `AssessmentPlan-bad-last-modified.yaml`, `CatalogDocument-bad-uuid-only.yaml`, `AtFrequency-zero-period.yaml` and `PortRange-negative-start.yaml`. A comment says that the dataclasses check no minimum, which the generated JSON Schema does;
- rewrite the hyphenated keys of each CNCF fixture with underscores and check it against `ComponentDefinitionDocument` in the generated JSON Schema: the valid copies must pass, and the fault-injected copies must fail;
- check that three enums marked `allow_any: true` carry the annotation, and record as expected failures that the generated enum classes do not yet accept a value outside the declared set.

The docstring also says that some generated classes read hyphenated alias keys, so the loader injects those keys by hand for a few classes, such as `Observation`, `Risk` and `AssessmentPlan`. [Validate OSCAL data against the schema](../playbooks/validate-data.md) says what each check leaves out.

## tests/test_schema_rules.py

Its seven tests check that the schema agrees with the OSCAL release it is pinned to, and that the adapt copy's names stay apart from its neighbours':[^test_schema_rules.py]

- the header's `oscal_tag`, `oscal_commit` and `source` match the pins in `scripts/check_upstream_release.py`, and the tag is `v` followed by the header's `version`;
- every module carries the umbrella's `version`, and each module's `source` is that release's JSON schema;
- every module's id lies under the umbrella's namespace, and every module's default prefix is `oscal:`;
- each enum names its metaschema lists in `oscal_allowed_values`, and holds exactly their values: see [OSCAL metaschema copy](metaschema-copy.md);
- no class, enum, type or subset name of `.lokf/oscal.yaml` is LOKF's, and a slot name the two share carries LOKF's IRI;
- no such name is shared with `tests/neighbours/slsa.yaml` or `tests/neighbours/github-actions.yaml`, and the only keys shared with them under another IRI are the seven listed: see [Element names and the shared namespace](../explanations/element-names.md).

A comment says that the two neighbours are adapt copies that other lmodel repositories release, each the schema asset of a release checked against its `.sha256` and attestation: slsa v0.7.0 and github-actions v0.1.0.

## How they run

`just test` runs five recipes.[^justfile] `_test-schema` generates the project into `tmp/`. `_test-python` regenerates the Python models and runs pytest. `_test-examples` runs `linkml-run-examples` over `tests/data/valid/` and `tests/data/invalid/`, and writes what it converts into `examples/output/`, which git ignores. The other two come from `project.justfile`.[^project.justfile] `_test-linkml-validate` runs `linkml-validate` on every file in `valid/` and `invalid/` against the module that defines its class, or the umbrella, and on the CNCF fixtures with their keys rewritten. `test-luigi-carpio` checks the Luigi Carpio fixture. [Build and test](../workflows/main.md) runs `just test` on every pull request.

[^data-readme.md]: tests/data/README.md, the folder list and Naming conventions
[^changelog.md]: CHANGELOG.md, the Added items of the Unreleased section
[^test_data.py]: tests/test_data.py, the docstring, NON_FAILING_INVALID_FIXTURES and the test functions
[^test_schema_rules.py]: tests/test_schema_rules.py, the seven test functions and the comment above COPY
[^justfile]: justfile, the test, `_test-schema`, `_test-python` and `_test-examples` recipes
[^project.justfile]: project.justfile, `_test-linkml-validate` and test-luigi-carpio
