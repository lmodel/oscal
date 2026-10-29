---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-assessment-results-schema
title: OSCAL Assessment Results Schema
description: "The assessment results module of the OSCAL schema, `src/oscal/schema/oscal_assessment_results.yaml` (id `https://w3id.org/lmodel/oscal/oscal_assessment_results`, OSCAL 1.2.3): the AssessmentResults model of what an assessment observed and found, with its results, attestations and assessment log, and AssessmentResultsDocument as its document root; it imports the catalog and assessment plan modules."
version: 1.2.3
resource: src/oscal/schema/oscal_assessment_results.yaml
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
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_assessment_results.yaml
genre: reference
dependsOn:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-catalog-schema
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-assessment-plan-schema
sources:
  - id: oscal_assessment_results.yaml
    resource: src/oscal/schema/oscal_assessment_results.yaml
    title: the header, the subset and AssessmentResults
  - id: readme.md
    resource: README.md
    title: the What it models section
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:53:56Z"
  revision: 7746495c7a27992c40ebd9cff16858020a82696e
---

# OSCAL Assessment Results Schema

`src/oscal/schema/oscal_assessment_results.yaml` is the module titled "OSCAL Assessment Results Model", with the id `https://w3id.org/lmodel/oscal/oscal_assessment_results`.[^oscal_assessment_results.yaml] Its `version` is `1.2.3`, its license Apache-2.0, and its `source` is NIST's JSON schema of the model, `http://csrc.nist.gov/ns/oscal/1.2.3/oscal-ar-schema.json`. It imports `linkml:types`, the [catalog module](oscal-catalog-schema.md) and the [assessment plan module](oscal-assessment-plan-schema.md). Its `see_also` names NIST's page on the assessment results, <https://pages.nist.gov/OSCAL/learn/concepts/layer/assessment/assessment-results/>.

The README describes the assessment plan and the assessment results together as what an assessment covers, and what it observed and found.[^readme.md] `AssessmentResults` is "Security assessment results, such as those provided by a FedRAMP assessor in a security assessment report". It requires `uuid`, `metadata`, `import-ap` and `results`, and also holds `local-definitions` and `back-matter`. `AssessmentResultsDocument` wraps one set of results as the root of an assessment results document.

The module's one subset, `assessment_results`, holds the root document and its containers: `ImportAssessmentPlan`, `AssessmentResultsLocalDefinitions`, `Result`, `ResultLocalDefinitions`, `Attestation`, `AssessmentLog` and `AssessmentLogEntry`. The observations, findings and risks a result records are the assessment plan module's classes.

[^oscal_assessment_results.yaml]: src/oscal/schema/oscal_assessment_results.yaml, the header, the subset and the classes
[^readme.md]: README.md, the What it models section
