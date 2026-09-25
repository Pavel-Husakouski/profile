#!/usr/bin/env python3
"""Render cv.md to a print-ready, ATS-friendly PDF via Chrome headless.

Usage: python3 make-pdf.py [source.md] [output.pdf]

The output is the copy that goes into applicant tracking systems, so the
typography is folded to ASCII (em dash, en dash, middot, curly quotes,
trademark) - some parsers turn those characters into mush and glue the
neighbouring words together - and the contact line shows the raw address and
URL while staying clickable.

Layout knobs are the CSS constants below: PAGE_MARGIN, BASE_PT, LEADING.
Shrink BASE_PT by 0.25pt steps to pull the document onto two pages.
"""
import html
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PAGE_SIZE = "A4"
PAGE_MARGIN = "8mm 16mm"
BASE_PT = 8.7
LEADING = 1.3

def css(base_pt=BASE_PT, leading=LEADING, page_size=PAGE_SIZE, page_margin=PAGE_MARGIN):
    """The whole stylesheet; base_pt is the knob that pulls the document onto two pages."""
    return f"""
@page {{ size: {page_size}; margin: {page_margin}; }}
* {{ box-sizing: border-box; }}
body {{
  font-family: "Noto Sans", "Liberation Sans", Arial, sans-serif;
  font-size: {base_pt}pt; line-height: {leading}; color: #14181f;
  margin: 0; -webkit-print-color-adjust: exact;
}}
h1 {{ font-size: 19pt; margin: 0 0 2pt; font-weight: 650; }}
.tagline {{ font-size: 10.5pt; font-weight: 600; color: #1f2a3a; margin: 0 0 1pt; }}
.tagline em {{ font-weight: 500; font-style: normal; color: #55606f; }}
.contact {{ font-size: 8.6pt; color: #55606f; margin: 0 0 9pt; }}
h2 {{
  font-size: 9.5pt; text-transform: uppercase; font-weight: 700;
  color: #1f2a3a; border-bottom: 0.6pt solid #c4ccd6;
  margin: 10pt 0 4pt; padding-bottom: 1.5pt;
}}
h3 {{ font-size: 10.6pt; font-weight: 650; margin: 7pt 0 0; }}
h4, .project {{ font-size: 9.8pt; font-weight: 650; margin: 5pt 0 0; color: #22303f; }}
h1, h2, h3, h4, .project {{ break-after: avoid; page-break-after: avoid; }}
p {{ margin: 1.5pt 0 3pt; }}
.when {{ float: right; font-size: 8.8pt; font-weight: 500; color: #55606f; }}
h3, h4, .project {{ overflow: hidden; }}
ul {{ margin: 2pt 0 4pt; padding-left: 0; list-style: none; }}
li {{ margin: 0 0 2.2pt; padding-left: 7pt; text-indent: -7pt;
     break-inside: avoid; page-break-inside: avoid; }}
a {{ color: inherit; text-decoration: none; }}
strong {{ font-weight: 650; }}
blockquote {{ margin: 0 0 6pt; color: #55606f; font-style: italic; }}
hr {{ border: 0; border-top: 0.6pt solid #d6dce4; margin: 8pt 0; }}
.stack {{ font-size: 9.2pt; color: #3c4654; }}
"""

ASCII_MAP = {
    "\u2014": "-", "\u2013": "-", "\u00b7": "|", "\u2122": "",
    "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
    "\u2026": "...", "\u00a0": " ", "\u2212": "-",
}
CONTACT_LINK = re.compile(r"\[([^\]]+)\]\((mailto:([^)]+)|https?://[^)]+)\)")


def to_ascii(md):
    """Fold typography to ASCII and flatten the contact line's links."""
    out = []
    for line in md.splitlines():
        if "mailto:" in line:
            # Keep the links clickable, but show the address itself: a PDF
            # parser reads the visible text and never sees the href.
            line = CONTACT_LINK.sub(
                lambda m: "[{}]({})".format(
                    m.group(3) or re.sub(r"^https?://(?:www\.)?", "", m.group(2)).rstrip("/"),
                    m.group(2),
                ),
                line,
            )
        for src, dst in ASCII_MAP.items():
            line = line.replace(src, dst)
        out.append(re.sub(r" {2,}", " ", line))
    return "\n".join(out)


INLINE = (
    (re.compile(r"\[([^\]]+)\]\(([^)]+)\)"), r'<a href="\2">\1</a>'),
    (re.compile(r"\*\*([^*]+)\*\*"), r"<strong>\1</strong>"),
    (re.compile(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])"), r"<em>\1</em>"),
    (re.compile(r"`([^`]+)`"), r"<code>\1</code>"),
)


def inline(text):
    out = html.escape(text, quote=False)
    for pattern, repl in INLINE:
        out = pattern.sub(repl, out)
    return out


DATE = r"(?:[A-Z][a-z]{2} \d{4}|\d{2}\.\d{4})"
DATE_LINE = re.compile(rf"\*\*\s*{DATE}\s*[–-]\s*(?:present|{DATE})\s*\*\*", re.I)
LABEL_ONLY = re.compile(r"\*\*[^*]*accomplishments[^*]*:\*\*\s*$", re.I)
# a project is a bold line, not a heading: an ATS reads a fourth-level heading
# unpredictably, a bold line always as text
PROJECT_LINE = re.compile(r"\*\*(Projects?:.*)\*\*\s*$")


def convert(md):
    """Markdown to HTML, with two presentation-only compressions:
    a date line following a heading is pulled into that heading, and the
    bare "Key accomplishments:" labels are dropped - the bullets under a
    project heading need no announcement."""
    lines = [ln.rstrip() for ln in md.splitlines()]
    body, in_list, i = [], False, 0

    def close_list():
        nonlocal in_list
        if in_list:
            body.append("</ul>")
            in_list = False

    while i < len(lines):
        line = lines[i]
        i += 1
        if not line.strip():
            close_list()
            continue
        if line.startswith("- "):
            if not in_list:
                body.append("<ul>")
                in_list = True
            # The marker is written as text: a CSS ::marker is drawn past the
            # text layer, so resume parsers see the bullets as plain paragraphs.
            body.append(f"<li>- {inline(line[2:])}</li>")
            continue
        close_list()
        project = PROJECT_LINE.match(line.strip())
        if line.startswith("#") or project:
            level = len(line) - len(line.lstrip("#"))
            raw_heading = project.group(1) if project else line[level:].strip()
            # "Project: X, 1M+ users - 10.2023 - present" -> title, right-aligned dates
            # The separator before the date may be a comma or a dash; either way
            # the date is lifted out of the heading and floated to the right.
            tail = re.search(
                rf"\s*[,\u2014-]\s+\*{{0,2}}({DATE}\s*[\u2013-]\s*(?:present|{DATE}))\*{{0,2}}$",
                raw_heading, re.I,
            )
            if tail:
                heading = inline(raw_heading[: tail.start()]) + f'<span class="when">{inline(tail.group(1))}</span>'
            else:
                heading = inline(raw_heading)
            nxt = next((lines[j] for j in range(i, len(lines)) if lines[j].strip()), "")
            if DATE_LINE.fullmatch(nxt.strip()):
                heading += f'<span class="when">{inline(nxt.strip())}</span>'
                i = lines.index(nxt, i) + 1
            body.append(
                f'<p class="project">{heading}</p>' if project
                else f"<h{level}>{heading}</h{level}>"
            )
        elif LABEL_ONLY.match(line):
            continue
        elif line.startswith("> "):
            body.append(f"<blockquote>{inline(line[2:])}</blockquote>")
        elif line.startswith("---"):
            body.append("<hr>")
        else:
            text = inline(line)
            if "mailto:" in text:
                cls = "contact"
            elif text.startswith("<strong>Stack:</strong>"):
                cls = "stack"
            elif not any(x.startswith("<h2") for x in body) and text.startswith("<strong>"):
                cls = "tagline"
            else:
                cls = None
            body.append(f'<p class="{cls}">{text}</p>' if cls else f"<p>{text}</p>")
    close_list()
    return "\n".join(body)


def main():
    args = sys.argv[1:]
    src = Path(args[0] if args else "cv.md")
    out = Path(args[1] if len(args) > 1 else "Pavel Husakouski - Nodejs-backend-fullstack.pdf")
    chrome = shutil.which("google-chrome-stable") or shutil.which("chromium") or shutil.which("chrome")
    if not chrome:
        sys.exit("no Chrome binary found")

    source = to_ascii(src.read_text(encoding="utf-8"))

    page = (
        "<!doctype html><html><head><meta charset='utf-8'>"
        f"<title>{html.escape(src.stem)}</title><style>{css()}</style></head>"
        f"<body>{convert(source)}</body></html>"
    )

    with tempfile.TemporaryDirectory() as tmp:
        page_path = Path(tmp) / "cv.html"
        page_path.write_text(page, encoding="utf-8")
        subprocess.run(
            [chrome, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
             f"--print-to-pdf={out.resolve()}", page_path.as_uri()],
            check=True, capture_output=True,
        )
    print(f"{out} written")


if __name__ == "__main__":
    main()
