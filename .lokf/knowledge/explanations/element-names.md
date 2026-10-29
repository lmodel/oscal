---
type: Explanation
id: https://w3id.org/lmodel/oscal/knowledge/explanations/element-names
genre: explanation
title: Element names and the shared namespace
description: "Why the OSCAL schema names its elements as it does: OSCAL's own keys as slot names (`last-modified`, and `class_` for OSCAL's `class`), UpperCamelCase classes and enums, and every element under `oscal:`; and why its adapt copy gives LOKF's Role, Parameter, Citation and Revision an Oscal prefix and seventeen keys an `oscal_` one, and shares seven keys (attestations, dependencies, parties, provenance, subject, value, actions) with slsa's and github-actions' copies under another IRI."
resource: README.md
about:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-schema
sources:
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: linkmllint.yaml
    resource: .linkmllint.yaml
    title: the comment and the standard_naming rule
  - id: oscal_catalog.yaml
    resource: src/oscal/schema/oscal_catalog.yaml
    title: the comment on class_
  - id: ai_covenant.md
    resource: AI_COVENANT.md
    title: the item on the namespace
  - id: changelog.md
    resource: CHANGELOG.md
    title: the Changed items
  - id: lokf-oscal.yaml
    resource: .lokf/oscal.yaml
    title: the last note
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: SHARED_WITH_NEIGHBOURS, test_names_apart_from_lokf and test_names_apart_from_neighbours
  - resource: CONTRIBUTING.md
    title: the rules on names and conventions
generated:
  by: process:ktl-librarian
  at: "2026-10-29T01:15:40Z"
status: draft
---

# Element names and the shared namespace

## OSCAL's own names

CONTRIBUTING.md asks for UpperCamelCase classes and enums, OSCAL's own keys as slot names, and a short description on every element, which `just lint` checks. `.linkmllint.yaml` keeps LinkML's recommended lint rules but lowers `standard_naming` to a warning, which `just lint` does not fail on. Its comment says why: slots keep OSCAL's own hyphenated keys, such as `last-modified` and `finding-uuid`, so the schema reads as the metaschema does. It adds that the generators write those keys with underscores, so an OSCAL JSON document has its keys rewritten before it validates, as the `_test-linkml-validate` recipe and `tests/test_data.py` do.[^linkmllint.yaml]

OSCAL's `class` key is the slot `class_`. The catalog module's comment says that a slot or alias named `class` makes the generated dataclasses invalid Python, and that gen-doc names a page after the slot, so `_class` hid its page from the site. `class_` is the spelling the generated Pydantic model gives a slot named `class`.[^oscal_catalog.yaml] CHANGELOG.md records the rename from `_class`.[^changelog.md]

AI_COVENANT.md says that everything the schema defines lives under `oscal:`, which is `https://w3id.org/lmodel/oscal/`, and that OSCAL's own names, such as property names and link relations, appear only as values the schema documents.[^ai_covenant.md] CHANGELOG.md says that every element's IRI moved there from a namespace per module, such as `https://w3id.org/lmodel/oscal_catalog/`, that no w3id route serves.

## The adapt copy's renames

The README says that a host imports the adapt copy, `.lokf/oscal.yaml`, beside `lokf.yaml`, and that LinkML merges the two into one namespace, where the last definition of a name wins silently.[^readme.md] So the copy renames what LOKF defines. The classes `Role`, `Parameter`, `Citation` and `Revision` take an `Oscal` prefix, and seventeen keys, such as `title`, `version` and `last-modified`, take an `oscal_` one. The copy also writes OSCAL's hyphenated keys with underscores, so `oscal-version` becomes `oscal_oscal_version`.

The copy's last note lists the seventeen keys, each renamed with its IRI unchanged: `title`, `description`, `id`, `name`, `type`, `status`, `sources`, `last-modified`, `version`, `media-type`, `algorithm`, `constraints`, `unit`, `target`, `reason`, `source` and `predicate`.[^lokf-oscal.yaml] The README adds that OSCAL gives none of the eight model classes an identifier slot, so a concept keeps each one's required `uuid` and `metadata`, and its `id` names it beside them.

## Keys shared with slsa and github-actions

The README says that seven keys are OSCAL's and also slsa's or github-actions' under another IRI: `attestations`, `dependencies`, `parties`, `provenance`, `subject` and `value` in slsa's copy, and `actions` in github-actions' copy. A host that imports this copy beside either projects each of those keys under one vocabulary's IRI.

`tests/test_schema_rules.py` lists the seven in `SHARED_WITH_NEIGHBOURS`.[^test_schema_rules.py] Its comment says that they are OSCAL's own keys, and that `lokf adapt` renames only what `lokf.yaml` defines, so they stay until it can rename what a neighbour copy defines too. Two tests check the names:

- `test_names_apart_from_lokf` fails when a class, enum, type or subset name of `.lokf/oscal.yaml` is LOKF's, or when a slot name the two share carries another IRI;
- `test_names_apart_from_neighbours` fails when such a name appears in `tests/neighbours/slsa.yaml` or `tests/neighbours/github-actions.yaml`, or when the keys shared with them under another IRI are not exactly the listed ones, so a new shared key fails it.

CONTRIBUTING.md asks contributors to keep names apart from LOKF's, slsa's and github-actions', because a host imports the copies together.

[^linkmllint.yaml]: .linkmllint.yaml, the comment and rules
[^oscal_catalog.yaml]: src/oscal/schema/oscal_catalog.yaml, the comment on the class_ slot
[^changelog.md]: CHANGELOG.md, the Changed items of the Unreleased section
[^ai_covenant.md]: AI_COVENANT.md, the third item of A note specific to this project
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^lokf-oscal.yaml]: .lokf/oscal.yaml, the last note, which lokf adapt wrote
[^test_schema_rules.py]: tests/test_schema_rules.py, SHARED_WITH_NEIGHBOURS and its comment, test_names_apart_from_lokf and test_names_apart_from_neighbours
