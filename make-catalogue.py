#!/usr/bin/env python3
"""Render catalogue.md from cv.md.

The catalogue is the long form of the resume: same content, but every bullet
block under Professional Experience is announced with a "Key accomplishments"
label. The resume itself drops those labels to save a page.

Usage: python3 make-catalogue.py [source.md] [output.md]
"""
import sys
from pathlib import Path

LABEL = "**Key accomplishments**"


def render(md):
    lines = md.splitlines()
    out, in_experience = [], False
    for i, line in enumerate(lines):
        if line.startswith("## "):
            in_experience = "professional experience" in line.lower()
        starts_block = line.startswith("- ") and not (out and out[-1].startswith("- "))
        if in_experience and starts_block:
            previous = next((x for x in reversed(out) if x.strip()), "")
            # a block that already announces itself keeps its own wording,
            # bold or plain ("Selected accomplishments over the twelve years:")
            if "accomplishments" not in previous.lower():
                out += [LABEL, ""]
        out.append(line)
    return "\n".join(out) + "\n"


def main():
    src = Path(sys.argv[1] if len(sys.argv) > 1 else "cv.md")
    out = Path(sys.argv[2] if len(sys.argv) > 2 else "catalogue.md")
    out.write_text(render(src.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"{out} written")


if __name__ == "__main__":
    main()
