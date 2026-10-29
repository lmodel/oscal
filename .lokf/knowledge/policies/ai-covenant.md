---
type: Policy
id: https://w3id.org/lmodel/oscal/knowledge/policies/ai-covenant
genre: reference
title: AI covenant
description: "The rules for AI-assisted work in oscal: a contributor owns what they submit; every element says what OSCAL's metaschema says at the pinned release and each enum names its lists in oscal_allowed_values; the metaschema copy is never edited; everything the schema defines lives under oscal:; and the scheduled librarian works through pull requests a person approves, with least privilege."
resource: AI_COVENANT.md
references:
  - https://w3id.org/lmodel/oscal/knowledge/workflows/knowledge-librarian
  - https://w3id.org/lmodel/oscal/knowledge/datasets/metaschema-copy
sources:
  - id: ai_covenant.md
    resource: AI_COVENANT.md
    title: every section
  - resource: CONTRIBUTING.md
    title: Using AI tools
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:47:10Z"
  revision: 928ef231c9fe1766b5f38ad26ece260a7ab1d870
status: draft
---

# AI covenant

`AI_COVENANT.md` sets the norms for AI-assisted work in `https://github.com/lmodel/oscal`.[^ai_covenant.md] Its core principle is that everything a contributor submits is theirs, whatever tools helped. The contributor must understand it, verify that it is correct and appropriate, defend and explain their choices in review, and make sure it meets the project's standards. CONTRIBUTING.md adds that a claim about what OSCAL defines must be checked against its metaschema.

## The rules specific to this project

The covenant says that this repository models someone else's standard. NIST defines what an OSCAL catalog, profile, system security plan or assessment result may say, in the metaschema of each release, and this project renders those definitions as a LinkML schema. That makes one failure mode worse here than elsewhere: a field, value or rule that a model produced, presented as what OSCAL says. So:

- an element says what OSCAL says. Every class, slot and enum under `src/oscal/schema/` renders a definition in OSCAL's metaschema at the pinned release, and each enum names in `oscal_allowed_values` the lists it renders. A pull request cites the definition, and never gives an OSCAL term a meaning its source does not carry;
- the metaschema copy is upstream text. `src/oscal/schema/metaschema/` holds OSCAL's files as published at the pinned release, with NIST's licence. Never edit them: replace them from one release, and `upstream-watch.yaml` checks that they still match. See [OSCAL metaschema copy](../datasets/metaschema-copy.md);
- the namespace is this project's. Everything the schema defines lives under `oscal:`, which is `https://w3id.org/lmodel/oscal/`, and OSCAL's own names, such as property names and link relations, appear only as values the schema documents.

## Reviews and agents

AI review comments are automated quality checks, not human reviews, and a pull request still needs a person's approval. AI tools may help a person prepare for a discussion, but must not be used to post comments, replies or messages directly in GitHub issues or discussions, shared Slack channels, or the project's mailing lists or email threads.

The scheduled agent that [Knowledge Librarian](../workflows/knowledge-librarian.md) runs commits as `knowledge-librarian[bot]` or as the maintainer who ran it interactively, never both, and its commits carry no AI co-authorship trailer. Every change it proposes arrives as a pull request that a maintainer approves. It runs in a read-only job with no git credentials on disk and hands its change to a privileged job that runs no agent code, and its contract to edit only `.lokf/knowledge/` is checked after it runs. A skill that records a person's judgment writes only what that person said about that item, in that session.

## Disclosure

Disclosure is required for a fix to code that the contributor does not fully understand, and for an element under `src/oscal/schema/` that an AI drafted, together with the OSCAL definition it rests on. Whoever drafted it, a change to an element cites the OSCAL definition it renders. Routine AI use needs no disclosure, and AI co-authorship in commit messages is actively discouraged. The covenant says that it is adapted from the Knowledge Trust Ladder AI Covenant, which is adapted from LinkML's.

[^ai_covenant.md]: AI_COVENANT.md, every section
