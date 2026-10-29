# Change Log

## 2026-10-29

* **Changed**: Element names says that OSCAL documents have their keys rewritten before they validate, as `.linkmllint.yaml` now says.
* **Resolved**: `.linkmllint.yaml` no longer says that OSCAL JSON validates without translation; it names the key rewrite the tests do.
* **Changed**: Knowledge librarian says when the skills pin moves past v0.57.0, from CHANGELOG.md.
* **Resolved**: CHANGELOG.md now says that the pin stays at v0.57.0 until the first weekly sync.
* **Source map**: dropped `scripts/debug_each_generator.py` and `scripts/detect_linkml_class.py`, which the repository removed.
* **Changed**: oscal documentation site says that `just testdoc` serves the site, from the justfile.
* **Source map**: the map records the commit of the tree it was read at.
* **Changed**: the footnotes that name a recipe, a function or a key with a leading underscore now set it in a code span, so Markdown no longer reads the underscores as emphasis.
* **Source map**: the map now names every repository path the bundle derives from, by its path from the root, with the concepts each yields and how to re-check it, and the paths left out with the reason for each; it drops the August account of the first run and the gaps it noted, which the new concepts now cover.
* **Question**: Element names and the shared namespace asks whether `.linkmllint.yaml`'s claim that OSCAL JSON validates without translation still holds, since the tests rewrite hyphenated keys first.
* **Question**: Knowledge Librarian asks whether its skills pin at v0.57.0 is meant to trail the v0.58.0 sidecar copies until the first sync.
* **Changed**: OSCAL Schema (top-level) now renders OSCAL 1.2.3, pinned to tag v1.2.3 and commit e061961, with every module under `https://w3id.org/lmodel/oscal/`, and describes `.lokf/oscal.yaml`, the adapt copy that is the bundle's domain schema; it cites the schema by its repository path.
* **Changed**: the catalog module concept now renders OSCAL 1.2.3 under `https://w3id.org/lmodel/oscal/oscal_catalog`, names the shared metadata, back matter and types the module defines, and cites it by its repository path.
* **Changed**: the profile module concept now renders OSCAL 1.2.3 under `https://w3id.org/lmodel/oscal/oscal_profile`, names the Profile class's required slots and its import of the catalog module, and cites the module by its repository path.
* **Changed**: the system security plan module concept now renders OSCAL 1.2.3 under `https://w3id.org/lmodel/oscal/oscal_ssp`, names the required slots and the system characteristics' new props and links, and cites the module by its repository path.
* **Changed**: the assessment plan module concept now renders OSCAL 1.2.3 under `https://w3id.org/lmodel/oscal/oscal_assessment_plan`, names its required slots and the assessment-common and implementation-common classes that four other modules import from it, and cites it by its repository path.
* **Changed**: the assessment results module concept now renders OSCAL 1.2.3 under `https://w3id.org/lmodel/oscal/oscal_assessment_results`, names its required slots and its imports, and cites it by its repository path.
* **Changed**: the component definition module concept now renders OSCAL 1.2.3 under `https://w3id.org/lmodel/oscal/oscal_component`, names its required slots, its imports and the fixtures that exercise it, and cites it by its repository path.
* **Changed**: the mapping collection module concept now renders OSCAL 1.2.3 under `https://w3id.org/lmodel/oscal/oscal_mapping`, names its required slots and its import of the catalog module, and cites it by its repository path.
* **Changed**: the POA&M module concept now renders OSCAL 1.2.3 under `https://w3id.org/lmodel/oscal/oscal_poam`, names its required slots and its imports, and cites it by its repository path.
* **Changed**: CNCF AI Ecosystem OSCAL Benchmarks now cites the fixtures by their repository paths and NOTICE for their licence, says that the schema renders OSCAL 1.2.3 while the fixtures declare 1.2.1, and names the recipe and tests that check them.
* **Changed**: NIST 800-53 Rev 5 to AWS Service Mapping (Luigi Carpio) now cites the fixture by its repository path, takes the 31 controls and the five CJIS deltas from its README, which corrects an earlier count of 29, and lists what the test-luigi-carpio recipe checks.
* **Changed**: NIST OSCAL now names OSCAL 1.2.3, the v1.2.3 tag and commit e061961 that the schema renders, and takes its description of OSCAL and its layers from the repository's own files; it drops the reversed `about` link to the schema, which `derivedFrom` on the schema already states.
* **Changed**: LinkML now says what this repository takes from LinkML, from its own files: the template it was built from, the locked versions, the generators the recipes run and the known generator limits the tests record; it drops the reversed `about` link to the schema.
* **Changed**: lmodel now takes the organization from `.copier-answers.yml` and the repository's addresses, rather than from `pyproject.toml`'s authors, which name a person, and names the neighbouring lmodel repositories the tests read.
* **Added**: Build and test (main.yaml), from `.github/workflows/main.yaml`.
* **Added**: Lint & docs (lint-and-docs.yaml), from `.github/workflows/lint-and-docs.yaml`.
* **Added**: Semantic release (semantic-release.yml), from `.github/workflows/semantic-release.yml`.
* **Added**: Upstream watch (upstream-watch.yaml), from `.github/workflows/upstream-watch.yaml`.
* **Added**: Knowledge website (knowledge-website.yaml), from `.github/workflows/knowledge-website.yaml`.
* **Added**: Knowledge Registrar (knowledge-registrar.yaml), from `.github/workflows/knowledge-registrar.yaml`.
* **Added**: Knowledge Librarian (knowledge-librarian.yaml), from `.github/workflows/knowledge-librarian.yaml`.
* **Added**: Knowledge Release (knowledge-release.yaml), from `.github/workflows/knowledge-release.yaml`.
* **Added**: Knowledge sync (knowledge-sync.yaml), from `.github/workflows/knowledge-sync.yaml`.
* **Added**: OSCAL metaschema copy, from `src/oscal/schema/metaschema`.
* **Added**: Generated artefacts, from `project`.
* **Added**: Test data and schema tests, from `tests/data`.
* **Added**: Element names and the shared namespace, from `README.md`.
* **Added**: Scope, influences and mappings, from `README.md`.
* **Added**: Regenerate and test the schema, from `CONTRIBUTING.md`.
* **Added**: Release the schema, from `CONTRIBUTING.md`.
* **Added**: Move the upstream pins, from `scripts/check_upstream_release.py`.
* **Added**: Validate OSCAL data against the schema, from `project.justfile`.
* **Added**: License and attribution, from `NOTICE`.
* **Added**: Security policy, from `SECURITY.md`.
* **Added**: AI covenant, from `AI_COVENANT.md`.
* **Added**: oscal documentation site, from `website`.

## 2026-08-05

* **Source map**: Orphan sweep accounted for the remaining top-level directories: recorded `tmp/` and `examples/` (generated outputs, same rationale as `project/`) and `docs/` (MkDocs site generated from the schema) as conscious exclusions in `playbooks/knowledge-sources.md` gaps. Re-verified all 11 datasets, 2 references, and the org concept against their sources (schema versions 1.2.1, 31+31 CNCF fixtures, luigi_carpio OSCAL 1.1.2) - no drift.
* **Namespace migration**: Changed `base_iri` from `https://github.com/lmodel/oscal/knowledge/` to `https://w3id.org/lmodel/oscal/knowledge/`, rewriting every concept `id`, the publisher `id`, and all typed-relation targets (55 IRIs across 15 concepts). Rationale: the old IRIs sat inside github.com's URL space, which the project does not control and where they can never dereference; the w3id.org namespace matches the schema's own `https://w3id.org/lmodel/oscal` authority and can later be made to resolve via a `perma-id/w3id.org` redirect rule pointing at the GitHub Pages site. `resource`/`access_url` values (real GitHub blob/tree links) are unchanged. No external consumers existed yet, so no links were broken.
* **Removal**: `tests/data/open_control/` was deleted from the repository (along with its `tests/data/README.md` entry). Removed the corresponding `references/open-control` concept, its bullets in `knowledge/index.md` and `knowledge/references/index.md`, and its row in `playbooks/knowledge-sources.md`'s source map (including the now-moot note about the corrupted `component_v1.0.0.yaml` stub, since the fixture no longer exists).
* **Steady-state refresh**: Re-verified all 9 existing schema datasets, both references, and the org concept against their sources (versions, imports/`hasPart`, URLs) - no drift found. Added 3 new concepts for real-world test fixtures introduced this session: `datasets/cncf-ai-benchmarks` (31 CNCF AI ecosystem Component Definition fixtures, valid + fault-injected invalid variants), `datasets/luigi-carpio-component-definition` (NIST 800-53 Rev 5 -> AWS mapping fixture), and `references/open-control` (predecessor compliance format, format-comparison reference). Noted in the source map that `tests/data/open_control/component_v1.0.0.yaml` is a corrupted `404: Not Found` stub, not real data - recorded accurately rather than assumed valid. Updated `playbooks/knowledge-sources.md` source map and gaps.
* **Initialization**: Bootstrap discovery pass. Created LOKF bundle for OSCAL with concepts derived from `src/oscal/schema/` (9 schema datasets), `CONTRIBUTING.md`/`README.md` (playbook), NIST OSCAL upstream standard (reference), LinkML framework (reference), and lmodel organization (org). Knowledge sources map recorded in `playbooks/knowledge-sources.md`.
