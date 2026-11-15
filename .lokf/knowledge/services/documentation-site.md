---
type: Service
id: https://w3id.org/lmodel/oscal/knowledge/services/documentation-site
genre: reference
title: oscal documentation site
description: The Hugo site in website/, built from the README, docs/, the schema's gen-doc pages, the changelog and the knowledge bundle by the Knowledge website workflow, which deploys it to GitHub Pages at lmodel.github.io/oscal once KNOWLEDGE_WEBSITE_ENABLED is true; it replaced the mkdocs site, and the schema's pages keep the mkdocs addresses under /elements/.
resource: website
dependsOn:
  - https://w3id.org/lmodel/oscal/knowledge/workflows/knowledge-website
sources:
  - id: readme.md
    resource: README.md
    title: Documentation Website and the website item of Repository Structure
  - id: website-readme.md
    resource: website/README.md
    title: what each page comes from, previewing and editing
  - id: site.toml
    resource: website/site.toml
    title: the site's address, title and redirects
  - id: changelog.md
    resource: CHANGELOG.md
    title: the item on the knowledge website
  - id: justfile
    resource: justfile
    title: the testdoc and _serve recipes
  - id: lychee.toml
    resource: lychee.toml
    title: the exclusion of the site's address
  - resource: NOTICE
    title: the Knowledge bundle section
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:08:14Z"
status: draft
---

# oscal documentation site

`website/` holds a Hugo site, which the README describes as built from the README, `docs/`, the schema's pages and the knowledge bundle, and whose address it gives as `https://lmodel.github.io/oscal`.[^readme.md] CHANGELOG.md says that this knowledge website replaces the mkdocs site.[^changelog.md] NOTICE says that the site derives from the ktl-website templates of the Knowledge Trust Ladder repository.

`website/README.md` says that the Knowledge website workflow publishes the site to GitHub Pages at `https://lmodel.github.io/oscal/`.[^website-readme.md] `website/site.toml` names the repository `lmodel/oscal`, the address `https://lmodel.github.io` and the base path `/oscal`.[^site.toml] A comment in `lychee.toml` says that the site answers once the workflow first deploys it to Pages, so the link check leaves its address out until then.[^lychee.toml]

## What the pages come from

`website/README.md` says that every page comes from a file the repository already holds, so a change to the site is a change to that file:

- each concept in `.lokf/knowledge/` becomes a page under `knowledge/`, with its trust label from `knowledge-report.sh`, its sources and its relations both ways, and the four files `lokf export` writes are served beside them;
- the README becomes the home page, and each page under `docs/` a page under `docs/`;
- `CHANGELOG.md` becomes a page per release under `changelog/`, which search leaves out;
- `src/oscal/schema/oscal.yaml` becomes the Schema part: a page per class, slot, enumeration and type, written by LinkML's `gen-doc`, each also at `elements/<Name>/`, where the schema's w3id rules point. The home page then leads with the schema.

`site.toml` names no `browse` folder, so the site serves no data. Its redirects send `/about` to `docs/about.md`.

## Previewing it

Previewing needs bash, git and uv. Hugo and Pagefind come from PyPI, at the versions `website/pyproject.toml` names and the hashes `website/uv.lock` holds. In `website/`, `scripts/build.sh` writes `dist/` with the search index and then checks every link between its pages. `scripts/build.sh serve` serves the site at `http://localhost:1313/oscal/` and rebuilds it as you edit. `scripts/build.sh preview` serves the site as it will be published, at `http://localhost:1313/`.[^website-readme.md] From the repository root, `just testdoc` runs `just gen-doc` and then the Hugo server, `website/scripts/build.sh serve`.[^justfile]

## Publishing it

[Knowledge website](../workflows/knowledge-website.md) builds the site on pull requests and on the default branch, and deploys it to GitHub Pages only once the repository variable `KNOWLEDGE_WEBSITE_ENABLED` is `true`.

## Editing it

Change a page's words in the file it comes from: the README, a page under `docs/`, the schema, or a concept, which goes through the librarian and the curator like any other change to the bundle. Change the site's own values in `site.toml`, and its look in `assets/css/custom.css`, which is this repository's own.

[^readme.md]: README.md, Documentation Website and the website item of Repository Structure
[^changelog.md]: CHANGELOG.md, the last item under Added
[^website-readme.md]: website/README.md, the list of page sources, Preview it and What to edit
[^site.toml]: website/site.toml, the site's address, title and redirects
[^lychee.toml]: lychee.toml, the comment above the site's address in exclude

[^justfile]: justfile, the testdoc and _serve recipes
