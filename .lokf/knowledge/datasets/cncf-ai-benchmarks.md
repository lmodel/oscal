---
type: Dataset
id: https://github.com/lmodel/oscal/knowledge/datasets/cncf-ai-benchmarks
title: CNCF AI Ecosystem OSCAL Benchmarks
description: 31 real-world OSCAL Component Definition JSON fixtures covering CNCF AI ecosystem projects (PyTorch, TensorFlow, LangChain, Kubernetes, and others), each derived from a project-specific "Governance Benchmark". Used as positive (valid) and negative (fault-injected invalid) test fixtures for ComponentDefinitionDocument schema validation.
version: "1.2.1"
resource: https://github.com/lmodel/oscal/tree/main/tests/data/cncf-ai-benchmarks
license: https://www.apache.org/licenses/LICENSE-2.0
timestamp: "2026-08-05T00:00:00Z"
source:
  - https://github.com/oscal-compass-lab/ai-benchmarks
about:
  - https://github.com/lmodel/oscal/knowledge/datasets/oscal-component-schema
distribution:
  - media_type: application/json
    access_url: https://github.com/lmodel/oscal/tree/main/tests/data/cncf-ai-benchmarks
  - media_type: application/json
    access_url: https://github.com/lmodel/oscal/tree/main/tests/data/invalid/cncf-ai-benchmarks
---

# CNCF AI Ecosystem OSCAL Benchmarks

31 `<Name>-component-definition.json` fixtures (e.g. `PyTorch-component-definition.json`, `TensorFlow-component-definition.json`, `Kubernetes-component-definition.json`), sourced from the upstream [oscal-compass-lab/ai-benchmarks](https://github.com/oscal-compass-lab/ai-benchmarks) project. Each models an OSCAL `oscal-version` 1.2.1 Component Definition with `metadata.remarks` noting it was "derived from the `<Name>` Governance Benchmark".

Two roles in the test suite:

- **`tests/data/cncf-ai-benchmarks/`** — the 31 files as-is, expected to be valid `ComponentDefinitionDocument` instances. Parametrized by `test_data.py::test_cncf_ai_benchmarks_match_generated_json_schema`.
- **`tests/data/invalid/cncf-ai-benchmarks/`** — identical copies with one fault injected: `metadata.last-modified` uses the malformed `+0000` timezone offset (no colon) instead of RFC 3339 `+00:00`, which the generated JSON Schema's date-time pattern rejects. Parametrized by `test_data.py::test_cncf_ai_benchmarks_invalid_fail_generated_json_schema`.

Both directories use native OSCAL hyphenated keys (`component-definition`, not `component_definition`); tests normalize to underscores before validating against the generated JSON Schema. Also covered by the `_test-linkml-validate` recipe in `project.justfile`, which validates both directories via `linkml-validate` after the same key-normalization step.
