---
lokf_version: "0.1"
okf_version: "0.1"
base_iri: https://github.com/lmodel/oscal/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: OSCAL Knowledge Bundle
description: LinkML schema encoding the NIST Open Security Controls Assessment Language (OSCAL), providing machine-readable representations for security controls, assessments, and compliance data.
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Organization
  id: https://github.com/lmodel/oscal/knowledge/org/lmodel
  name: lmodel
---

# OSCAL Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for OSCAL (Open Security Controls Assessment Language). Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

## Datasets

* [OSCAL Schema (top-level)](datasets/oscal-schema.md) - Aggregating top-level LinkML schema for OSCAL.
* [OSCAL Catalog Schema](datasets/oscal-catalog-schema.md) - Control Catalog model.
* [OSCAL Profile Schema](datasets/oscal-profile-schema.md) - Profile model.
* [OSCAL SSP Schema](datasets/oscal-ssp-schema.md) - System Security Plan model.
* [OSCAL Assessment Plan Schema](datasets/oscal-assessment-plan-schema.md) - Assessment Plan model.
* [OSCAL Assessment Results Schema](datasets/oscal-assessment-results-schema.md) - Assessment Results model.
* [OSCAL Component Definition Schema](datasets/oscal-component-schema.md) - Component Definition model.
* [OSCAL Mapping Schema](datasets/oscal-mapping-schema.md) - Mapping Collection model.
* [OSCAL POAM Schema](datasets/oscal-poam-schema.md) - Plan of Action and Milestones model.
* [CNCF AI Ecosystem OSCAL Benchmarks](datasets/cncf-ai-benchmarks.md) - 31 real-world Component Definition fixtures (valid + fault-injected invalid) from the CNCF AI ecosystem.
* [NIST 800-53 Rev 5 to AWS Service Mapping](datasets/luigi-carpio-component-definition.md) - Real-world Component Definition fixture mapping NIST 800-53 Rev 5 to AWS services (FedRAMP High + CJIS).

## References

* [NIST OSCAL](references/nist-oscal.md) - Upstream NIST OSCAL standard (the authoritative source).
* [LinkML](references/linkml.md) - The Linked Data Modeling Language used to author all schemas.

## Playbooks

* [Knowledge Sources](playbooks/knowledge-sources.md) - Map of knowledge sources scraped to build this bundle.

## Organizations

* [lmodel](org/lmodel.md) - The lmodel GitHub organization that publishes this project.
