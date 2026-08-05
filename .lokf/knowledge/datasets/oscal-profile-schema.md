---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-profile-schema
title: OSCAL Profile Schema
description: LinkML schema for the OSCAL Profile model (v1.2.1). Profiles allow organizations to tailor a catalog by selecting and customizing controls.
version: "1.2.1"
resource: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_profile.yaml
license: https://www.apache.org/licenses/LICENSE-2.0
timestamp: "2026-08-05T00:00:00Z"
source:
  - http://csrc.nist.gov/ns/oscal/1.2.1/oscal-profile-schema.json
isPartOf:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-schema
derivedFrom:
  - https://w3id.org/lmodel/oscal/knowledge/references/nist-oscal
references:
  - https://w3id.org/lmodel/oscal/knowledge/references/linkml
distribution:
  - media_type: application/yaml
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_profile.yaml
---

# OSCAL Profile Schema

The **OSCAL Profile schema** (`src/oscal/schema/oscal_profile.yaml`) encodes the OSCAL Profile model: a mechanism for selecting and tailoring controls from one or more catalogs to produce a baseline (e.g. NIST SP 800-53 Low/Moderate/High).

**Upstream documentation:**
- <https://pages.nist.gov/OSCAL/learn/concepts/layer/control/profile/>
