#!/usr/bin/env python3
"""Render cv.md to a .docx that applicant tracking systems can read.

Usage: python3 make-docx.py [source.md] [output.docx]

The document is deliberately plain: real heading styles so a parser can find
the sections, plain bullet lists, no columns, no tables, no text boxes. The
typography is folded to ASCII the same way make-pdf.py does it, because some
parsers turn em dashes and middots into mush. Links stay plain text: a parser
reads the text, and nobody reads a .docx by hand - that is what the PDF is for.

No third-party libraries: a .docx is a zip of XML parts, and the handful of
parts below is all Word needs.
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

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'


def _style(sid, name, size_half_pt, bold, outline=None, space_before=120):
    outline_xml = f'<w:outlineLvl w:val="{outline}"/>' if outline is not None else ""
    return (
        f'<w:style w:type="paragraph" w:styleId="{sid}"><w:name w:val="{name}"/>'
        f'<w:basedOn w:val="Normal"/><w:qFormat/>'
        f'<w:pPr><w:spacing w:before="{space_before}" w:after="40"/>{outline_xml}</w:pPr>'
        f'<w:rPr><w:b w:val="{"1" if bold else "0"}"/><w:sz w:val="{size_half_pt}"/></w:rPr></w:style>'
    )


STYLES = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles {W}>
<w:docDefaults><w:rPrDefault><w:rPr>
<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="20"/>
</w:rPr></w:rPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:styleId="Normal" w:default="1"><w:name w:val="Normal"/>
<w:pPr><w:spacing w:after="60"/></w:pPr></w:style>
{_style("Title", "Title", 40, True, space_before=0)}
{_style("Heading1", "heading 1", 26, True, outline=0)}
{_style("Heading2", "heading 2", 24, True, outline=1)}
{_style("Heading3", "heading 3", 22, True, outline=2)}
<w:style w:type="paragraph" w:styleId="ListParagraph"><w:name w:val="List Paragraph"/>
<w:basedOn w:val="Normal"/><w:qFormat/>
<w:pPr><w:ind w:left="360" w:hanging="180"/><w:spacing w:after="40"/></w:pPr></w:style>
</w:styles>"""

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
    src = Path(args[0] if args else "cv.md")
    out = Path(args[1] if len(args) > 1 else "Pavel Husakouski - CV.docx")

    md = to_ascii(src.read_text(encoding="utf-8"))

    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)
        z.writestr("word/styles.xml", STYLES)
        z.writestr("word/document.xml", convert(md))
    print(f"{out} written")


if __name__ == "__main__":
    main()
