---
type: Reference
id: https://w3id.org/lmodel/oscal/knowledge/references/nist-oscal
title: NIST OSCAL
description: "NIST's Open Security Controls Assessment Language (OSCAL), the upstream standard this repository renders: release 1.2.3 (tag v1.2.3, commit e061961 of usnistgov/OSCAL), whose metaschema defines the catalog, profile, component definition, system security plan, assessment plan, assessment results, POA&M and mapping collection models, documented at pages.nist.gov/OSCAL."
resource: https://pages.nist.gov/OSCAL/
timestamp: "2026-08-05T00:00:00Z"
about: []
genre: reference
relatedTo:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/metaschema-copy
sources:
  - id: readme.md
    resource: README.md
    title: the What it models section
  - id: about.md
    resource: docs/about.md
    title: the opening paragraph and Reference
  - id: schema-oscal.yaml
    resource: src/oscal/schema/oscal.yaml
    title: the header's source, see_also and annotations
  - id: schema
    resource: src/oscal/schema
    title: the see_also addresses of the eight modules
  - id: metaschema-readme.md
    resource: src/oscal/schema/metaschema/readme.md
    title: NIST's description of a metaschema
  - id: notice
    resource: NOTICE
    title: the opening paragraphs
  - resource: CONTRIBUTING.md
    title: Reporting issues
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:53:56Z"
---

# NIST OSCAL

The Open Security Controls Assessment Language (OSCAL) is a language of the National Institute of Standards and Technology (NIST), as NOTICE names them.[^notice] `docs/about.md` calls it NIST's language for control catalogs, profiles, component definitions, system security plans, assessment plans and results, plans of action and milestones, and control mappings.[^about.md] The README links its pages at <https://pages.nist.gov/OSCAL/>, and says that the schema in this repository models OSCAL 1.2.3, one module for each of its models.[^readme.md]

## The release the schema renders

The umbrella schema's header gives its `version` as 1.2.3, its `source` as the `src/metaschema` folder of usnistgov/OSCAL at commit `e061961c7702afeabffdf5e59894d35e748dade1`, and that tag and commit in its `oscal_tag` and `oscal_commit` annotations.[^schema-oscal.yaml] Its `see_also` names the OSCAL-Reference pages of v1.2.3 and the release, <https://github.com/usnistgov/OSCAL/releases/tag/v1.2.3>. The [OSCAL metaschema copy](../datasets/metaschema-copy.md) holds that commit's metaschema sources. NIST's `readme.md` there says that an OSCAL metaschema defines the information structures of an OSCAL model in a format-neutral form, and that OSCAL's XML and JSON schemas and model documentation are generated from it.[^metaschema-readme.md]

## The layers

The modules' `see_also` addresses place each model in a layer of NIST's OSCAL concepts:[^schema]

- the control layer: the catalog and the profile;
- the implementation layer: the component definition and the system security plan;
- the assessment layer: the assessment plan, the assessment results and the POA&M;
- the mapping layer: the mapping collection.

CONTRIBUTING.md says that a problem in OSCAL itself belongs upstream, in usnistgov/OSCAL's issue tracker.

[^notice]: NOTICE, the paragraph on src/oscal/schema/*.yaml
[^about.md]: docs/about.md, the opening paragraph
[^readme.md]: README.md, the What it models section
[^schema-oscal.yaml]: src/oscal/schema/oscal.yaml, the header's version, source, see_also and annotations
[^metaschema-readme.md]: src/oscal/schema/metaschema/readme.md, the whole page
[^schema]: src/oscal/schema, the see_also addresses of the eight modules
