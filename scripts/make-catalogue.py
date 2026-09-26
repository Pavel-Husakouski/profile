#!/usr/bin/env python3
"""Render the catalogue form of a CV markdown file.

The catalogue is the long form of the resume, meant to be pasted into resume
builders field by field: same content, but every bullet block under
Professional Experience is announced with a "Key accomplishments" label, and
the contacts - which come from .env, not from the markdown - are written out as
a "Contacts" section of "Label: value" rows. The resume itself drops the labels
to save a page and keeps the contacts on one line.

Usage: python3 make-catalogue.py <source.md> <output.md> [lang]

The output is generated: edit the CV, never the catalogue. The language (en by
default, ru for cv-ru.md) picks the date, project and education patterns.
"""
import re
import sys
from pathlib import Path

import contacts

LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

RU_MONTH = r"(?:янв|фев|март|апр|май|июн[ья]|июл[ья]|авг|сент|окт|нояб|дек)\.?"

# Everything language-dependent in one place: the labels the catalogue writes,
# the section names it recognises in the source, and the date/project shapes.
LANGS = {
    "en": {
        "month": r"[A-Z][a-z]{2} \d{4}",
        "present": "Present",
        "projects": r"Projects?:",
        "experience": "professional experience",
        "education": "education",
        "labels": {
            "accomplishments": "Key accomplishments:",
            "contacts": "Contacts:", "name": "Name", "title": "Title", "focus": "Focus",
            "email": "Email", "linkedin": "LinkedIn", "telegram": "Telegram",
            "phone": "Phone", "format": "Work format", "location": "Location",
            "position": "Position", "period": "Period", "project": "Project",
            "summary": "Summary: ",
            "university": "University", "degree": "Degree", "field": "Field",
            "note": "Note", "years": "Years",
        },
    },
    "ru": {
        "month": rf"(?:{RU_MONTH} )?\d{{4}}",
        "present": r"наст\.? время",
        "projects": r"Проекты?:",
        "experience": "опыт работы",
        "education": "образование",
        "labels": {
            "accomplishments": "Ключевые достижения:",
            "contacts": "Контакты:", "name": "Имя", "title": "Должность", "focus": "Специализация",
            "email": "Email", "linkedin": "LinkedIn", "telegram": "Telegram",
            "phone": "Телефон", "format": "Формат работы", "location": "Город",
            "position": "Должность", "period": "Период", "project": "Проект",
            "summary": "Кратко: ",
            "university": "Университет", "degree": "Степень", "field": "Специальность",
            "note": "Примечание", "years": "Годы",
        },
    },
}

LANG = LANGS["en"]
LABEL = LANG["labels"]["accomplishments"]
DATES = re.compile(rf"((?:{LANG['month']})\s*[-–—]\s*(?:{LANG['present']}|{LANG['month']}))\s*$", re.I)
PROJECT_LINE = re.compile(rf"\*\*{LANG['projects']}.*\*\*\s*$")


def set_language(lang):
    """Point the module at one language's labels and patterns."""
    global LANG, LABEL, DATES, PROJECT_LINE
    LANG = LANGS.get(lang, LANGS["en"])
    LABEL = LANG["labels"]["accomplishments"]
    DATES = re.compile(
        rf"((?:{LANG['month']})\s*[-–—]\s*(?:{LANG['present']}|{LANG['month']}))\s*$", re.I
    )
    PROJECT_LINE = re.compile(rf"\*\*{LANG['projects']}.*\*\*\s*$")


def label(key):
    return LANG["labels"][key]


def plain(text):
    """Heading text without markdown: no bold markers, links as their label."""
    return LINK.sub(r"\1", text).replace("**", "").strip()


def header(lines, lang):
    """Name, title, and contacts of cv.md as a Contacts block. The name and the
    tagline are read off the top of the CV, the rest comes from .env."""
    name = lines[0].lstrip("# ").strip()
    tagline = next(l for l in lines if l.startswith("**") and "mailto:" not in l)
    title, _, focus = plain(tagline).partition(" \u2014 ")
    rows = [(label("name"), name), (label("title"), title.strip())]
    if focus:
        rows.append((label("focus"), focus.strip()))
    rows += [(label(key), value) for key, value in contacts.rows(lang)]
    return [label("contacts"), ""] + [f"  {k}: {v}" for k, v in rows]


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
    rows = [(label("university"), university.strip())]
    for key, value in zip(("degree", "field"), parts):
        rows.append((label(key), value))
    rows += [(label("note"), p) for p in parts[2:]]
    if years:
        rows.append((label("years"), years.group(1)))
    return rows


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
            in_experience = LANG["experience"] in section
            out += ["", line[3:].strip() + ":", ""]
            depth = 1
        elif line.startswith("### "):
            text, dates = split_heading(line[4:])
            out.append("")
            block(f"{label('position')}: {text}", 1)
            if dates:
                block(f"{label('period')}: {dates}", 2)
            depth = 2
        elif PROJECT_LINE.match(line):
            # a project is written bold rather than as a heading: an ATS reads
            # a fourth-level heading unpredictably, a bold line always as text
            text, dates = split_heading(line.strip().strip("*"))
            block(f"{label('project')}: {re.sub(LANG['projects'], '', text, count=1).strip()}", 2)
            if dates:
                block(f"{label('period')}: {dates}", 3)
            depth = 3
        elif line.startswith("- "):
            previous = next((x for x in reversed(out) if x.strip()), "")
            if in_experience and not previous.lstrip().startswith("- "):
                block(LABEL, depth)
            block(line, depth + 1 if in_experience else depth)
        elif line.strip() and section == LANG["education"]:
            out += [f"  {k}: {v}" for k, v in education_rows(line)]
        elif line.strip():
            # the free line under a project heading is its one-sentence summary
            prefix = label("summary") if in_experience and not line.startswith("**Stack") else ""
            block(prefix + plain(line), depth)
        elif out and out[-1].strip():
            out.append("")

    text = "\n".join(line.replace("**", "").rstrip() for line in out)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        sys.exit("usage: make-catalogue.py <source.md> <output.md> [lang]")
    src, out = Path(args[0]), Path(args[1])
    lang = args[2] if len(args) > 2 else "en"
    set_language(lang)
    md = contacts.expand(src.read_text(encoding="utf-8"), lang)
    out.write_text("\n".join(header(md.splitlines(), lang)) + "\n\n" + render(md), encoding="utf-8")
    print(f"{out} written")


if __name__ == "__main__":
    main()
