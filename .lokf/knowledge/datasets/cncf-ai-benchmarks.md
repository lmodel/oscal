---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/cncf-ai-benchmarks
title: CNCF AI Ecosystem OSCAL Benchmarks
description: 31 OSCAL component definitions from oscal-compass-lab/ai-benchmarks, one for each of 31 CNCF AI ecosystem projects (PyTorch, TensorFlow, LangChain, Kubernetes and others), in tests/data/cncf-ai-benchmarks/ under Apache-2.0, with fault-injected copies in tests/data/invalid/cncf-ai-benchmarks/ whose last-modified offset is +0000; tests/test_data.py and just test validate both as ComponentDefinitionDocument after rewriting their keys with underscores.
version: 1.2.1
resource: tests/data/cncf-ai-benchmarks
license: https://www.apache.org/licenses/LICENSE-2.0
timestamp: "2026-08-05T00:00:00Z"
source:
  - https://github.com/oscal-compass-lab/ai-benchmarks
about:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-component-schema
distribution:
  - media_type: application/json
    access_url: https://github.com/lmodel/oscal/tree/main/tests/data/cncf-ai-benchmarks
  - media_type: application/json
    access_url: https://github.com/lmodel/oscal/tree/main/tests/data/invalid/cncf-ai-benchmarks
genre: reference
isPartOf:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/test-data
sources:
  - id: cncf-ai-benchmarks
    resource: tests/data/cncf-ai-benchmarks
    title: the 31 files and their metadata
  - id: data-readme.md
    resource: tests/data/README.md
    title: the cncf-ai-benchmarks items and the naming convention
  - id: notice
    resource: NOTICE
    title: the Test fixtures section
  - id: test_data.py
    resource: tests/test_data.py
    title: the two CNCF tests
  - id: project.justfile
    resource: project.justfile
    title: the CNCF part of _test-linkml-validate
  - resource: tests/data/invalid/cncf-ai-benchmarks
    title: the fault-injected copies
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:56:26Z"
  revision: bdb583e206869df24d631c65d97fbe26584f852a
---

# CNCF AI Ecosystem OSCAL Benchmarks

`tests/data/cncf-ai-benchmarks/` holds 31 files named `<Name>-component-definition.json`, such as `PyTorch-component-definition.json`, `TensorFlow-component-definition.json` and `Kubernetes-component-definition.json`.[^cncf-ai-benchmarks] Each file's metadata gives `oscal-version` 1.2.1, while the schema renders OSCAL 1.2.3. Each file's `remarks` say that the component definition is derived from the project's governance benchmark, as in "Component definition derived from PyTorch Governance Benchmark".

`tests/data/README.md` calls them real-world OSCAL component definitions covering CNCF AI ecosystem projects, and treats every file in the folder as a `ComponentDefinitionDocument`, whatever its prefix.[^data-readme.md] NOTICE says that they come from oscal-compass-lab/ai-benchmarks, <https://github.com/oscal-compass-lab/ai-benchmarks>, licensed under the Apache License, Version 2.0.[^notice]

## Two roles in the tests

- `tests/data/cncf-ai-benchmarks/` holds the 31 files as they are, and each must be a valid `ComponentDefinitionDocument`.
- `tests/data/invalid/cncf-ai-benchmarks/` holds copies with the same names and one fault injected in each: `metadata.last-modified` uses the malformed `+0000` time zone offset instead of RFC 3339's `+00:00`, which the generated JSON Schema's date-time pattern rejects. Each copy must fail.

The files use OSCAL's native hyphenated keys, such as `component-definition`. `tests/test_data.py` rewrites their keys with underscores and checks each against `ComponentDefinitionDocument` in the generated JSON Schema.[^test_data.py] The `_test-linkml-validate` recipe in `project.justfile`, which `just test` runs, rewrites them the same way in a temporary copy and runs `linkml-validate` with `src/oscal/schema/oscal_component.yaml`.[^project.justfile] See [Test data and schema tests](test-data.md).

[^cncf-ai-benchmarks]: tests/data/cncf-ai-benchmarks, the 31 files and their metadata
[^data-readme.md]: tests/data/README.md, the cncf-ai-benchmarks items and Naming conventions
[^notice]: NOTICE, the Test fixtures section
[^test_data.py]: tests/test_data.py, test_cncf_ai_benchmarks_match_generated_json_schema and test_cncf_ai_benchmarks_invalid_fail_generated_json_schema
[^project.justfile]: project.justfile, the cncf-ai-benchmarks part of `_test-linkml-validate`
