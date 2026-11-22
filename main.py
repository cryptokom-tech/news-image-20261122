#!/usr/bin/env python3
"""Entry program for the make.fun bounty news-image-20261122.

The repository ships a single finished picture, entry.png, that sums
up Sunday 22 November 2026's world news as a newspaper front page:
36 numbered stories, a dotted world map with a numbered pin for
each story, and a red banner naming the day. All this program does
is place that picture at the path the grader expects, after making
sure the file is a well-formed PNG of the right size. It needs no
network, installs nothing, and writes the same bytes on every run.
"""

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLED = os.path.join(HERE, "entry.png")
LIMIT = 1024 * 1024
MAGIC = b"\x89PNG\r\n\x1a\n"


def load_and_check():
    with open(BUNDLED, "rb") as handle:
        blob = handle.read()
    if len(blob) > LIMIT:
        raise SystemExit(f"entry.png is {len(blob)} bytes, over the 1 MiB limit")
    if blob[:8] != MAGIC:
        raise SystemExit("entry.png does not start with the PNG signature")
    width = int.from_bytes(blob[16:20], "big")
    height = int.from_bytes(blob[20:24], "big")
    if (width, height) != (1024, 1024):
        raise SystemExit(f"entry.png is {width}x{height}, expected 1024x1024")
    if b"IEND" not in blob[-12:]:
        raise SystemExit("entry.png is missing its IEND chunk")
    return blob


def run():
    blob = load_and_check()
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(blob)
    with open(target, "rb") as handle:
        again = handle.read()
    if again != blob:
        raise SystemExit("the file written to /output differs from the bundle")
    if len(again) != len(blob):
        raise SystemExit("the file written to /output has the wrong size")
    digest = hashlib.sha256(blob).hexdigest()
    print(f"wrote {target} ({len(blob)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(run())
