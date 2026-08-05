---
type: Dataset
id: https://w3id.org/lmodel/oscal/knowledge/datasets/luigi-carpio-component-definition
title: NIST 800-53 Rev 5 to AWS Service Mapping (Luigi Carpio)
description: A real-world OSCAL Component Definition JSON fixture mapping NIST 800-53 Rev 5 security controls to AWS services, with FedRAMP High baseline coverage and a CJIS v6.0 delta section for controls where CJIS exceeds FedRAMP High. Used for structural and domain-specific validation of the OSCAL model.
version: "1.1.2"
resource: https://github.com/lmodel/oscal/tree/main/tests/data/luigi_carpio
license: MIT
timestamp: "2026-08-05T00:00:00Z"
about:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/oscal-component-schema
---

# NIST 800-53 Rev 5 to AWS Service Mapping (Luigi Carpio)

A single `component-definition.json` fixture (`tests/data/luigi_carpio/component-definition.json`, OSCAL `oscal-version` 1.1.2 — older than the 1.2.1 modeled by this repository's schema) mapping 29 NIST 800-53 Rev 5 controls to AWS services via OSCAL `props`. Each `implemented_requirement` carries a `fedramp-high` property, and a subset also carry a `cjis-delta` property marking where CJIS v6.0 exceeds the FedRAMP High baseline (e.g. AC-2 quarterly account reviews, IA-2 phishing-resistant AAL2 MFA, AU-6 one-year audit retention, SC-28 agency-managed encryption keys, IR-6 CSO/FBI CJIS Division reporting).

Validated by the `test-luigi-carpio` recipe in `project.justfile`, which checks `metadata.last_modified` format, the `fedramp-high`/`cjis-delta` props, component count, and UUID conformance (warn by default, fail under `test-luigi-carpio-strict` / `OSCAL_STRICT_UUID=1`).
