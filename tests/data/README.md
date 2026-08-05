# Example data for oscal

This folder contains example data for testing and demonstrating the datamodel,
sorted in subfolders:

- `valid/` — YAML fixtures conforming to the datamodel. Used to verify the datamodel
  (parametrized by `test_data.py::test_valid_data_files`).
- `invalid/` — YAML fixtures that must fail validation. Used to verify that the schema
  rejects bad data (parametrized by `test_data.py::test_invalid_data_files`).
  - `invalid/cncf-ai-benchmarks/` — copies of the `cncf-ai-benchmarks/` fixtures below,
    each with a single fault injected (`metadata.last-modified` uses the malformed
    `+0000` timezone offset instead of RFC 3339 `+00:00`). Must fail
    `ComponentDefinitionDocument` validation; parametrized by
    `test_data.py::test_cncf_ai_benchmarks_invalid_fail_generated_json_schema` and
    covered by the `_test-linkml-validate` recipe in `project.justfile`.
- `problem/` — Fixtures documenting known model quirks not yet handled correctly in the
  current schema version, split into `problem/valid/` and `problem/invalid/`. Referenced
  directly by individual tests, not part of the main parametrized runs.
- `cncf-ai-benchmarks/` — 31 real-world OSCAL Component Definition JSON files covering
  CNCF AI ecosystem projects (e.g. PyTorch, TensorFlow, LangChain, Kubernetes). All are
  valid `ComponentDefinitionDocument` instances validated by
  `test_data.py::test_cncf_ai_benchmarks_match_generated_json_schema` and the
  `_test-linkml-validate` recipe in `project.justfile`.
- `luigi_carpio/` — A real-world OSCAL Component Definition JSON file mapping NIST
  800-53 Rev 5 controls to AWS services (FedRAMP High + CJIS). Validated by the
  `test-luigi-carpio` recipe in `project.justfile`.
- `open_control/` — Reference files in the **OpenControl format** (v1.0.0, v3.0.0,
  v3.1.0), a predecessor compliance format with its own schema (`satisfies`,
  `control_key`, `schema_version`, etc.). These are **not OSCAL** and cannot be
  validated against the OSCAL LinkML schema or generated JSON Schema; they are kept
  as reference material for format-comparison and migration context.

## Naming conventions

**`valid/` and `invalid/`** filenames must follow `ClassName-suffix.yaml` where
`ClassName` is an exact class name from the schema. The class is derived by splitting
the stem at the first `-` and taking the part before it (e.g. `Observation-001.yaml`
→ `Observation`). The suffix can be a number or any filename-safe string.

**`cncf-ai-benchmarks/`** filenames follow `ProjectName-component-definition.json`.
All files in this directory are treated as `ComponentDefinitionDocument` instances
regardless of the prefix. See [https://github.com/oscal-compass-lab/ai-benchmarks](https://github.com/oscal-compass-lab/ai-benchmarks).
