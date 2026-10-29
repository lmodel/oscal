---
type: Playbook
id: https://w3id.org/lmodel/oscal/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Move the upstream pins
description: "What to do when the upstream watch opens its issue because NIST released a newer OSCAL or the metaschema copy drifted: replace src/oscal/schema/metaschema/ whole from the new tag's src/metaschema/, move PINNED_TAG and PINNED_COMMIT with the schema header's version, source and annotations, run just test and update every enum that tests/test_schema_rules.py reports."
resource: scripts/check_upstream_release.py
about:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/metaschema-copy
references:
  - https://w3id.org/lmodel/oscal/knowledge/workflows/upstream-watch
  - https://w3id.org/lmodel/oscal/knowledge/references/nist-oscal
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring, the pins and the report's instructions
  - id: notice
    resource: NOTICE
    title: the section OSCAL metaschema, by NIST
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: test_header_pins_match_the_watch, test_modules_carry_the_pinned_version and the enum tests
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the rule on the metaschema copy
  - resource: src/oscal/schema/oscal.yaml
    title: the header's version, source and annotations
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:47:10Z"
  revision: 9682284a2e351227aebe66a0fe34180d933ad8f8
status: draft
---

# Move the upstream pins

[Upstream watch](../workflows/upstream-watch.md) runs `scripts/check_upstream_release.py` every week. The script's docstring names two things that can go wrong with `src/oscal/schema/metaschema/` with no change in this repository:[^check_upstream_release.py]

- NIST releases a newer OSCAL version, so the schema falls behind;
- the copied files drift from the tree they were taken from.

The script exits 1 on either, and the workflow then opens its issue or comments on the one already open.

## The pins

The copy has no version in its path, so the script pins the release and the commit it was taken from. `PINNED_TAG` is `v1.2.3`, `PINNED_COMMIT` is `e061961c7702afeabffdf5e59894d35e748dade1`, and `PINNED_PATH` is `src/metaschema`. A comment asks that all three move together, with the schema header's version, source and annotations, when the copy is replaced from a newer release. The umbrella schema's header gives the release as `version`, the tag and the commit in its `oscal_tag` and `oscal_commit` annotations, and the tree in `source`. NOTICE records the same commit and release.[^notice]

`tests/test_schema_rules.py` fails when the header and the script disagree.[^test_schema_rules.py] `test_header_pins_match_the_watch` compares the annotations and `source` with the pins, and requires the tag to be `v` followed by `version`. `test_modules_carry_the_pinned_version` requires every module to carry the umbrella's `version`, and each module's `source` to name that release's JSON schema under `/ns/oscal/<version>/`.

## When NIST has released a newer OSCAL

The script's report gives the steps:

1. Replace `src/oscal/schema/metaschema/` with `src/metaschema/` at the new tag, whose address the report gives. CONTRIBUTING.md asks that the folder be replaced whole from one release and never edited.[^contributing.md]
2. Move the pins in `scripts/check_upstream_release.py` and the schema header.
3. Run `just test`, and update every enum that `tests/test_schema_rules.py` reports, so that each enum holds exactly the values of the lists it names in `oscal_allowed_values`.

## When a copied file differs

The report names each copied file that differs from its counterpart in the pinned tree, or that has no counterpart there. CONTRIBUTING.md asks that the folder stay as upstream wrote it. When the GitHub API returns the pinned tree's listing truncated, the report says so and asks for the copy to be compared by hand.

[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring, the pins and the report lines check() writes
[^notice]: NOTICE, the section OSCAL metaschema, by NIST
[^test_schema_rules.py]: tests/test_schema_rules.py, test_header_pins_match_the_watch, test_modules_carry_the_pinned_version and test_enums_render_the_pinned_metaschema
[^contributing.md]: CONTRIBUTING.md, the rule on src/oscal/schema/metaschema/
