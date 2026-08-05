---
type: Dataset
id: https://github.com/lmodel/oscal/knowledge/datasets/oscal-ssp-schema
title: OSCAL System Security Plan Schema
description: LinkML schema for the OSCAL System Security Plan (SSP) model (v1.2.1). Encodes how an organization implements security controls in their information system.
version: "1.2.1"
resource: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_ssp.yaml
license: https://www.apache.org/licenses/LICENSE-2.0
timestamp: "2026-08-05T00:00:00Z"
source:
  - http://csrc.nist.gov/ns/oscal/1.2.1/oscal-ssp-schema.json
isPartOf:
  - https://github.com/lmodel/oscal/knowledge/datasets/oscal-schema
derivedFrom:
  - https://github.com/lmodel/oscal/knowledge/references/nist-oscal
references:
  - https://github.com/lmodel/oscal/knowledge/references/linkml
distribution:
  - media_type: application/yaml
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_ssp.yaml
---

# OSCAL System Security Plan Schema

The **OSCAL SSP schema** (`src/oscal/schema/oscal_ssp.yaml`) encodes the OSCAL System Security Plan model: the Implementation layer document describing how an organization implements a profile's security controls in a specific information system. It imports `oscal_assessment_plan`, `oscal_catalog`, and other modules.

**Upstream documentation:**
- <https://pages.nist.gov/OSCAL/learn/concepts/layer/implementation/ssp/>
