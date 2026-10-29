---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-ssp-schema
title: OSCAL System Security Plan Schema
description: "The system security plan module of the OSCAL schema, `src/oscal/schema/oscal_ssp.yaml` (id `https://w3id.org/lmodel/oscal/oscal_ssp`, OSCAL 1.2.3): the SystemSecurityPlan model of a system's characteristics, its implementation and how it implements a profile's controls, with SspDocument as its document root; it imports the catalog and assessment plan modules."
version: 1.2.3
resource: src/oscal/schema/oscal_ssp.yaml
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
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_ssp.yaml
genre: reference
dependsOn:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-catalog-schema
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-assessment-plan-schema
sources:
  - id: oscal_ssp.yaml
    resource: src/oscal/schema/oscal_ssp.yaml
    title: the header, the subset, SystemSecurityPlan and SystemCharacteristics
  - id: readme.md
    resource: README.md
    title: the What it models section
  - id: changelog.md
    resource: CHANGELOG.md
    title: the Fixed item
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:53:56Z"
  revision: 7746495c7a27992c40ebd9cff16858020a82696e
---

# OSCAL System Security Plan Schema

`src/oscal/schema/oscal_ssp.yaml` is the module titled "OSCAL System Security Plan (SSP) Model", with the id `https://w3id.org/lmodel/oscal/oscal_ssp`.[^oscal_ssp.yaml] Its `version` is `1.2.3`, its license Apache-2.0, and its `source` is NIST's JSON schema of the model, `http://csrc.nist.gov/ns/oscal/1.2.3/oscal-ssp-schema.json`. It imports `linkml:types`, the [catalog module](oscal-catalog-schema.md) and the [assessment plan module](oscal-assessment-plan-schema.md). Its `see_also` names NIST's page on the system security plan, <https://pages.nist.gov/OSCAL/learn/concepts/layer/implementation/ssp/>.

The README describes the model as a system's characteristics, its implementation and how it implements a profile's controls.[^readme.md] `SystemSecurityPlan` is "A system security plan, such as those described in NIST SP 800-18". It requires `uuid`, `metadata`, `import-profile`, `system-characteristics`, `system-implementation` and `control-implementation`, and also holds `back-matter`. `SspDocument` wraps one plan as the root of a system security plan document.

`SystemCharacteristics` requires `system-ids`, `system-name`, `description`, `system-information`, `system-status` and `authorization-boundary`. CHANGELOG.md says that it now takes `props` and `links`, as OSCAL defines them.[^changelog.md] The module's one subset, `ssp`, holds the root document and its SSP-specific containers, such as `SystemInformation`, `SystemImplementation`, `LeveragedAuthorization`, `SspControlImplementation` and `ByComponent`.

[^oscal_ssp.yaml]: src/oscal/schema/oscal_ssp.yaml, the header, the subset, SystemSecurityPlan, SspDocument and SystemCharacteristics
[^readme.md]: README.md, the What it models section
[^changelog.md]: CHANGELOG.md, the Fixed item of the Unreleased section
