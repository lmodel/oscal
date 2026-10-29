---
type: Policy
id: https://w3id.org/lmodel/oscal/knowledge/policies/license-and-attribution
genre: reference
title: License and attribution
description: "Which licence covers what in the oscal repository: Apache-2.0 for the schema, the generated models and the code; the OSCAL metaschema copy, NIST's work in the public domain and dedicated worldwide under CC0 1.0, with NIST's request for acknowledgement; the CNCF AI benchmark fixtures under Apache-2.0 and Luigi Carpio's fixture under MIT; the linkml-project-copier scaffolding under MIT; the KTL sidecar and site templates under Apache-2.0; and the bundle under CC BY 4.0."
resource: NOTICE
relatedTo:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/metaschema-copy
  - https://w3id.org/lmodel/oscal/knowledge/datasets/cncf-ai-benchmarks
  - https://w3id.org/lmodel/oscal/knowledge/datasets/luigi-carpio-component-definition
sources:
  - id: notice
    resource: NOTICE
    title: every section
  - id: readme.md
    resource: README.md
    title: the License and Credits sections
  - id: website-notice
    resource: website/NOTICE
    title: the graph explorer's notice
  - resource: LICENSE
    title: the Apache License, Version 2.0
  - resource: CONTRIBUTING.md
    title: the License section
  - resource: src/oscal/schema/metaschema/LICENSE.md
    title: NIST's licence
  - resource: tests/data/luigi_carpio/LICENSE.txt
    title: the MIT License of the Luigi Carpio fixture
  - resource: website/README.md
    title: the typefaces paragraph
  - resource: .lokf/knowledge/index.md
    title: the license key
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:47:10Z"
  revision: 928ef231c9fe1766b5f38ad26ece260a7ab1d870
status: draft
---

# License and attribution

`NOTICE` names the project "OSCAL LinkML Schema (oscal)", copyright 2026 Noel McLoughlin. It says that the code in the repository is licensed under the Apache License, Version 2.0, which `LICENSE` holds, and that some of the content the repository carries is third-party work under its own terms.[^notice] The README says that the schema and the code are under the Apache License 2.0, and that this is not an official NIST project and its use implies no endorsement by NIST.[^readme.md] CONTRIBUTING.md says that a contribution is licensed under the Apache License 2.0, and asks that NOTICE be updated when something new comes from elsewhere.

## What NOTICE lists

- **The schema's rendering of OSCAL.** `src/oscal/schema/*.yaml`, `src/oscal/datamodel/` and `project/` model what NIST's OSCAL defines. They are this project's rendering of OSCAL 1.2.3 as a LinkML schema, with NIST as the source of the definitions. They are not NIST's, and their use does not imply endorsement by NIST.
- **OSCAL's metaschema, by NIST.** `src/oscal/schema/metaschema/` holds OSCAL's metaschema sources from the v1.2.3 release, beside NIST's `LICENSE.md`. NIST's work is in the public domain within the United States, and NIST dedicates it to the worldwide public domain under CC0 1.0. NIST asks that a derived work acknowledge NIST as the source and note the date and nature of its changes, and CHANGELOG.md records each release of this rendering and what it changed. See [OSCAL metaschema copy](../datasets/metaschema-copy.md).
- **Test fixtures.** `tests/data/cncf-ai-benchmarks/` holds OSCAL component definitions from oscal-compass-lab/ai-benchmarks, licensed under the Apache License, Version 2.0, and `tests/data/invalid/cncf-ai-benchmarks/` holds copies of them with one fault injected in each. `tests/data/luigi_carpio/` holds a component definition by Luigi Carpio, licensed under the MIT License, whose text is `tests/data/luigi_carpio/LICENSE.txt`.
- **linkml-project-copier.** The project was generated from this template, and its justfile, configuration and documentation scaffolding derive from it, under the MIT License, copyright 2025 David Linke. The README credits the template by its DOI, `10.5281/zenodo.15163584`.
- **The knowledge bundle's tooling.** The scripts under `.lokf/scripts/` and `.lokf/m365/` and the knowledge-librarian, knowledge-registrar, knowledge-release and knowledge-sync workflows are copies of the ktl-sidecar templates in knowledge-trust-ladder. `website/` and the knowledge-website workflow derive from its ktl-website templates. All of them are licensed under the Apache License, Version 2.0.

`website/NOTICE` says that `src/components/KnowledgeGraph.astro` is adapted from the LOKF toolkit's site, copyright 2026 Nolan Nichols, under the Apache License, Version 2.0, and that the file's header comment lists the changes.[^website-notice] `website/README.md` says that the site's two typefaces are self-hosted from Fontsource under the SIL Open Font License 1.1. The bundle's root `index.md` declares the licence CC BY 4.0 for the knowledge bundle itself.

[^notice]: NOTICE, every section
[^readme.md]: README.md, the License and Credits sections
[^website-notice]: website/NOTICE, the whole file
