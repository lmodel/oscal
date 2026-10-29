---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/metaschema-copy
genre: reference
title: OSCAL metaschema copy
description: "OSCAL's metaschema sources from the v1.2.3 release (usnistgov/OSCAL `src/metaschema` at commit e061961), copied byte for byte with NIST's LICENSE.md into `src/oscal/schema/metaschema/`: never edited here, the source of the allowed values every enum renders, which tests/test_schema_rules.py checks, and compared weekly with upstream by scripts/check_upstream_release.py."
resource: src/oscal/schema/metaschema
version: 1.2.3
license: https://creativecommons.org/publicdomain/zero/1.0/
derivedFrom:
  - https://w3id.org/lmodel/oscal/knowledge/references/nist-oscal
source:
  - https://github.com/usnistgov/OSCAL/tree/e061961c7702afeabffdf5e59894d35e748dade1/src/metaschema
sources:
  - id: notice
    resource: NOTICE
    title: the section OSCAL metaschema, by NIST
  - id: metaschema-readme.md
    resource: src/oscal/schema/metaschema/readme.md
    title: NIST's description of a metaschema
  - id: license.md
    resource: src/oscal/schema/metaschema/LICENSE.md
    title: NIST's licence
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the rules on the metaschema copy and on oscal_allowed_values
  - id: schema-readme.md
    resource: src/oscal/schema/README.md
    title: the metaschema item
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: _load, _allowed_values and the two enum tests
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring, the pins and the comparison
  - resource: .pre-commit-config.yaml
    title: the comment and the exclude list
  - resource: pyproject.toml
    title: the codespell and typos skip lists
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:56:26Z"
  revision: 9682284a2e351227aebe66a0fe34180d933ad8f8
status: draft
---

# OSCAL metaschema copy

NOTICE says that `src/oscal/schema/metaschema/` holds a copy of OSCAL's metaschema sources, retrieved from the `src/metaschema` folder of usnistgov/OSCAL at commit `e061961c7702afeabffdf5e59894d35e748dade1`, the v1.2.3 release.[^notice] NIST's `LICENSE.md` from the root of the same commit sits beside them. NOTICE says that every file is identical to its counterpart there, and that `scripts/check_upstream_release.py` checks that it stays so.

The folder holds one `_metaschema.xml` file for each of OSCAL's metaschema modules, such as `oscal_catalog_metaschema.xml`, `oscal_ssp_metaschema.xml` and `oscal_complete_metaschema.xml`, and the shared-constraint files in `shared-constraints/`. NIST's own `readme.md` there says that an OSCAL metaschema defines the information structures of an OSCAL model in a format-neutral form, and that OSCAL's XML and JSON schemas, its conversion scripts and its model documentation are generated from it.[^metaschema-readme.md]

## Licence

NOTICE says that NIST's work is in the public domain within the United States, and that NIST dedicates it to the worldwide public domain under CC0 1.0. NIST asks that a derived work acknowledge NIST as the source and note the date and nature of its changes, and NOTICE says that CHANGELOG.md records each release of this rendering and what it changed. `LICENSE.md` in the folder is NIST's own statement of those terms.[^license.md] [License and attribution](../policies/license-and-attribution.md) lists the other terms in the repository.

## Never edited here

CONTRIBUTING.md says to leave the folder as upstream wrote it. To move to another release, replace the folder whole from one OSCAL release, and move the pins in `scripts/check_upstream_release.py` and the schema header.[^contributing.md] The schema directory's README says the same.[^schema-readme.md] The pre-commit configuration excludes the folder, so that no hook rewrites a file that the upstream check matches by git object hash, and the codespell and typos settings in `pyproject.toml` skip it.

## How the schema uses it

CONTRIBUTING.md asks that each enum name, in its `oscal_allowed_values` annotation, the metaschema lists it renders. `tests/test_schema_rules.py` reads every `allowed-values` list in the copy's `_metaschema.xml` files with the standard library's XML parser.[^test_schema_rules.py] It writes the text of each shared-constraint file in by hand, so the parser resolves no external entity. It keys a list by its `id`. OSCAL reuses four ids in two definitions each, so such a list is keyed `id@definition`, after the nearest named definition around it, and a list with no id is keyed by its file, its definition path and its target. Two tests then hold the schema to the copy:

- `test_every_enum_names_its_lists` checks that each enum names at least one list in `oscal_allowed_values`, and that each name is a list of the copy;
- `test_enums_render_the_pinned_metaschema` checks that an enum holds exactly the values of the lists it names, and carries `allow_any` exactly when one of those lists admits other values. Its docstring says that OSCAL 1.2.3 lists a blank location type marked TBD, which the schema leaves out.

## The upstream check

`scripts/check_upstream_release.py` pins the release as `PINNED_TAG`, `v1.2.3`, the commit as `PINNED_COMMIT`, and the folder as `PINNED_PATH`, `src/metaschema`. It takes `LICENSE.md` from the root of the tree instead.[^check_upstream_release.py] It asks the GitHub API for usnistgov/OSCAL's latest release and for the pinned tree, and compares every copied file with its blob there by git object hash, so it downloads nothing but two listings. It prints a Markdown report, and exits 1 when a newer release is out or a file differs. [Upstream watch](../workflows/upstream-watch.md) runs it weekly, and [Move the upstream pins](../playbooks/update-upstream-pins.md) says what to do when it reports.

[^notice]: NOTICE, the section OSCAL metaschema, by NIST
[^metaschema-readme.md]: src/oscal/schema/metaschema/readme.md, the whole page
[^license.md]: src/oscal/schema/metaschema/LICENSE.md, the whole page
[^contributing.md]: CONTRIBUTING.md, the table of paths and the rules in Before opening a pull request
[^schema-readme.md]: src/oscal/schema/README.md, the metaschema item
[^test_schema_rules.py]: tests/test_schema_rules.py, `_load`, `_allowed_values`, test_every_enum_names_its_lists and test_enums_render_the_pinned_metaschema
[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring, the pins, ELSEWHERE and check()
