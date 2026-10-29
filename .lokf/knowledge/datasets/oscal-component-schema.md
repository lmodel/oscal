---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-component-schema
title: OSCAL Component Definition Schema
description: "The component definition module of the OSCAL schema, `src/oscal/schema/oscal_component.yaml` (id `https://w3id.org/lmodel/oscal/oscal_component`, OSCAL 1.2.3): the ComponentDefinition model of components, their capabilities and the controls each implements, with ComponentDefinitionDocument as its document root, against which the CNCF and Luigi Carpio fixtures are validated; it imports the catalog and assessment plan modules."
version: 1.2.3
resource: src/oscal/schema/oscal_component.yaml
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
    access_url: https://github.com/lmodel/oscal/blob/main/src/oscal/schema/oscal_component.yaml
genre: reference
dependsOn:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-catalog-schema
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-assessment-plan-schema
sources:
  - id: oscal_component.yaml
    resource: src/oscal/schema/oscal_component.yaml
    title: the header, the subset and ComponentDefinition
  - id: readme.md
    resource: README.md
    title: the What it models section
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:53:56Z"
  revision: 7746495c7a27992c40ebd9cff16858020a82696e
---

# OSCAL Component Definition Schema

`src/oscal/schema/oscal_component.yaml` is the module titled "OSCAL Component Definition Model", with the id `https://w3id.org/lmodel/oscal/oscal_component`.[^oscal_component.yaml] Its `version` is `1.2.3`, its license Apache-2.0, and its `source` is NIST's JSON schema of the model, `http://csrc.nist.gov/ns/oscal/1.2.3/oscal-component-definition-schema.json`. It imports `linkml:types`, the [catalog module](oscal-catalog-schema.md) and the [assessment plan module](oscal-assessment-plan-schema.md). Its `see_also` names NIST's page on the component definition, <https://pages.nist.gov/OSCAL/learn/concepts/layer/implementation/component-definition/>.

The README describes the model as components and the controls each implements.[^readme.md] `ComponentDefinition` is "A collection of component descriptions, which may optionally be grouped by capability". It requires `uuid` and `metadata`, and also holds `import-component-definitions`, `components`, `capabilities` and `back-matter`. `ComponentDefinitionDocument` wraps one component definition as the root of a component definition document.

The module's one subset, `component_definition`, holds the root document and its containers: `ImportComponentDefinition`, `DefinedComponent`, `Capability`, `IncorporatesComponent`, `ControlImplementationSet`, `ImplementedRequirement` and `ImplementedControlStatement`. The two third-party fixture sets, [CNCF AI Ecosystem OSCAL Benchmarks](cncf-ai-benchmarks.md) and [NIST 800-53 Rev 5 to AWS Service Mapping (Luigi Carpio)](luigi-carpio-component-definition.md), are component definitions checked against this module.

[^oscal_component.yaml]: src/oscal/schema/oscal_component.yaml, the header, the subset and the classes
[^readme.md]: README.md, the What it models section
