---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-mapping-schema
title: OSCAL Mapping Collection Schema
description: LinkML schema for the OSCAL Mapping Collection model (v1.2.1). Encodes relationships between controls in different catalogs or profiles.
version: "1.2.1"
resource: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_mapping.yaml
license: https://www.apache.org/licenses/LICENSE-2.0
timestamp: "2026-08-05T00:00:00Z"
isPartOf:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-schema
derivedFrom:
  - https://w3id.org/lmodel/oscal/knowledge/references/nist-oscal
references:
  - https://w3id.org/lmodel/oscal/knowledge/references/linkml
distribution:
  - media_type: application/yaml
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_mapping.yaml
---

# OSCAL Mapping Collection Schema

The **OSCAL Mapping Collection schema** (`src/oscal/schema/oscal_mapping.yaml`) encodes the OSCAL Mapping model: a document that describes equivalences, subsets, or other relationships between controls in different catalogs or profiles.

**Upstream documentation:**
- <https://pages.nist.gov/OSCAL/learn/concepts/layer/mapping/>
