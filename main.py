#!/usr/bin/env python3
"""Entrypoint for the news-image-20261126 entry.

Copies the pre-rendered 26 November 2026 world-news summary image
(entry.png, shipped in this repository) to the grader's output directory
as entry.png. No network, no randomness: the output bytes are identical
on every run.
"""

import hashlib
import os
import shutil
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"
MAX_BYTES = 1048576
MAX_PIXELS = 1024


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    with open(source, "rb") as f:
        data = f.read()
    # Gate: the file must be a whole PNG or JPEG inside the size cap.
    if not (data[:8] == PNG_MAGIC or data[:3] == JPEG_MAGIC):
        print("entry.png is not a PNG or JPEG", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print("entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(here, "out")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)
    with open(dest, "rb") as f:
        if hashlib.sha256(f.read()).hexdigest() != hashlib.sha256(data).hexdigest():
            print("output copy mismatch", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
