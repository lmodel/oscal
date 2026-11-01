<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# oscal

Open Security Controls Assessment Language (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/oscal](https://lmodel.github.io/oscal)

## What it models

The schema models NIST's [Open Security Controls Assessment Language](https://pages.nist.gov/OSCAL/) (OSCAL) 1.2.3. It has one module for each of OSCAL's models: the catalog, the profile, the component definition, the system security plan, the assessment plan and results, the plan of action and milestones, and the mapping collection. Every model shares OSCAL's metadata and back matter, which the catalog module defines.

The schema header pins OSCAL's release tag and commit, and [src/oscal/schema/metaschema/](src/oscal/schema/metaschema) holds that commit's metaschema sources. Each enum names the allowed-values lists it renders there, which `tests/test_schema_rules.py` checks. A weekly workflow opens an issue when NIST releases a newer OSCAL or the copy drifts.

## Mappings

None yet.

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

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/oscal.yaml`, is the copy `just lokf-adapt` writes from `src/oscal/schema/oscal.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-oscal.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots these classes on `Concept`, so a concept may name any of them, or a subclass, as its `type`. In Obsidian, add them to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
Catalog, Profile, ComponentDefinition, SystemSecurityPlan, AssessmentPlan, AssessmentResults, PlanOfActionAndMilestones, MappingCollection
```

OSCAL gives none of these classes an identifier slot, so a concept keeps each one's required `uuid` and `metadata`, and its `id` names it beside them.

The copy renames what LOKF defines: the classes `Role`, `Parameter`, `Citation` and `Revision` take an `Oscal` prefix, and seventeen keys, such as `title`, `version` and `last-modified`, an `oscal_` one. It writes OSCAL's hyphenated keys with underscores, so `oscal-version` becomes `oscal_oscal_version`. Seven keys are also slsa's or github-actions' under another IRI, and `tests/test_schema_rules.py` lists them and fails on a new shared key.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)). OSCAL's metaschema is NIST's work, in the public domain, and keeps NIST's licence beside it, and the third-party test documents keep their own: see [NOTICE](NOTICE). This is not an official NIST project, and its use implies no endorsement by NIST.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
