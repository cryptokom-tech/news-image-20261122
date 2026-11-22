#!/usr/bin/env python3
"""news-image-20261122 entry: write the front-page image to the output.

The image (entry.png, 1024x1024) sums up Sunday 22 November 2026's
world news — the round 1 morning edition: 36 numbered stories from
six continents, a dotted world map with a numbered pin per story, and
a red banner naming the day. It was drawn by the build script in the
work session and is bundled here.

This program only copies the bundled image to the output path, after
checking the PNG signature, the IHDR dimensions, the 1 MiB size
limit and the IEND chunk, and confirming the written bytes match the
bundle. Standard library only, no network, and every run writes the
exact same bytes.
"""

import os
import struct
import sys

MAX_BYTES = 1_048_576
EXPECT_W, EXPECT_H = 1024, 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def read_bundle():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.png")
    with open(path, "rb") as fh:
        return fh.read()


def check_png(data):
    """Check magic, size, and IHDR dimensions; return (width, height)."""
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png too large: {len(data)} bytes")
    if data[:8] != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG file")
    if len(data) < 33 or data[12:16] != b"IHDR":
        raise SystemExit("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECT_W, EXPECT_H):
        raise SystemExit(f"unexpected size {width}x{height}")
    if b"IEND" not in data[-12:]:
        raise SystemExit("entry.png has no IEND chunk")
    return width, height


def main():
    data = read_bundle()
    width, height = check_png(data)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    with open(out_path, "wb") as fh:
        fh.write(data)
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != data:
        raise SystemExit("written bytes differ from the bundle")
    print(f"wrote {out_path} ({width}x{height}, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
