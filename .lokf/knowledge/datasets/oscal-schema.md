---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-schema
title: OSCAL Schema (top-level)
description: "The umbrella LinkML schema of OSCAL 1.2.3, `src/oscal/schema/oscal.yaml` (schema id `https://w3id.org/lmodel/oscal`, prefix `oscal:`): it imports the eight model modules, pins OSCAL's tag v1.2.3 and commit e061961 in its annotations, and its `lokf adapt` copy `.lokf/oscal.yaml`, rooted on the eight models, is this bundle's domain schema."
version: 1.2.3
resource: src/oscal/schema/oscal.yaml
license: https://www.apache.org/licenses/LICENSE-2.0
timestamp: "2026-08-05T00:00:00Z"
derivedFrom:
  - https://w3id.org/lmodel/oscal/knowledge/references/nist-oscal
  - https://w3id.org/lmodel/oscal/knowledge/datasets/metaschema-copy
references:
  - https://w3id.org/lmodel/oscal/knowledge/references/linkml
hasPart:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-catalog-schema
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-profile-schema
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-ssp-schema
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-assessment-plan-schema
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-assessment-results-schema
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-component-schema
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-mapping-schema
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-poam-schema
distribution:
  - media_type: application/yaml
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal.yaml
genre: reference
source:
  - https://github.com/usnistgov/OSCAL/tree/e061961c7702afeabffdf5e59894d35e748dade1/src/metaschema
sources:
  - id: schema-oscal.yaml
    resource: src/oscal/schema/oscal.yaml
    title: the header, the comment and the imports
  - id: config.public.mk
    resource: config.public.mk
    title: LINKML_SCHEMA_NAME and LINKML_SCHEMA_SOURCE_DIR
  - id: readme.md
    resource: README.md
    title: the What it models and Knowledge Trust Ladder (KTL) sections
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: test_modules_share_the_oscal_namespace
  - id: changelog.md
    resource: CHANGELOG.md
    title: the Unreleased section
  - id: lokf-justfile
    resource: .lokf/justfile
    title: the schema line
  - id: project.justfile
    resource: project.justfile
    title: the knowledge bundle recipes and their roots
  - id: lokf-oscal.yaml
    resource: .lokf/oscal.yaml
    title: the header and the last note
  - resource: src/oscal/schema/README.md
    title: the list of modules
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:53:56Z"
  revision: 9682284a2e351227aebe66a0fe34180d933ad8f8
---

# OSCAL Schema (top-level)

`src/oscal/schema/oscal.yaml` is the umbrella schema, titled "Open Security Controls Assessment Language (OSCAL)".[^schema-oscal.yaml] Its description calls it a LinkML model of NIST's OSCAL 1.2.3, with each of the eight models in a module of its own. Its `version` is `1.2.3`, the OSCAL release it renders, and its `source` is the `src/metaschema` folder of usnistgov/OSCAL at commit `e061961c7702afeabffdf5e59894d35e748dade1`. The annotations `oscal_tag` and `oscal_commit` pin the tag `v1.2.3` and the same commit. A comment says that `scripts/check_upstream_release.py` reads the same pins and reports when NIST tags a newer release or the copy drifts, and that the release tags are the schema's own versions.

The schema declares the license Apache-2.0 and binds the prefix `oscal:` to `https://w3id.org/lmodel/oscal/`, its default prefix. Its `see_also` names the documentation site, NIST's OSCAL pages, the OSCAL-Reference pages of v1.2.3 and the v1.2.3 release. Its notes repeat OSCAL's rule that a changed OSCAL file gets a new document UUID and a new `last-modified` time.

## Modules

`config.public.mk` names `oscal` as `LINKML_SCHEMA_NAME` and `src/oscal/schema` as its folder, so the `just` recipes generate from the umbrella.[^config.public.mk] The umbrella imports `linkml:types` and one module for each OSCAL model, and defines no class, slot or enum of its own:

- [OSCAL Catalog Schema](oscal-catalog-schema.md), `oscal_catalog.yaml`;
- [OSCAL Profile Schema](oscal-profile-schema.md), `oscal_profile.yaml`;
- [OSCAL System Security Plan Schema](oscal-ssp-schema.md), `oscal_ssp.yaml`;
- [OSCAL Assessment Plan Schema](oscal-assessment-plan-schema.md), `oscal_assessment_plan.yaml`;
- [OSCAL Assessment Results Schema](oscal-assessment-results-schema.md), `oscal_assessment_results.yaml`;
- [OSCAL Component Definition Schema](oscal-component-schema.md), `oscal_component.yaml`;
- [OSCAL Mapping Collection Schema](oscal-mapping-schema.md), `oscal_mapping.yaml`;
- [OSCAL POA&M Schema](oscal-poam-schema.md), `oscal_poam.yaml`.

The README says that every model shares OSCAL's metadata and back matter, which the catalog module defines.[^readme.md] Every module's `id` is `https://w3id.org/lmodel/oscal/` followed by its name, and every module's default prefix is `oscal:`, which `tests/test_schema_rules.py` checks.[^test_schema_rules.py] CHANGELOG.md says that this replaced a namespace per module, such as `https://w3id.org/lmodel/oscal_catalog/`, that no w3id route serves.[^changelog.md]

## Enums and the metaschema

CHANGELOG.md says that each of the schema's 155 enums names the allowed-values lists it renders, and that a test holds it to them. Each enum carries the names of those lists in its `oscal_allowed_values` annotation, and an enum that admits other values carries `allow_any: true`. The lists are defined in the [OSCAL metaschema copy](metaschema-copy.md), and [Test data and schema tests](test-data.md) says how the tests hold the enums to them.

## What the models record

The README lists the eight models and their classes:

- **Catalog** (`Catalog`): controls, their groups, parameters and parts.
- **Profile** (`Profile`): a selection of controls from catalogs, and how it alters them.
- **Component definition** (`ComponentDefinition`): components and the controls each implements.
- **System security plan** (`SystemSecurityPlan`): a system's characteristics, its implementation and how it implements a profile's controls.
- **Assessment plan** (`AssessmentPlan`) and **assessment results** (`AssessmentResults`): what an assessment covers, and what it observed and found.
- **Plan of action and milestones** (`PlanOfActionAndMilestones`): the risks a system still carries and how they are tracked.
- **Mapping collection** (`MappingCollection`): how the controls of one catalog relate to another's.

[Scope, influences and mappings](../explanations/scope-and-influences.md) says what the schema leaves out.

## As the bundle's domain schema

The README says that this bundle's domain schema is `.lokf/oscal.yaml`, which `lokf adapt` writes from `src/oscal/schema/oscal.yaml`, and that the source is edited, never the copy. `just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` says when it is stale. The `schema :=` line of `.lokf/justfile` names `oscal.yaml`, so `just lokf-validate` and `just lokf-check-refs` pass the copy to the validator.[^lokf-justfile]

`project.justfile` passes eight roots to `lokf adapt`: `Catalog`, `Profile`, `ComponentDefinition`, `SystemSecurityPlan`, `AssessmentPlan`, `AssessmentResults`, `PlanOfActionAndMilestones` and `MappingCollection`.[^project.justfile] Its comment says that these are the classes a knowledge concept may use as its `type`, and that OSCAL gives none of them an identifier slot, so each keeps its required `uuid` and `metadata`, and a concept's `id` names it beside them. The recipes run the `lokf` that the sidecar's floor pins, 0.9.0 or later, unless `LOKF_CMD` names another. The copy's header says that it was generated from `oscal.yaml` (oscal 1.2.3), with the id `https://w3id.org/lmodel/oscal-lokf`, and its last note lists the eight classes it re-rooted on `lokf:Concept` and the names it changed.[^lokf-oscal.yaml] [Element names and the shared namespace](../explanations/element-names.md) explains those renames.

The README lists the eight classes for Obsidian users to add to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins. It also says that a release carries the copy as `schema-<tag>-oscal.yaml`, on the terms CONTRIBUTING.md gives: see [Knowledge Release](../workflows/knowledge-release.md). [Generated artefacts](generated-artefacts.md) lists what the generators write from these files.

[^schema-oscal.yaml]: src/oscal/schema/oscal.yaml, the header, the comment and the imports
[^config.public.mk]: config.public.mk, LINKML_SCHEMA_NAME and LINKML_SCHEMA_SOURCE_DIR
[^readme.md]: README.md, the What it models and Knowledge Trust Ladder (KTL) sections
[^test_schema_rules.py]: tests/test_schema_rules.py, test_modules_share_the_oscal_namespace
[^changelog.md]: CHANGELOG.md, the Added and Changed items of the Unreleased section
[^lokf-justfile]: .lokf/justfile, the schema line
[^project.justfile]: project.justfile, the comment above lokf_cmd and the lokf_adapt_roots line
[^lokf-oscal.yaml]: .lokf/oscal.yaml, the header and the last note
