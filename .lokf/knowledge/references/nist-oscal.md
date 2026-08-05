---
type: Reference
id: https://github.com/lmodel/oscal/knowledge/references/nist-oscal
title: NIST OSCAL
description: The NIST Open Security Controls Assessment Language (OSCAL) standard. The authoritative upstream specification from which all schema modules in this repository are derived.
resource: https://pages.nist.gov/OSCAL/
timestamp: "2026-08-05T00:00:00Z"
about:
  - https://github.com/lmodel/oscal/knowledge/datasets/oscal-schema
---

# NIST OSCAL

**OSCAL (Open Security Controls Assessment Language)** is a set of formats published by NIST that represent security controls and related information in machine-readable form. The goal is to automate security and privacy risk management across the supply chain.

OSCAL defines a layered model:
- **Control layer** - Catalog and Profile documents
- **Implementation layer** - System Security Plan (SSP) and Component Definition
- **Assessment layer** - Assessment Plan, Assessment Results, and POA&M
- **Mapping layer** - Cross-framework control mappings

**Version modeled in this repository:** 1.2.1

**Key references:**
- Specification: <https://pages.nist.gov/OSCAL/>
- GitHub: <https://github.com/usnistgov/OSCAL>
- JSON Schema source files: `http://csrc.nist.gov/ns/oscal/1.2.1/`
