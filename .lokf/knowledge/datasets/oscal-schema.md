---
type: Dataset
id: https://github.com/lmodel/oscal/knowledge/datasets/oscal-schema
title: OSCAL Schema (top-level)
description: Aggregating top-level LinkML schema for OSCAL (Open Security Controls Assessment Language). Imports all eight domain sub-schemas and provides the shared namespace.
version: "1.2.1"
resource: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal.yaml
license: https://www.apache.org/licenses/LICENSE-2.0
timestamp: "2026-08-05T00:00:00Z"
derivedFrom:
  - https://github.com/lmodel/oscal/knowledge/references/nist-oscal
references:
  - https://github.com/lmodel/oscal/knowledge/references/linkml
hasPart:
  - https://github.com/lmodel/oscal/knowledge/datasets/oscal-catalog-schema
  - https://github.com/lmodel/oscal/knowledge/datasets/oscal-profile-schema
  - https://github.com/lmodel/oscal/knowledge/datasets/oscal-ssp-schema
  - https://github.com/lmodel/oscal/knowledge/datasets/oscal-assessment-plan-schema
  - https://github.com/lmodel/oscal/knowledge/datasets/oscal-assessment-results-schema
  - https://github.com/lmodel/oscal/knowledge/datasets/oscal-component-schema
  - https://github.com/lmodel/oscal/knowledge/datasets/oscal-mapping-schema
  - https://github.com/lmodel/oscal/knowledge/datasets/oscal-poam-schema
distribution:
  - media_type: application/yaml
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal.yaml
---

# OSCAL Schema (top-level)

The **OSCAL top-level schema** (`src/oscal/schema/oscal.yaml`) is the aggregating entry-point for the full OSCAL LinkML schema. It imports the eight domain sub-schemas (`oscal_catalog`, `oscal_profile`, `oscal_ssp`, `oscal_assessment_plan`, `oscal_assessment_results`, `oscal_component`, `oscal_mapping`, `oscal_poam`) and declares the shared `oscal:` prefix bound to `https://w3id.org/lmodel/oscal/`.

OSCAL version modeled: **1.2.1** (last-modified 2026-03-27).

The schema is the source of truth for all generated artifacts under `project/` (JSON Schema, OWL, SHACL, RDF, TypeScript, Python datamodel, Go, Rust, Protobuf, and more).
