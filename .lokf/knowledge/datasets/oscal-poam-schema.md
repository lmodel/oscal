---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-poam-schema
title: OSCAL POA&M Schema
description: LinkML schema for the OSCAL Plan of Action and Milestones (POA&M) model (v1.2.1). Encodes the tracking of identified risks and remediation activities.
version: "1.2.1"
resource: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_poam.yaml
license: https://www.apache.org/licenses/LICENSE-2.0
timestamp: "2026-08-05T00:00:00Z"
source:
  - http://csrc.nist.gov/ns/oscal/1.2.1/oscal-poam-schema.json
isPartOf:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-schema
derivedFrom:
  - https://w3id.org/lmodel/oscal/knowledge/references/nist-oscal
references:
  - https://w3id.org/lmodel/oscal/knowledge/references/linkml
distribution:
  - media_type: application/yaml
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_poam.yaml
---

# OSCAL POA&M Schema

The **OSCAL POA&M schema** (`src/oscal/schema/oscal_poam.yaml`) encodes the OSCAL Plan of Action and Milestones (POA&M) model: a document that tracks identified risks, weaknesses, and deficiencies in a system along with milestones for remediation.

**Upstream documentation:**
- <https://pages.nist.gov/OSCAL/learn/concepts/layer/assessment/poam/>
