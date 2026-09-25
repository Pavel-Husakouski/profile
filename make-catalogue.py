#!/usr/bin/env python3
"""Render catalogue.generated.md from cv.md.

The catalogue is the long form of the resume, meant to be pasted into resume
builders field by field: same content, but every bullet block under
Professional Experience is announced with a "Key accomplishments" label, and
the contact line is broken out into a "Contacts" section of "Label: value"
rows. The resume itself drops the labels to save a page and keeps the contacts
on one line.

Usage: python3 make-catalogue.py [source.md] [output.md]
The output is generated: edit cv.md, never the catalogue.
"""
import re
import sys
from pathlib import Path

LABEL = "Key accomplishments:"
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
DATES = re.compile(r"((?:[A-Z][a-z]{2} \d{4})\s*[-–—]\s*(?:Present|[A-Z][a-z]{2} \d{4}))\s*$", re.I)


def plain(text):
    """Heading text without markdown: no bold markers, links as their label."""
    return LINK.sub(r"\1", text).replace("**", "").strip()


def contact_rows(line):
    """The one-line contact paragraph as labelled rows a builder can map."""
    rows = []
    for part in (p.strip() for p in line.split("\u00b7")):
        if not part:
            continue
        link = LINK.fullmatch(part)
        url = link.group(2) if link else ""
        text = link.group(1) if link else part
        if url.startswith("mailto:"):
            rows.append(("Email", url[len("mailto:"):]))
        elif "linkedin.com" in url:
            rows.append(("LinkedIn", url))
        elif "t.me" in url:
            rows.append(("Telegram", url))
        elif re.fullmatch(r"[+\d][\d()\s-]{6,}", text):
            rows.append(("Phone", text))
        elif "remote" in text.lower() or "office" in text.lower():
            rows.append(("Work format", text))
        else:
            rows.append(("Location", text))
    return rows


def header(lines):
    """Name, title, and contacts of cv.md as a Contacts block."""
    name = lines[0].lstrip("# ").strip()
    contacts = next(l for l in lines if "mailto:" in l)
    tagline = next(l for l in lines if l.startswith("**") and "mailto:" not in l)
    title, _, focus = plain(tagline).partition(" \u2014 ")
    rows = [("Name", name), ("Title", title.strip())]
    if focus:
        rows.append(("Focus", focus.strip()))
    rows += contact_rows(contacts)
    return ["Contacts:", ""] + [f"  {k}: {v}" for k, v in rows]


YEARS = re.compile(r"(\d{4}\s*[-–—]\s*\d{4}|\d{4})\s*\.?$")


def education_rows(line):
    """An Education line as fields: university, degree, field, years.

    cv.md keeps it as one sentence - "University. Degree, Field, Years" - so
    the university is taken up to the first full stop and the rest is split on
    commas, with a trailing year or year range recognised as the years.
    """
    text = plain(line).rstrip(".")
    years = YEARS.search(text)
    if years:
        text = text[: years.start()].rstrip().rstrip(",")
    university, _, rest = text.partition(". ")
    parts = [p.strip() for p in rest.split(",") if p.strip()]
    rows = [("University", university.strip())]
    for label, value in zip(("Degree", "Field"), parts):
        rows.append((label, value))
    rows += [("Note", p) for p in parts[2:]]
    if years:
        rows.append(("Years", years.group(1)))
    return rows


PROJECT_LINE = re.compile(r"\*\*Projects?:.*\*\*\s*$")


def split_heading(heading):
    """Heading text and its trailing date range, both plain."""
    text = plain(heading)
    dates = DATES.search(text)
    if dates:
        text = text[: dates.start()].rstrip().rstrip(",")
    return text, dates.group(1) if dates else ""


def render(md):
    """cv.md as an indented "Label: value" tree for a resume builder.

    Every section keeps its content one level in; a position is one level
    below its section, a project one below its position, and bullets one
    below the "Key accomplishments" label that announces them.
    """
    out, in_experience, depth, started, section = [], False, 1, False, ""

    def block(label, indent):
        out.append(f"{'  ' * indent}{label}")

    for line in md.splitlines():
        if not started:
            # the name, the tagline and the contact line live in the Contacts block
            if not line.startswith("## "):
                continue
            started = True
        if line.startswith("## "):
            section = line[3:].strip().lower()
            in_experience = "professional experience" in section
            out += ["", line[3:].strip() + ":", ""]
            depth = 1
        elif line.startswith("### "):
            text, dates = split_heading(line[4:])
            out.append("")
            block(f"Position: {text}", 1)
            if dates:
                block(f"Period: {dates}", 2)
            depth = 2
        elif PROJECT_LINE.match(line):
            # a project is written bold rather than as a heading: an ATS reads
            # a fourth-level heading unpredictably, a bold line always as text
            text, dates = split_heading(line.strip().strip("*"))
            block(f"Project: {re.sub(r'^Projects?:', '', text).strip()}", 2)
            if dates:
                block(f"Period: {dates}", 3)
            depth = 3
        elif line.startswith("- "):
            previous = next((x for x in reversed(out) if x.strip()), "")
            if in_experience and not previous.lstrip().startswith("- "):
                block(LABEL, depth)
            block(line, depth + 1 if in_experience else depth)
        elif line.strip() and section == "education":
            out += [f"  {k}: {v}" for k, v in education_rows(line)]
        elif line.strip():
            # the free line under a project heading is its one-sentence summary
            label = "Summary: " if in_experience and not line.startswith("**Stack") else ""
            block(label + plain(line), depth)
        elif out and out[-1].strip():
            out.append("")

    text = "\n".join(line.replace("**", "").rstrip() for line in out)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def main():
    src = Path(sys.argv[1] if len(sys.argv) > 1 else "cv.md")
    out = Path(sys.argv[2] if len(sys.argv) > 2 else "catalogue.generated.md")
    md = src.read_text(encoding="utf-8")
    out.write_text("\n".join(header(md.splitlines())) + "\n\n" + render(md), encoding="utf-8")
    print(f"{out} written")


if __name__ == "__main__":
    main()
