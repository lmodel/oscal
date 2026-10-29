---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-profile-schema
title: OSCAL Profile Schema
description: "The profile module of the OSCAL schema, `src/oscal/schema/oscal_profile.yaml` (id `https://w3id.org/lmodel/oscal/oscal_profile`, OSCAL 1.2.3): the Profile model, a selection of controls from catalogs or profiles and how it merges and modifies them, with ProfileDocument as its document root; it imports the catalog module."
version: 1.2.3
resource: src/oscal/schema/oscal_profile.yaml
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
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_profile.yaml
genre: reference
dependsOn:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-catalog-schema
sources:
  - id: oscal_profile.yaml
    resource: src/oscal/schema/oscal_profile.yaml
    title: the header, the subset and the Profile classes
  - id: readme.md
    resource: README.md
    title: the What it models section
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:53:56Z"
  revision: 57a6e461e82c2896a6fceb786029f75b32ec8668
---

# OSCAL Profile Schema

`src/oscal/schema/oscal_profile.yaml` is the module titled "OSCAL Profile Model", with the id `https://w3id.org/lmodel/oscal/oscal_profile`.[^oscal_profile.yaml] Its `version` is `1.2.3`, its license Apache-2.0, and its `source` is NIST's JSON schema of the model, `http://csrc.nist.gov/ns/oscal/1.2.3/oscal-profile-schema.json`. It imports `linkml:types` and the [catalog module](oscal-catalog-schema.md). Its `see_also` names NIST's page on the profile, <https://pages.nist.gov/OSCAL/learn/concepts/layer/control/profile/>.

The README describes the profile model as a selection of controls from catalogs, and how it alters them.[^readme.md] `Profile` is "An OSCAL Profile that designates a set of controls from one or more catalogs or profiles, optionally restructures and modifies them, to describe a basis for a security standard or body of practice". It requires `uuid`, `metadata` and `imports`, and also holds `merge`, `modify` and `back-matter`. `ProfileDocument` wraps one profile as the root of a profile document.

The module's one subset, `profile`, holds the root document and its profile-specific containers: `ProfileImport`, the merge classes `ProfileMerge`, `CombinationRule`, `MergeFlat` and `MergeCustom`, and the modification classes `ProfileModify`, `ParameterSetting`, `Alteration`, `Removal` and `Addition`, among others.

[^oscal_profile.yaml]: src/oscal/schema/oscal_profile.yaml, the header, the subset and the classes
[^readme.md]: README.md, the What it models section
