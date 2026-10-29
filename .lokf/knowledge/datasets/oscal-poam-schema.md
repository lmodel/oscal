---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-poam-schema
title: OSCAL POA&M Schema
description: "The plan of action and milestones module of the OSCAL schema, `src/oscal/schema/oscal_poam.yaml` (id `https://w3id.org/lmodel/oscal/oscal_poam`, OSCAL 1.2.3): the PlanOfActionAndMilestones model of the risks a system still carries and how they are tracked, through its POA&M items, with PoamDocument as its document root; it imports the catalog and assessment plan modules."
version: 1.2.3
resource: src/oscal/schema/oscal_poam.yaml
license: https://www.apache.org/licenses/LICENSE-2.0
timestamp: "2026-08-05T00:00:00Z"
source:
  - https://github.com/usnistgov/OSCAL/tree/e061961c7702afeabffdf5e59894d35e748dade1/src/metaschema
isPartOf:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-schema
derivedFrom:
  - https://w3id.org/lmodel/oscal/knowledge/references/nist-oscal
  - https://w3id.org/lmodel/oscal/knowledge/datasets/metaschema-copy
references:
  - https://w3id.org/lmodel/oscal/knowledge/references/linkml
distribution:
  - media_type: application/yaml
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_poam.yaml
genre: reference
dependsOn:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-catalog-schema
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-assessment-plan-schema
sources:
  - id: oscal_poam.yaml
    resource: src/oscal/schema/oscal_poam.yaml
    title: the header, the subset and PlanOfActionAndMilestones
  - id: readme.md
    resource: README.md
    title: the What it models section
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:53:56Z"
  revision: 7746495c7a27992c40ebd9cff16858020a82696e
---

# OSCAL POA&M Schema

`src/oscal/schema/oscal_poam.yaml` is the module titled "OSCAL Plan of Action and Milestones (POA&M) Model", with the id `https://w3id.org/lmodel/oscal/oscal_poam`.[^oscal_poam.yaml] Its `version` is `1.2.3`, its license Apache-2.0, and its `source` is NIST's JSON schema of the model, `http://csrc.nist.gov/ns/oscal/1.2.3/oscal-poam-schema.json`. It imports `linkml:types`, the [catalog module](oscal-catalog-schema.md) and the [assessment plan module](oscal-assessment-plan-schema.md). Its `see_also` names NIST's page on the POA&M, <https://pages.nist.gov/OSCAL/learn/concepts/layer/assessment/poam/>.

The README describes the model as the risks a system still carries and how they are tracked.[^readme.md] `PlanOfActionAndMilestones` is "A plan of action and milestones that identifies initial and residual risks, deviations, and disposition". It requires `uuid`, `metadata` and `poam-items`, and also holds `import-ssp`, `system-id`, `local-definitions`, `observations`, `risks`, `findings` and `back-matter`. `PoamDocument` wraps one plan as the root of a POA&M document.

The module's one subset, `poam`, holds the root document and its containers: `PoamLocalDefinitions`, `PoamItem` and `RelatedFinding`. The observations, findings and risks it records are the assessment plan module's classes.

[^oscal_poam.yaml]: src/oscal/schema/oscal_poam.yaml, the header, the subset and the classes
[^readme.md]: README.md, the What it models section
