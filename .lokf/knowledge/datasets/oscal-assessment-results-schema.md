---
type: Dataset
id: https://github.com/lmodel/oscal/knowledge/datasets/oscal-assessment-results-schema
title: OSCAL Assessment Results Schema
description: LinkML schema for the OSCAL Assessment Results (AR) model (v1.2.1). Encodes the findings and results from security control assessments.
version: "1.2.1"
resource: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_assessment_results.yaml
license: https://www.apache.org/licenses/LICENSE-2.0
timestamp: "2026-08-05T00:00:00Z"
source:
  - http://csrc.nist.gov/ns/oscal/1.2.1/oscal-ar-schema.json
isPartOf:
  - https://github.com/lmodel/oscal/knowledge/datasets/oscal-schema
derivedFrom:
  - https://github.com/lmodel/oscal/knowledge/references/nist-oscal
references:
  - https://github.com/lmodel/oscal/knowledge/references/linkml
distribution:
  - media_type: application/yaml
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_assessment_results.yaml
---

# OSCAL Assessment Results Schema

The **OSCAL Assessment Results schema** (`src/oscal/schema/oscal_assessment_results.yaml`) encodes the OSCAL AR model: records the findings of a completed security assessment against an Assessment Plan.

**Upstream documentation:**
- <https://pages.nist.gov/OSCAL/learn/concepts/layer/assessment/assessment-results/>
