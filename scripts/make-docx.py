#!/usr/bin/env python3
"""Render a CV markdown file to a .docx that applicant tracking systems can read.

Usage: python3 make-docx.py <source.md> <output.docx>

The document is deliberately plain: real heading styles so a parser can find
the sections, plain bullet lists, no columns, no tables, no text boxes. The
typography is folded to ASCII the same way make-pdf.py does it, because some
parsers turn em dashes and middots into mush. Links stay plain text: a parser
reads the text, and nobody reads a .docx by hand - that is what the PDF is for.

No third-party libraries: a .docx is a zip of XML parts, and the handful of
parts in docx/ next to this script is all Word needs - styles.xml holds the
typography, the rest is package boilerplate.
"""
import importlib.util
import re
import sys
import zipfile
from pathlib import Path

# make-pdf.py cannot be imported by name (the dash), so it is loaded by path.
_spec = importlib.util.spec_from_file_location("make_pdf", Path(__file__).with_name("make-pdf.py"))
_make_pdf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_make_pdf)
to_ascii = _make_pdf.to_ascii

# The static parts of the package live in docx/ next to this script, one file
# per entry of the zip; only word/document.xml is generated per run.
PARTS = Path(__file__).with_name("docx")
PART_FILES = {
    "[Content_Types].xml": "content-types.xml",
    "_rels/.rels": "package.rels.xml",
    "word/_rels/document.xml.rels": "document.rels.xml",
    "word/styles.xml": "styles.xml",
}
W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'

LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD = re.compile(r"\*\*([^*]+)\*\*")
CODE = re.compile(r"`([^`]+)`")


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def runs(text):
    """Markdown inline to <w:r> runs; only bold survives, the rest goes plain."""
    text = LINK.sub(r"\1", text)
    text = CODE.sub(r"\1", text)
    out = []
    for i, chunk in enumerate(BOLD.split(text)):
        if not chunk:
            continue
        bold = '<w:rPr><w:b/></w:rPr>' if i % 2 else ""
        out.append(f'<w:r>{bold}<w:t xml:space="preserve">{esc(chunk)}</w:t></w:r>')
    return "".join(out)


def para(text, style=None, bullet=False):
    """A bullet is written as a literal "- ": Word's own numbering lives in
    numbering.xml, and a parser that only reads paragraph text sees no marker
    at all - the same reason make-pdf.py stopped using CSS ::marker."""
    props = f'<w:pStyle w:val="{style}"/>' if style else ""
    props = f"<w:pPr>{props}</w:pPr>" if props else ""
    return f"<w:p>{props}{runs('- ' + text if bullet else text)}</w:p>"


HEADING_STYLE = {1: "Title", 2: "Heading1", 3: "Heading2", 4: "Heading3"}


def convert(md):
    body = []
    for line in md.splitlines():
        line = line.rstrip()
        if not line or line.startswith("---"):
            continue
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            body.append(para(line[level:].strip(), HEADING_STYLE.get(level, "Heading3")))
        elif line.startswith("- "):
            body.append(para(line[2:], "ListParagraph", bullet=True))
        elif line.startswith("> "):
            body.append(para(line[2:]))
        else:
            body.append(para(line))
    return (
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:document {W}><w:body>'
        + "".join(body)
        + '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="720" w:right="900" w:bottom="720" w:left="900"/></w:sectPr>'
        "</w:body></w:document>"
    )


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        sys.exit("usage: make-docx.py <source.md> <output.docx>")
    src, out = Path(args[0]), Path(args[1])

    md = to_ascii(src.read_text(encoding="utf-8"))

    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for part, source in PART_FILES.items():
            z.writestr(part, (PARTS / source).read_text(encoding="utf-8"))
        z.writestr("word/document.xml", convert(md))
    print(f"{out} written")


if __name__ == "__main__":
    main()
