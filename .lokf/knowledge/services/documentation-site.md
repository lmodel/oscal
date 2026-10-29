---
type: Service
id: https://w3id.org/lmodel/oscal/knowledge/services/documentation-site
genre: reference
title: oscal documentation site
description: The Astro Starlight site in website/, built from the README, docs/, the schema's gen-doc pages, the changelog and the knowledge bundle by the Knowledge website workflow, which deploys it to GitHub Pages at lmodel.github.io/oscal once KNOWLEDGE_WEBSITE_ENABLED is true; it replaced the mkdocs site, and its REDIRECTS send the mkdocs addresses on to the new pages.
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
  - id: site.config.mjs
    resource: website/site.config.mjs
    title: REPO, SITE, BASE, DOCS, REDIRECTS, CHANGELOG, SCHEMA and BROWSE
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
  at: "2026-10-29T01:15:40Z"
status: draft
---

# oscal documentation site

`website/` holds an Astro Starlight site, which the README describes as built from the README, `docs/`, the schema's pages and the knowledge bundle, and whose address it gives as `https://lmodel.github.io/oscal`.[^readme.md] CHANGELOG.md says that this knowledge website replaces the mkdocs site.[^changelog.md] NOTICE says that the site derives from the ktl-website templates of the Knowledge Trust Ladder repository.

`website/README.md` says that the Knowledge website workflow publishes the site to GitHub Pages at `https://lmodel.github.io/oscal/`.[^website-readme.md] `website/site.config.mjs` names the repository `lmodel/oscal`, the address `https://lmodel.github.io` and the base path `/oscal`.[^site.config.mjs] A comment in `lychee.toml` says that the site answers once the workflow first deploys it to Pages, so the link check leaves its address out until then.[^lychee.toml]

## What the pages come from

`website/README.md` says that every page comes from a file the repository already holds, so a change to the site is a change to that file:

- each concept in `.lokf/knowledge/` becomes a page under `knowledge/`, with its trust label from `knowledge-report.sh`, its sources and its typed relations both ways, and the four files `lokf export` writes are served beside them;
- the README becomes the home page, and each page under `docs/` a page under `docs/`, except `docs/templates-linkml/`, which `site.config.mjs` leaves out;
- `CHANGELOG.md` becomes a page per release under `changelog/`, which `site.config.mjs` shows once the file holds a released version;
- the schema's pages, which `gen-doc` writes into `docs/elements/`, become a page each under `schema/`, with their class diagrams drawn in the browser. The folder is not committed, so the sync runs the command that builds it when it is missing.

`site.config.mjs` shows no data pages, since `BROWSE` is `null`. Its `REDIRECTS` send the addresses that the mkdocs site gave its pages on to the new ones: `/elements` and each `/elements/<name>` to `/schema/`, and `/about` to `/docs/about/`.

## Previewing it

Previewing needs Node.js 22.12 or later and uv. In `website/`, run `npm ci --ignore-scripts`, then `npm run dev` for a local server, or `npm run build`, which writes `dist/` and then checks every link between its pages. Both run `npm run sync` first, which runs `lokf export` from the sidecar's environment in `.lokf/` and writes the generated pages. Nothing the sync writes is committed. From the repository root, `just testdoc` runs `just gen-doc` and then the same local server.[^justfile]

## Publishing it

[Knowledge website](../workflows/knowledge-website.md) builds the site on pull requests and on the default branch, and deploys it to GitHub Pages only once the repository variable `KNOWLEDGE_WEBSITE_ENABLED` is `true`.

## Editing it

Change a page's words in the file it comes from: the README, a page under `docs/`, the schema, or a concept, which goes through the librarian and the curator like any other change to the bundle. Change the site's values and options in `site.config.mjs`, and its look in `src/styles/custom.css`, which is this repository's own.

[^readme.md]: README.md, Documentation Website and the website item of Repository Structure
[^changelog.md]: CHANGELOG.md, the last item under Added
[^website-readme.md]: website/README.md, the list of page sources, Preview it and What to edit
[^site.config.mjs]: website/site.config.mjs, REPO, SITE, BASE, DOCS, REDIRECTS, CHANGELOG, SCHEMA and BROWSE
[^lychee.toml]: lychee.toml, the comment above the site's address in exclude

[^justfile]: justfile, the testdoc and _serve recipes
