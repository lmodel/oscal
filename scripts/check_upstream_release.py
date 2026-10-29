#!/usr/bin/env python3
"""Check the OSCAL metaschema copy against NIST's OSCAL releases.

Two things can go wrong with ``src/oscal/schema/metaschema/`` without any
change in this repository:

- NIST releases a newer OSCAL version, so the schema falls behind;
- the copied files drift from the tree they were taken from.

The copy has no version in its path, so the release and the commit it was
taken from are pinned below. This script asks the GitHub API for
usnistgov/OSCAL's latest release and for the pinned tree, and compares every
copied file with its blob there by git object hash, so nothing is downloaded
but two listings. It prints a Markdown report and exits 1 when a newer
release is out or a file differs.

Set ``GITHUB_TOKEN`` to raise the API rate limit. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPY = ROOT / "src" / "oscal" / "schema" / "metaschema"
API = "https://api.github.com/repos/usnistgov/OSCAL"

# The release and the commit its tag names. Move all three together when the
# copy is replaced from a newer release, with the schema header's version,
# source and annotations.
PINNED_TAG = "v1.2.3"
PINNED_COMMIT = "e061961c7702afeabffdf5e59894d35e748dade1"
PINNED_PATH = "src/metaschema"

# Copied files that come from elsewhere in the pinned tree than PINNED_PATH.
ELSEWHERE = {"LICENSE.md": "LICENSE.md"}


def _get(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "lmodel-oscal-upstream-check",
        },
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def _version_key(tag: str) -> tuple[int, ...]:
    """Numeric parts of a tag, padded so that v1.2 and v1.2.0 order alike."""
    parts = [int(x) for x in re.findall(r"\d+", tag)]
    return tuple(parts + [0] * (4 - len(parts)))


def _blob_sha(path: Path) -> str:
    """The git object hash of a file, as the trees API reports it."""
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def check() -> tuple[list[str], bool]:
    """Return the report lines and whether anything needs attention."""
    report = [
        f"- Pinned release: OSCAL {PINNED_TAG}, commit `{PINNED_COMMIT[:12]}`, `{PINNED_PATH}/` "
        "copied to `src/oscal/schema/metaschema/`."
    ]
    attention = False

    latest = json.loads(_get(f"{API}/releases/latest"))["tag_name"]
    if _version_key(latest) > _version_key(PINNED_TAG):
        attention = True
        report.append(
            f"- **NIST has released OSCAL {latest}.** Replace `src/oscal/schema/metaschema/` with "
            f"`{PINNED_PATH}/` at that tag (https://github.com/usnistgov/OSCAL/tree/{latest}/{PINNED_PATH}), "
            "move the pins in `scripts/check_upstream_release.py` and the schema header, run "
            "`just test`, and update every enum `tests/test_schema_rules.py` reports."
        )
    else:
        report.append(f"- Latest release: {latest}, the pinned one.")

    tree = json.loads(_get(f"{API}/git/trees/{PINNED_COMMIT}?recursive=1"))
    if tree.get("truncated"):
        return report + [
            "- The pinned tree listing came back truncated; compare the copy by hand."
        ], True
    upstream = {e["path"]: e["sha"] for e in tree["tree"] if e["type"] == "blob"}

    files = sorted(p for p in COPY.rglob("*") if p.is_file())
    matching, differing = 0, []
    for path in files:
        rel = path.relative_to(COPY).as_posix()
        source = ELSEWHERE.get(rel, f"{PINNED_PATH}/{rel}")
        if upstream.get(source) == _blob_sha(path):
            matching += 1
        elif source in upstream:
            differing.append(f"`{rel}` differs from `{source}` at {PINNED_TAG}")
        else:
            differing.append(f"`{rel}` has no `{source}` at {PINNED_TAG}")
    report.append(
        f"- {matching} of {len(files)} copied files match the pinned tree byte for byte."
    )
    if differing:
        attention = True
        report.append(
            f"- **{len(differing)} copied file(s) differ from the pinned tree:**"
        )
        report += [f"  - {d}" for d in differing]
    return report, attention


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines, attention = check()
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
