---
type: Service
id: https://w3id.org/lmodel/oscal/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: "The Knowledge website workflow, .github/workflows/knowledge-website.yaml: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds website/ and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once KNOWLEDGE_WEBSITE_ENABLED is true."
resource: .github/workflows/knowledge-website.yaml
relatedTo:
  - https://w3id.org/lmodel/oscal/knowledge/services/documentation-site
sources:
  - id: knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
    title: the header comment, the on key and both jobs
  - id: notice
    resource: NOTICE
    title: the Knowledge bundle section
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:08:14Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

`.github/workflows/knowledge-website.yaml` is the workflow named "Knowledge website". It builds the site in `website/` and publishes the default branch's build to GitHub Pages.[^knowledge-website.yaml] NOTICE says that it derives from the ktl-website templates of the Knowledge Trust Ladder repository.[^notice]

It runs on a push or a pull request that touches the site, the bundle, the README, `docs/`, `.assets/`, the changelog, `.linkml/`, a schema under `src/*/schema/`, the workflow itself or the knowledge federation workflow. It also runs every Monday at 05:23 UTC and by hand. A header comment says that the weekly run rebuilds the site from the default branch, to catch what no push to those paths brings, such as the changelog's promotion, whose commit skips CI.

- **`build`**, named "Build the site (read-only)", runs with `contents: read`. A push builds on the default branch only, and a pull request or a dispatch always builds. It checks out the whole history, sets up uv, finds the site's folder, installs just when the site builds its data with it, and then runs the site's `scripts/build.sh`. That script runs `lokf export` and, for a LinkML schema, `gen-doc`, both from the toolkit `.lokf/uv.lock` pins. It then runs Hugo and Pagefind from the site's own `uv.lock`, cleans the raw HTML and checks the links. The job uploads the site's `dist/` as the Pages artifact.
- **`deploy`**, named "Deploy to GitHub Pages", holds `pages: write` and `id-token: write`, and runs only harden-runner and GitHub's own deploy-pages action. It runs for the default branch once the repository variable `KNOWLEDGE_WEBSITE_ENABLED` is `true`. Until then the workflow builds but deploys nothing.

A header comment says to tell Pages once to take its site from Actions before setting the variable, and to keep the variable unset while another publisher still deploys Pages, since two publishers overwrite each other's site. [oscal documentation site](../services/documentation-site.md) describes the site.

[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the header comment, the on key and both jobs
[^notice]: NOTICE, the Knowledge bundle section
