---
type: Dataset
id: https://github.com/lmodel/oscal/knowledge/datasets/oscal-component-schema
title: OSCAL Component Definition Schema
description: LinkML schema for the OSCAL Component Definition model (v1.2.1). Encodes reusable definitions of system components and their control implementations.
version: "1.2.1"
resource: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_component.yaml
license: https://www.apache.org/licenses/LICENSE-2.0
timestamp: "2026-08-05T00:00:00Z"
source:
  - http://csrc.nist.gov/ns/oscal/1.2.1/oscal-component-definition-schema.json
isPartOf:
  - https://github.com/lmodel/oscal/knowledge/datasets/oscal-schema
derivedFrom:
  - https://github.com/lmodel/oscal/knowledge/references/nist-oscal
references:
  - https://github.com/lmodel/oscal/knowledge/references/linkml
distribution:
  - media_type: application/yaml
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_component.yaml
---

# OSCAL Component Definition Schema

The **OSCAL Component Definition schema** (`src/oscal/schema/oscal_component.yaml`) encodes the OSCAL Component Definition model: a document that describes reusable system components (hardware, software, services, policies) and the security controls they implement or support.

**Upstream documentation:**
- <https://pages.nist.gov/OSCAL/learn/concepts/layer/implementation/component-definition/>
