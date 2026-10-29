---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-mapping-schema
title: OSCAL Mapping Collection Schema
description: "The mapping collection module of the OSCAL schema, `src/oscal/schema/oscal_mapping.yaml` (id `https://w3id.org/lmodel/oscal/oscal_mapping`, OSCAL 1.2.3): the MappingCollection model of how the controls of one catalog or profile relate to another's, with its provenance, maps, qualifiers, gap summaries, confidence scores and coverage, and MappingCollectionDocument as its document root; it imports the catalog module."
version: 1.2.3
resource: src/oscal/schema/oscal_mapping.yaml
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
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_mapping.yaml
genre: reference
source:
  - https://github.com/usnistgov/OSCAL/tree/e061961c7702afeabffdf5e59894d35e748dade1/src/metaschema
dependsOn:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-catalog-schema
sources:
  - id: oscal_mapping.yaml
    resource: src/oscal/schema/oscal_mapping.yaml
    title: the header, the subset and MappingCollection
  - id: readme.md
    resource: README.md
    title: the What it models section
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:53:56Z"
  revision: 7746495c7a27992c40ebd9cff16858020a82696e
---

# OSCAL Mapping Collection Schema

`src/oscal/schema/oscal_mapping.yaml` is the module titled "OSCAL Mapping Collection Model", with the id `https://w3id.org/lmodel/oscal/oscal_mapping`.[^oscal_mapping.yaml] Its `version` is `1.2.3`, its license Apache-2.0, and its `source` is NIST's JSON schema of the model, `http://csrc.nist.gov/ns/oscal/1.2.3/oscal-mapping-schema.json`. It imports `linkml:types` and the [catalog module](oscal-catalog-schema.md). Its `see_also` names NIST's OSCAL pages and its page on the mapping layer, <https://pages.nist.gov/OSCAL/learn/concepts/layer/mapping/>.

The README describes the model as how the controls of one catalog relate to another's.[^readme.md] `MappingCollection` is "A collection of control mappings between source and target resources". It requires `uuid`, `metadata`, `provenance` and `mappings`, and also holds `back-matter`. `MappingCollectionDocument` wraps one collection as the root of a mapping collection document.

The module's one subset, `mapping_collection`, holds the root document and its containers: `MappingProvenance`, `Mapping`, `Map`, `MappingItem`, `MappingResourceReference`, `QualifierItem`, `GapSummary`, `ConfidenceScore` and `Coverage`. Its enums include `RelationshipEnum`, `MappingMethodEnum` and `MappingStatusEnum`.

[^oscal_mapping.yaml]: src/oscal/schema/oscal_mapping.yaml, the header, the subset, the classes and the enums
[^readme.md]: README.md, the What it models section
