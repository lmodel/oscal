<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# oscal

Open Security Controls Assessment Language (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/oscal](https://lmodel.github.io/oscal)

## What it models

NIST's [Open Security Controls Assessment Language](https://pages.nist.gov/OSCAL/) (OSCAL) 1.2.3, one module for each of its models:

* **Catalog** (`Catalog`): controls, their groups, parameters and parts.
* **Profile** (`Profile`): a selection of controls from catalogs, and how it alters them.
* **Component definition** (`ComponentDefinition`): components and the controls each implements.
* **System security plan** (`SystemSecurityPlan`): a system's characteristics, its implementation and how it implements a profile's controls.
* **Assessment plan** (`AssessmentPlan`) and **assessment results** (`AssessmentResults`): what an assessment covers, and what it observed and found.
* **Plan of action and milestones** (`PlanOfActionAndMilestones`): the risks a system still carries and how they are tracked.
* **Mapping collection** (`MappingCollection`): how the controls of one catalog relate to another's.

Every model shares OSCAL's metadata and back matter, which the catalog module defines. The schema header's `version` is OSCAL's release, 1.2.3, and its annotations pin the release's tag and commit. [src/oscal/schema/metaschema/](src/oscal/schema/metaschema) holds that commit's metaschema sources, and each enum names the allowed-values lists it renders there, which `tests/test_schema_rules.py` checks. A weekly workflow opens an issue when NIST releases a newer OSCAL or the copy drifts. Release tags number the schema's versions.

## Influences

None beyond OSCAL itself: the schema renders one specification, and its module layout, release asset and governance files follow [lmodel/slsa](https://github.com/lmodel/slsa).

## Mappings

None yet: no element names a term of another vocabulary.

## Not modelled here

OSCAL's metaschema states constraints that the schema does not check: the keys an `index`, `index-has-key` or `is-unique` constraint names, `expect` tests, and `has-cardinality` counts. An OSCAL document that passes the schema can still fail NIST's own validators on these.

## Repository Structure

* [docs/](docs/): the website's pages, with the generated schema pages in [elements/](docs/elements/)
* [examples/](examples/): usage examples
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch
* [src/oscal/schema/](src/oscal/schema): the LinkML schema, `oscal.yaml` and the modules it imports (edit these), and the metaschema copy
* [src/oscal/datamodel/](src/oscal/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data and third-party OSCAL documents in [data/](tests/data)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema is `.lokf/oscal.yaml`, which `lokf adapt` writes from `src/oscal/schema/oscal.yaml`. Edit the source, never the copy. A release carries the copy as `schema-<tag>-oscal.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

`just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` says when it is stale. `project.justfile` names the classes the copy roots on `Concept`, and a concept may name any of them, or a subclass, as its `type`. In Obsidian, add these classes to the KTL Registrar and KTL Curator plugins' *Known LOKF types* setting:

```text
Catalog, Profile, ComponentDefinition, SystemSecurityPlan, AssessmentPlan, AssessmentResults, PlanOfActionAndMilestones, MappingCollection
```

OSCAL gives none of these classes an identifier slot, so a concept keeps each one's required `uuid` and `metadata`, and its `id` names it beside them.

A host imports the copy beside `lokf.yaml`, and LinkML merges the two into one namespace, where the last definition of a name wins silently. So the copy renames what LOKF defines: the classes `Role`, `Parameter`, `Citation` and `Revision` take an `Oscal` prefix, and seventeen keys, such as `title`, `version` and `last-modified`, an `oscal_` one. The copy also writes OSCAL's hyphenated keys with underscores, so `oscal-version` becomes `oscal_oscal_version`.

Seven keys are OSCAL's and also slsa's or github-actions' under another IRI: `attestations`, `dependencies`, `parties`, `provenance`, `subject` and `value` in slsa's copy, and `actions` in github-actions'. A host that imports this copy beside either projects each of those keys under one vocabulary's IRI. `tests/test_schema_rules.py` checks the copy against all three schemas and fails on a new shared key.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)).

OSCAL's metaschema in [src/oscal/schema/metaschema/](src/oscal/schema/metaschema) is NIST's work, in the public domain, and keeps NIST's licence beside it; the third-party test documents keep their own: see [NOTICE](NOTICE).

This is not an official NIST project, and its use implies no endorsement by NIST.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
