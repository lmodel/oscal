---
type: Playbook
id: https://w3id.org/lmodel/oscal/knowledge/playbooks/release
genre: how-to
title: Release the schema
description: How a releasing commit merged to main makes semantic-release promote CHANGELOG.md's Unreleased section, tag vX.Y.Z and publish a GitHub Release, then dispatch the Knowledge Release workflow once KNOWLEDGE_RELEASE_ENABLED is true; below 1.0.0 from a v0.0.0 baseline tag, with a breaking change as a minor bump, no file bumped and nothing published to PyPI.
resource: CONTRIBUTING.md
references:
  - https://w3id.org/lmodel/oscal/knowledge/workflows/semantic-release
  - https://w3id.org/lmodel/oscal/knowledge/workflows/knowledge-release
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Releasing (maintainers)
  - id: security.md
    resource: SECURITY.md
    title: What this repository releases and the settings not yet in force
  - id: pyproject.toml
    resource: pyproject.toml
    title: the versioning settings
  - id: changelog.md
    resource: CHANGELOG.md
    title: the paragraph on the v0.0.0 tag
  - id: releaserc.json
    resource: .releaserc.json
    title: the release rules and the release commit message
  - resource: .github/workflows/semantic-release.yml
    title: the header comment and both jobs
  - resource: .github/scripts/changelog-release.mjs
    title: the check, notes and promote commands
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:47:10Z"
  revision: 928ef231c9fe1766b5f38ad26ece260a7ab1d870
status: draft
---

# Release the schema

CONTRIBUTING.md's Releasing section and the [Semantic release](../workflows/semantic-release.md) workflow say how a release is made.[^contributing.md] The release tags, `vX.Y.Z`, number the schema's versions, and no file is bumped. SECURITY.md says that the repository releases a LinkML schema, the Python datamodel generated from it, and the schema's `lokf adapt` copy as a release asset, and that nothing is published to PyPI.[^security.md] The package `oscal` takes its version from git through uv-dynamic-versioning, with `0.0.0` as the fallback.[^pyproject.toml]

## Before the first release

- Push the `v0.0.0` baseline tag on `main` before the first releasing merge, which then releases 0.1.0. Both release jobs refuse to run without a `v*` tag, because semantic-release would otherwise start at 1.0.0. CHANGELOG.md calls `v0.0.0` a baseline, not a release.[^changelog.md]
- Configure required reviewers on the `release` GitHub Environment in the repository's settings, or every qualifying merge is released unattended. SECURITY.md says that this setting is not yet in force.
- Leave off any branch rule that requires pull requests, status checks or signed commits on `main`, because it would reject the release job's own push to `main`.

## For each change

1. Write the change under `## [Unreleased]` in CHANGELOG.md as you go. The release job refuses an empty section, through `node .github/scripts/changelog-release.mjs check`.
2. Type the commit with Conventional Commits for what the change is. Only `feat:`, `fix:`, `security:` and a breaking `!` start a release, and other types leave their entries for the next release that does. A pull request that would release must carry a releasing type in its title too, since a squash merge takes its subject from the title.
3. Merge to `main`. semantic-release retitles the section to `## [X.Y.Z] - YYYY-MM-DD`, commits CHANGELOG.md, tags `vX.Y.Z` and publishes the GitHub Release. Once the repository variable `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches [Knowledge Release](../workflows/knowledge-release.md), which attaches the schema copy and the bundle when the bundle changed. Run that workflow by hand with `force` when only the schema changed.

## Staying below 1.0.0

`.releaserc.json` maps a breaking change to a minor release and a `security` commit to a patch release.[^releaserc.json] So the schema stays in 0.x until someone removes the first rule, which CONTRIBUTING.md asks to be done in a pull request of its own. The release commit's message is `chore(release): ${nextRelease.version} - changelog promoted [skip ci]`, so the commit skips CI.

[^contributing.md]: CONTRIBUTING.md, Releasing (maintainers)
[^security.md]: SECURITY.md, What this repository releases and the paragraph after the table
[^pyproject.toml]: pyproject.toml, the tool.hatch.version and tool.uv-dynamic-versioning settings
[^changelog.md]: CHANGELOG.md, the paragraph on the v0.0.0 tag
[^releaserc.json]: .releaserc.json, releaseRules and the git plugin's message
