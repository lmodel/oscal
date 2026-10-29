---
type: Explanation
id: https://w3id.org/lmodel/oscal/knowledge/explanations/scope-and-influences
genre: explanation
title: Scope, influences and mappings
description: "What the OSCAL schema renders and leaves out, and why: OSCAL 1.2.3's eight models as NIST's metaschema defines them, no influence beyond OSCAL apart from lmodel/slsa's module layout, release asset and governance files, no mapping yet to another vocabulary, and the metaschema constraints it does not check (index, index-has-key, is-unique, expect and has-cardinality)."
resource: README.md
about:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-schema
references:
  - https://w3id.org/lmodel/oscal/knowledge/references/nist-oscal
sources:
  - id: readme.md
    resource: README.md
    title: What it models, Influences, Mappings and Not modelled here
  - id: about.md
    resource: docs/about.md
    title: the opening paragraph
  - id: notice
    resource: NOTICE
    title: the opening paragraphs
  - resource: CONTRIBUTING.md
    title: What this project is
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:47:10Z"
  revision: 14c6e01c0283873b99f920c6289943bb78743b89
status: draft
---

# Scope, influences and mappings

## What the schema renders

The README says that the schema models NIST's Open Security Controls Assessment Language (OSCAL) 1.2.3, with one module for each of its models: catalog, profile, component definition, system security plan, assessment plan, assessment results, plan of action and milestones, and mapping collection.[^readme.md] `docs/about.md` says that every element renders a definition of OSCAL's metaschema at the v1.2.3 release.[^about.md] CONTRIBUTING.md says that the schema lets LinkML's tools validate OSCAL documents, and lets a knowledge bundle type its concepts with OSCAL's models.

NOTICE says that `src/oscal/schema/*.yaml`, `src/oscal/datamodel/` and `project/` are this project's rendering of OSCAL 1.2.3 as a LinkML schema, with NIST as the source of the definitions. They are not NIST's, and their use does not imply endorsement by NIST.[^notice] The README adds that this is not an official NIST project.

## Influences

The README names none beyond OSCAL itself, because the schema renders one specification. Its module layout, its release asset and its governance files follow lmodel/slsa.

## Mappings

The README says that there are none yet: no element names a term of another vocabulary.

## Not modelled

The README says that OSCAL's metaschema states constraints that the schema does not check:

- the keys that an `index`, `index-has-key` or `is-unique` constraint names;
- `expect` tests;
- `has-cardinality` counts.

So an OSCAL document that passes the schema can still fail NIST's own validators on these. [Validate OSCAL data against the schema](../playbooks/validate-data.md) says what each check in this repository covers.

[^readme.md]: README.md, the What it models, Influences, Mappings, Not modelled here and License sections
[^about.md]: docs/about.md, the opening paragraph
[^notice]: NOTICE, the paragraph on src/oscal/schema/*.yaml
