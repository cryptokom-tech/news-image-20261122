#!/usr/bin/env python3
"""Submission entry point for the news-image-20261122 bounty.

The repository ships one artifact: ``entry.png``, the final full-day
front page for Sunday 22 November 2026. This program does three things:

1. loads the bundled ``entry.png`` that sits next to this file,
2. proves it is a genuine 1024x1024 PNG under 1 MiB whose chunk
   structure ends cleanly with IEND,
3. copies it byte-for-byte to the submission output directory and
   reads the copy back, refusing to exit successfully unless the
   copy is identical to the bundle.

No network access, no third-party packages: standard library only.
Running the program twice always produces identical output bytes.
"""

import hashlib
import os
import struct
import sys

BUNDLE_FILENAME = "entry.png"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1024 * 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"


class BundleError(Exception):
    """Raised when the bundled image fails any validation check."""


def bundled_image_path():
    """Absolute path of the entry.png shipped beside this file."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, BUNDLE_FILENAME)


def destination_dir():
    """Output directory: $MAKEFUN_OUTPUT_DIR when set, else /output."""
    chosen = os.environ.get(OUTPUT_DIR_ENV, "").strip()
    return chosen or DEFAULT_OUTPUT_DIR


def inspect_png(blob):
    """Validate PNG bytes; return (width, height) or raise BundleError."""
    if len(blob) > MAX_BYTES:
        raise BundleError(
            "bundled image is %d bytes, over the %d-byte limit"
            % (len(blob), MAX_BYTES))
    if blob[:8] != PNG_SIGNATURE:
        raise BundleError("bundled file does not start with the PNG signature")
    offset = 8
    width = height = None
    saw_iend = False
    first_chunk = True
    while offset + 8 <= len(blob):
        (chunk_len,) = struct.unpack(">I", blob[offset:offset + 4])
        chunk_type = blob[offset + 4:offset + 8]
        data_start = offset + 8
        data_end = data_start + chunk_len
        if data_end + 4 > len(blob):
            raise BundleError(
                "chunk %r overruns the end of the file" % chunk_type)
        if first_chunk and chunk_type != b"IHDR":
            raise BundleError("first chunk is %r, expected IHDR" % chunk_type)
        first_chunk = False
        if chunk_type == b"IHDR":
            if chunk_len != 13:
                raise BundleError("IHDR chunk has an unexpected length")
            width, height = struct.unpack(">II", blob[data_start:data_start + 8])
        if chunk_type == b"IEND":
            if chunk_len != 0:
                raise BundleError("IEND chunk must be empty")
            (crc,) = struct.unpack(">I", blob[data_end:data_end + 4])
            if crc != 0xAE426082:
                raise BundleError("IEND chunk has a bad CRC")
            if data_end + 4 != len(blob):
                raise BundleError("trailing bytes found after the IEND chunk")
            saw_iend = True
            break
        offset = data_end + 4
    if width is None or height is None:
        raise BundleError("no IHDR chunk found in the bundled image")
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise BundleError(
            "bundled image is %dx%d, expected %dx%d"
            % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT))
    if not saw_iend:
        raise BundleError("bundled image has no terminating IEND chunk")
    return width, height


def sha256_hex(blob):
    return hashlib.sha256(blob).hexdigest()


def run():
    source = bundled_image_path()
    try:
        with open(source, "rb") as handle:
            blob = handle.read()
    except OSError as exc:
        raise BundleError("cannot read bundled image %s: %s" % (source, exc))
    width, height = inspect_png(blob)
    out_dir = destination_dir()
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, BUNDLE_FILENAME)
    with open(target, "wb") as handle:
        handle.write(blob)
        handle.flush()
        os.fsync(handle.fileno())
    with open(target, "rb") as handle:
        written = handle.read()
    if written != blob:
        raise BundleError(
            "output copy %s does not match the bundled image" % target)
    print("entry.png: %dx%d, %d bytes, sha256 %s"
          % (width, height, len(blob), sha256_hex(blob)))
    print("wrote %s (verified byte-identical to the bundle)" % target)
    return 0


def main(argv):
    try:
        return run()
    except BundleError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
