---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-assessment-plan-schema
title: OSCAL Assessment Plan Schema
description: "The assessment plan module of the OSCAL schema, `src/oscal/schema/oscal_assessment_plan.yaml` (id `https://w3id.org/lmodel/oscal/oscal_assessment_plan`, OSCAL 1.2.3): the AssessmentPlan model of what an assessment covers, and the assessment-common and implementation-common classes (subjects, tasks, observations, findings, risks, system components) that the component, SSP, assessment results and POA&M modules import."
version: 1.2.3
resource: src/oscal/schema/oscal_assessment_plan.yaml
license: https://www.apache.org/licenses/LICENSE-2.0
timestamp: "2026-08-05T00:00:00Z"
isPartOf:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-schema
derivedFrom:
  - https://w3id.org/lmodel/oscal/knowledge/references/nist-oscal
  - https://w3id.org/lmodel/oscal/knowledge/datasets/metaschema-copy
references:
  - https://w3id.org/lmodel/oscal/knowledge/references/linkml
distribution:
  - media_type: application/yaml
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_assessment_plan.yaml
genre: reference
source:
  - https://github.com/usnistgov/OSCAL/tree/e061961c7702afeabffdf5e59894d35e748dade1/src/metaschema
dependsOn:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-catalog-schema
sources:
  - id: oscal_assessment_plan.yaml
    resource: src/oscal/schema/oscal_assessment_plan.yaml
    title: the header, the three subsets, the types and AssessmentPlan
  - id: readme.md
    resource: README.md
    title: the What it models section
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:53:56Z"
  revision: 57a6e461e82c2896a6fceb786029f75b32ec8668
---

# OSCAL Assessment Plan Schema

`src/oscal/schema/oscal_assessment_plan.yaml` is the module titled "OSCAL Assessment Plan Model", with the id `https://w3id.org/lmodel/oscal/oscal_assessment_plan`.[^oscal_assessment_plan.yaml] Its `version` is `1.2.3`, its license Apache-2.0, and its `source` is NIST's JSON schema of the model, `http://csrc.nist.gov/ns/oscal/1.2.3/oscal-ap-schema.json`. It imports `linkml:types` and the [catalog module](oscal-catalog-schema.md). Its `see_also` names NIST's page on the assessment plan, <https://pages.nist.gov/OSCAL/learn/concepts/layer/assessment/assessment-plan/>.

The README describes the assessment plan and the assessment results together as what an assessment covers, and what it observed and found.[^readme.md] `AssessmentPlan` is "An assessment plan, such as those provided by a FedRAMP assessor". It requires `uuid`, `metadata`, `import-ssp` and `reviewed-controls`, and also holds `local-definitions`, `terms-and-conditions`, `assessment-subjects`, `assessment-assets`, `tasks` and `back-matter`. `AssessmentPlanDocument` wraps one plan as the root of an assessment plan document.

## The classes other modules share

The module defines three subsets:

- `assessment_plan`: the root document and its direct containers, local definitions and terms and conditions;
- `assessment_common`: the classes of OSCAL's assessment-common namespace, such as subjects, assets, activities, tasks, findings, observations and risks;
- `implementation_common`: the classes of OSCAL's implementation-common namespace, such as system components, protocols, inventory items, users and set-parameter.

So the component definition, system security plan, assessment results and POA&M modules import this module beside the catalog module. It also defines the types `NonNegativeIntegerType` and `PositiveIntegerType`.

[^oscal_assessment_plan.yaml]: src/oscal/schema/oscal_assessment_plan.yaml, the header, the subsets, the types, AssessmentPlan and AssessmentPlanDocument
[^readme.md]: README.md, the What it models section
