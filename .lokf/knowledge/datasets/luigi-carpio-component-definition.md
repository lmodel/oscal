---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/luigi-carpio-component-definition
title: NIST 800-53 Rev 5 to AWS Service Mapping (Luigi Carpio)
description: A third-party OSCAL 1.1.2 component definition by Luigi Carpio, tests/data/luigi_carpio/component-definition.json under MIT, mapping 31 NIST 800-53 Rev 5 controls to AWS services, each with a fedramp-high property, and marking with cjis-delta where CJIS v6.0 exceeds FedRAMP High (AC-2, IA-2, AU-6, SC-28, IR-6); the test-luigi-carpio recipe, which just test runs, checks it.
version: 1.1.2
resource: tests/data/luigi_carpio
license: MIT
timestamp: "2026-08-05T00:00:00Z"
about:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-component-schema
genre: reference
isPartOf:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/test-data
sources:
  - id: component-definition.json
    resource: tests/data/luigi_carpio/component-definition.json
    title: the metadata
  - id: luigi_carpio-readme.md
    resource: tests/data/luigi_carpio/README.md
    title: the summary, the table of controls and CJIS v6.0 Relevance
  - id: notice
    resource: NOTICE
    title: the Test fixtures section
  - id: project.justfile
    resource: project.justfile
    title: test-luigi-carpio and test-luigi-carpio-strict
  - resource: tests/data/luigi_carpio/LICENSE.txt
    title: the MIT License
  - resource: tests/data/README.md
    title: the luigi_carpio item
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:53:56Z"
  revision: 105607d4994fa4cff613c963ef4d8889f0126ac5
---

# NIST 800-53 Rev 5 to AWS Service Mapping (Luigi Carpio)

`tests/data/luigi_carpio/` holds one OSCAL component definition, `component-definition.json`, with its README and its licence. NOTICE says that the component definition is by Luigi Carpio, licensed under the MIT License, whose text is `tests/data/luigi_carpio/LICENSE.txt`.[^notice] The file's metadata gives the title "NIST 800-53 Rev 5 to AWS Service Mapping", the version 0.6.0 and `oscal-version` 1.1.2, while the schema renders OSCAL 1.2.3.[^component-definition.json]

The fixture's README says that it maps NIST 800-53 Rev 5 security controls to AWS services that support their implementation, with FedRAMP High baseline filtering and a CJIS v6.0 delta section.[^luigi_carpio-readme.md] Its table lists 31 controls, from AC-2 Account Management to SI-7 Software/Firmware Integrity. It names 5 controls where CJIS exceeds FedRAMP High: quarterly account reviews (AC-2), phishing-resistant AAL2 MFA (IA-2), 1-year audit log retention with weekly review (AU-6), agency-managed encryption keys (SC-28), and incident reporting to the CSO/FBI CJIS Division (IR-6). The README also describes a generator script and an output folder, which the copy in this repository does not hold.

## How it is checked

The `test-luigi-carpio` recipe in `project.justfile`, which `just test` runs, rewrites the file's keys with underscores, builds the generated `ComponentDefinitionDocument` from it, and checks:[^project.justfile]

- that `metadata.last_modified` is a date and time with a time zone;
- that the file keeps OSCAL's hyphenated top-level key, `component-definition`;
- that every implemented requirement carries a `fedramp-high` property whose value is `true`;
- that at least one implemented requirement carries a `cjis-delta` property;
- that the file holds at least one component.

It also checks every UUID field against a pattern for version 4 and version 5 UUIDs. A UUID that fails is a warning by default, and `just test-luigi-carpio-strict`, which sets `OSCAL_STRICT_UUID=1`, makes it a failure. See [Test data and schema tests](test-data.md).

[^notice]: NOTICE, the Test fixtures section
[^component-definition.json]: tests/data/luigi_carpio/component-definition.json, the metadata
[^luigi_carpio-readme.md]: tests/data/luigi_carpio/README.md, the opening paragraph, Compliance Controls Addressed and CJIS v6.0 Relevance
[^project.justfile]: project.justfile, test-luigi-carpio and test-luigi-carpio-strict
