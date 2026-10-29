---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "Files generated from the OSCAL schema and never edited by hand: project/ (what just gen-project writes, such as JSON Schema, JSON-LD, OWL, SHACL, ShEx, SQL, GraphQL, protobuf, Excel and TypeScript, and the further formats of just gen-project-extended), the dataclass and Pydantic models in src/oscal/datamodel/, docs/schema/oscal.yaml, the gen-doc pages in docs/elements/ and the domain schema copy .lokf/oscal.yaml."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-schema
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the table of paths and the rule to regenerate
  - id: generators.yaml
    resource: .linkml/generators.yaml
    title: the excludes and the generator arguments
  - id: justfile
    resource: justfile
    title: the gen-project, gen-python, gen-doc and _gen-yaml recipes
  - id: project.justfile
    resource: project.justfile
    title: the supplemental generator recipes and the knowledge bundle recipes
  - id: readme.md
    resource: README.md
    title: the Repository Structure section
  - resource: src/oscal/datamodel
    title: the generated Python models
  - resource: docs/schema
    title: the schema file gen-doc writes
  - resource: docs/elements
    title: the folder gen-doc writes
  - resource: scripts/issues
    title: the patched generator scripts
  - resource: .pre-commit-config.yaml
    title: the exclude list
  - resource: .gitignore
    title: the docs/elements and tmp rules
generated:
  by: process:ktl-librarian
  at: "2026-10-29T20:52:57Z"
status: draft
---

# Generated artefacts

CONTRIBUTING.md lists `src/oscal/datamodel/`, `project/` and `docs/schema/` as artefacts generated from the schema.[^contributing.md] It asks that a schema edit be followed by `just gen-project`, `just gen-doc` and `just lokf-adapt`, and that their output be committed, since `project/`, `src/oscal/datamodel/`, `docs/schema/` and `.lokf/oscal.yaml` are generated. The README says not to edit the files in `project/`.[^readme.md] The pre-commit configuration excludes all four, so that no hook rewrites what the next run would rewrite back.

## project/

`just gen-project` runs LinkML's `gen-project` with `.linkml/generators.yaml`, which skips the markdown generator and merges imports for the generators it configures.[^generators.yaml] The recipe then moves the Python output into `src/oscal/datamodel/` and writes the Pydantic model with `gen-pydantic`. It runs `gen-java`, `gen-typescript` and `gen-owl` on their own, because some generators ignore the configuration file or cannot create directories.[^justfile]

`project.justfile` adds `just gen-project-extended`, which runs the generators that `gen-project` does not cover:[^project.justfile] a merged LinkML file, resolved YAML, SSSOM, Python namespaces, a TSV summary, Graphviz, Mermaid class diagrams, a Mermaid ER diagram, PlantUML, RDF in Turtle, SPARQL queries, CSV, DBML, SQLAlchemy models, SQL validation queries, TerminusDB, TypeDB, Java, Go, Rust, C++, Pandera, a Markdown data dictionary and GOLR views. The YAML, RDF, DBML, Java, Pandera and Markdown data dictionary recipes run patched scripts from `scripts/issues/`, and each script's docstring names the upstream generator bug it works around. For example, a comment says that `gen-java` without merged imports generates no file, because the root schema's classes are all defined in the modules it imports.

`project/` holds one folder for each of `cpp`, `csv`, `dbml`, `erdiagram`, `excel`, `golang`, `golr`, `graphql`, `graphviz`, `java`, `jsonld`, `jsonschema`, `linkml`, `markdown-datadict`, `mermaid`, `namespaces`, `owl`, `pandera`, `plantuml`, `prefixmap`, `protobuf`, `rdf`, `rust`, `shacl`, `shex`, `sqla`, `sqlschema`, `sqlvalidation`, `sssom`, `summary`, `terminusdb`, `typedb`, `typescript` and `yaml`. `tests/test_data.py` validates the example data against `project/jsonschema/oscal.schema.json`, the generated JSON Schema.

## The Python models

`src/oscal/datamodel/oscal.py` holds the dataclasses, and `src/oscal/datamodel/oscal_pydantic.py` holds the Pydantic models. `just gen-python` regenerates both, and `just test` runs it before pytest. [Validate OSCAL data against the schema](../playbooks/validate-data.md) says what the dataclasses check.

## docs/schema/ and docs/elements/

`just gen-doc` writes `docs/schema/oscal.yaml` with `gen-yaml`, and the schema's Markdown pages into `docs/elements/` with `gen-doc`. Git ignores the pages in `docs/elements/`, and the [documentation site](../services/documentation-site.md) builds them when it needs them.

## The domain schema copy

`just lokf-adapt` writes `.lokf/oscal.yaml`, the bundle's domain schema, and `just lokf-adapt-check` fails when it is stale against the schema or `.lokf/lokf.yaml`. [OSCAL Schema (top-level)](oscal-schema.md) says what the copy is, and [Element names and the shared namespace](../explanations/element-names.md) says what it renames.

[^contributing.md]: CONTRIBUTING.md, the table of paths and the first item of Before opening a pull request
[^readme.md]: README.md, the Repository Structure section
[^generators.yaml]: .linkml/generators.yaml, excludes and generator_args
[^justfile]: justfile, the gen-project, gen-python, gen-doc and `_gen-yaml` recipes
[^project.justfile]: project.justfile, the supplemental generator recipes and gen-project-extended
