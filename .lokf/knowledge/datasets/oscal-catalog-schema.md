---
type: Dataset
id: https://github.com/lmodel/oscal/knowledge/datasets/oscal-catalog-schema
title: OSCAL Catalog Schema
description: LinkML schema for the OSCAL Control Catalog model (v1.2.1). Encodes the structure of security and privacy control catalogs such as NIST SP 800-53.
version: "1.2.1"
resource: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_catalog.yaml
license: https://www.apache.org/licenses/LICENSE-2.0
timestamp: "2026-08-05T00:00:00Z"
source:
  - http://csrc.nist.gov/ns/oscal/1.2.1/oscal-catalog-schema.json
isPartOf:
  - https://github.com/lmodel/oscal/knowledge/datasets/oscal-schema
derivedFrom:
  - https://github.com/lmodel/oscal/knowledge/references/nist-oscal
references:
  - https://github.com/lmodel/oscal/knowledge/references/linkml
distribution:
  - media_type: application/yaml
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_catalog.yaml
---

# OSCAL Catalog Schema

The **OSCAL Catalog schema** (`src/oscal/schema/oscal_catalog.yaml`) encodes the OSCAL Control Catalog model: the layer of OSCAL that represents authoritative collections of security and privacy controls (e.g. NIST SP 800-53 Rev. 5).

**Key design notes (from schema comments):**
- Core stays open - no regime-specific assumptions (no FedRAMP hard-coding).
- NIST JSON Schema source: `http://csrc.nist.gov/ns/oscal/1.2.1/oscal-catalog-schema.json`.

**Upstream documentation:**
- <https://pages.nist.gov/OSCAL/learn/concepts/layer/control/catalog/>
- <https://pages.nist.gov/OSCAL-Reference/models/v1.2.1/catalog/json-reference/>
