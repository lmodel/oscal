---
type: Reference
id: https://github.com/lmodel/oscal/knowledge/references/linkml
title: LinkML
description: The Linked Data Modeling Language. A framework for authoring schemas in YAML that generate JSON Schema, OWL, SHACL, RDF, and multiple programming-language datamodels. All OSCAL schemas in this repository are authored in LinkML.
resource: https://linkml.io/
timestamp: "2026-08-05T00:00:00Z"
about:
  - https://github.com/lmodel/oscal/knowledge/datasets/oscal-schema
---

# LinkML

**LinkML (Linked Data Modeling Language)** is an open framework for data modeling that bridges the gap between relational, object-oriented, and linked-data worlds. You author schemas in readable YAML; the `linkml` toolkit generates:

- JSON Schema, SHACL, OWL
- Python, TypeScript, Java, Go, Rust datamodels
- RDF/Turtle representations
- Documentation (Markdown, HTML)

All nine OSCAL schema files in `src/oscal/schema/` are authored in LinkML YAML. The `project/` directory contains artifacts generated from them by the `gen-project` recipe in `justfile`.

**Key references:**
- Specification & docs: <https://linkml.io/>
- GitHub: <https://github.com/linkml/linkml>
- W3ID namespace: `https://w3id.org/linkml/`
