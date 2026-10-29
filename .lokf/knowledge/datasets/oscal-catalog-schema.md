---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-catalog-schema
title: OSCAL Catalog Schema
description: "The catalog module of the OSCAL schema, `src/oscal/schema/oscal_catalog.yaml` (id `https://w3id.org/lmodel/oscal/oscal_catalog`, OSCAL 1.2.3): the Catalog model of controls, groups, parameters and parts, the metadata, back matter, shared types and mixins every other module imports, and OscalDocument, the schema's tree root."
version: 1.2.3
resource: src/oscal/schema/oscal_catalog.yaml
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
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_catalog.yaml
genre: reference
sources:
  - id: oscal_catalog.yaml
    resource: src/oscal/schema/oscal_catalog.yaml
    title: the header, the subsets, the types and the Catalog classes
  - id: readme.md
    resource: README.md
    title: the What it models section
  - id: changelog.md
    resource: CHANGELOG.md
    title: the Changed items
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:53:56Z"
  revision: 57a6e461e82c2896a6fceb786029f75b32ec8668
---

# OSCAL Catalog Schema

`src/oscal/schema/oscal_catalog.yaml` is the module titled "OSCAL Control Catalog Model", with the id `https://w3id.org/lmodel/oscal/oscal_catalog`.[^oscal_catalog.yaml] Its `version` is `1.2.3`, its license Apache-2.0, and its `source` is NIST's JSON schema of the model, `http://csrc.nist.gov/ns/oscal/1.2.3/oscal-catalog-schema.json`. It imports only `linkml:types`, and every other module imports it. Its comments say that the core stays open, with no assumptions about a regime such as FedRAMP. Its `see_also` names NIST's page on the catalog, <https://pages.nist.gov/OSCAL/learn/concepts/layer/control/catalog/>.

The README describes the catalog model as controls, their groups, parameters and parts.[^readme.md] `Catalog` is "A structured, organized collection of control information". It requires `uuid` and `metadata`, and also holds `params`, `controls`, `groups` and `back-matter`. `CatalogDocument` wraps one catalog as the root of a catalog document. It is a kind of `OscalDocument`, the schema's tree root, which is "A root wrapper for an OSCAL document, which may be of any OSCAL document type".

## What else the module holds

The README says that every model shares OSCAL's metadata and back matter, which this module defines. The module's four subsets say what it holds:

- `oscal_catalog`: the root catalog document, groups and controls;
- `oscal_metadata`: document metadata, parties, roles, locations, and utility types such as `Property`, `Link` and `Hash`;
- `oscal_back_matter`: the back matter and the resources in it;
- `oscal_control_common`: parts, parameters, constraints, guidelines, selections and control-matching helpers.

It also defines the schema's shared types, such as `UUIDType`, `URIType`, `DateTimeWithTimezoneType`, `MarkupLineType` and `TokenType`, and the mixins `HasPropsAndLinks`, `OscalCommon`, `HasResponsibleRoles` and `HasResponsibleParties`. Its slot `class_` renders OSCAL's `class` key, because a slot named `class` makes the generated dataclasses invalid Python. CHANGELOG.md says that the OSCAL 1.2.3 values joined the enums of control status, location type and data-center class, among others, and that a control's status now admits other values.[^changelog.md]

[^oscal_catalog.yaml]: src/oscal/schema/oscal_catalog.yaml, the header, the subsets, the types, the mixins, the class_ slot and the Catalog, CatalogDocument and OscalDocument classes
[^readme.md]: README.md, the What it models section
[^changelog.md]: CHANGELOG.md, the Changed items of the Unreleased section
