# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Fixed

- **`Base64Type`, `NonNegativeIntegerType` and `PositiveIntegerType` name the type they refine.** Each now says `typeof: string` or `typeof: integer` beside its own `uri`, so the Java generator maps them; under 1.11.1 it wrote `period`, `start` and `end` as `String`, and 1.12.1 stops on them.

## [0.1.1] - 2026-10-29

### Security

- **The sidecar copies and the skills pin are at Knowledge Trust Ladder [v0.59.0](https://github.com/noelmcloughlin/knowledge-trust-ladder/compare/v0.57.0...v0.59.0).** The release changed `.github/workflows/knowledge-release.yaml`, `.lokf/scripts/knowledge-conventions.sh`, `.lokf/scripts/knowledge-conventions.py`, `.lokf/scripts/knowledge-preflight.sh`, `.lokf/scripts/knowledge-report.sh` and `.lokf/m365/ktl-docent-m365.md` here.

## [0.1.0] - 2026-10-29

### Added

- **A LinkML schema of OSCAL 1.2.3, one module for each of its eight models**: catalog, profile, component definition, system security plan, assessment plan, assessment results, plan of action and milestones, and mapping collection.
- **A copy of OSCAL's metaschema sources at v1.2.3 and a weekly upstream watch.** Each of the schema's 155 enums names the allowed-values lists it renders, and a test holds it to them.
- **`.lokf/oscal.yaml`, the schema's `lokf adapt` copy, rooted on the eight models**, which the knowledge release attaches as `schema-<tag>-oscal.yaml`. Tests hold its names apart from `lokf.yaml` and pin the seven keys it shares with slsa's and github-actions' copies.
- **An example of each model and a counter-example for each one's required content**, held to the validator by `just test`.
- **The repository's KTL knowledge bundle and its sidecar automation**, from the KTL v0.58.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site. The librarian's skills pin, which those templates leave at v0.57.0, moves at the first weekly sync.

### Changed

- **Every element's IRI moves under `https://w3id.org/lmodel/oscal/`**, from a namespace per module, such as `https://w3id.org/lmodel/oscal_catalog/`, that no w3id route serves.
- **OSCAL's `class` key is the slot `class_`, formerly `_class`.** A slot named `class` breaks the generated dataclasses, and gen-doc's page for `_class` was hidden from the site.
- **The OSCAL 1.2.3 values join four enums**: control status, component type, location type and data-center class. A control's status now admits other values, and `Withdrawn` is gone, as in OSCAL.

### Fixed

- **A system security plan's system characteristics take `props` and `links`**, as OSCAL defines them, and the integer types state their minimums.
