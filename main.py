#!/usr/bin/env python3
"""news-image-20261124 -- copy the pre-rendered front page to the output dir.

The 1024x1024 PNG for Tuesday 24 November 2026 ("THE WORLD IN ONE DAY":
25 stories -- 3 big illustrated stories, a numbered world map, a
22-item list, a KPI strip and a DATE CHECK box) is drawn at build time
by render.py in the build directory. This entrypoint only copies it to
/output/entry.png: no network, and the same bytes on every run.
"""
import os
import shutil
import struct

LIMIT = 1_048_576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def read_dimensions(path):
    with open(path, "rb") as handle:
        head = handle.read(33)
    if head[:8] != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG file")
    if head[12:16] != b"IHDR":
        raise SystemExit("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def main():
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(dest_dir, exist_ok=True)
    base = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(dest_dir, "entry.png")
    shutil.copyfile(os.path.join(base, "entry.png"), target)
    width, height = read_dimensions(target)
    if width > 1024 or height > 1024:
        os.remove(target)
        raise SystemExit("entry.png is larger than 1024x1024")
    if os.path.getsize(target) > LIMIT:
        os.remove(target)
        raise SystemExit("entry.png is larger than 1 MiB")


if __name__ == "__main__":
    main()
