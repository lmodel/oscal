---
type: Service
id: https://w3id.org/lmodel/oscal/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The Upstream watch workflow, .github/workflows/upstream-watch.yaml: every Monday at 07:00 UTC and by hand, its oscal-metaschema job runs scripts/check_upstream_release.py against usnistgov/OSCAL's releases and the pinned metaschema tree, and on a finding opens or updates the issue titled Upstream watch: OSCAL has changed."
resource: .github/workflows/upstream-watch.yaml
relatedTo:
  - https://w3id.org/lmodel/oscal/knowledge/datasets/metaschema-copy
  - https://w3id.org/lmodel/oscal/knowledge/playbooks/update-upstream-pins
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
    title: the header comment, the on key and the oscal-metaschema job
  - id: report-issue.sh
    resource: .github/scripts/report-issue.sh
    title: the issue body and the reuse of an open issue
  - resource: scripts/check_upstream_release.py
    title: the checks it makes
generated:
  by: process:ktl-librarian
  at: "2026-10-29T00:48:58Z"
  revision: 9682284a2e351227aebe66a0fe34180d933ad8f8
status: draft
---

# Upstream watch (upstream-watch.yaml)

`.github/workflows/upstream-watch.yaml` is the workflow named "Upstream watch". A header comment says that it checks weekly what the repository is built from but does not control: NIST's OSCAL releases.[^upstream-watch.yaml] Nothing in a pull request can change them, so it runs on a schedule: every Monday at 07:00 UTC, after the knowledge workflows, and by hand.

Its one job, `oscal-metaschema`, named "OSCAL metaschema copy is current and intact", runs on `ubuntu-latest` with `contents: read` and `issues: write`. It runs `scripts/check_upstream_release.py` with the job's token, using only Python's standard library, so the runner's Python is enough. The script compares `src/oscal/schema/metaschema/` with OSCAL's latest release and with the pinned tree. When the check fails, `.github/scripts/report-issue.sh` opens an issue titled "Upstream watch: OSCAL has changed", or comments on the open issue with that title. The body is the check's report, or a note that the check stopped before writing one, and a link to the run.[^report-issue.sh] So a weekly finding is one issue, and does not depend on anyone reading the run log.

[OSCAL metaschema copy](../datasets/metaschema-copy.md) says what the script compares, and [Move the upstream pins](../playbooks/update-upstream-pins.md) says what to do about the issue.

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml, the header comment, the on key and the oscal-metaschema job
[^report-issue.sh]: .github/scripts/report-issue.sh, the header comment and the body it writes
