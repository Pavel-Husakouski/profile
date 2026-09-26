#!/usr/bin/env python3
"""The contact data of the CV: values in .env, placeholders in the markdown.

cv-en.md and cv-ru.md carry no personal data but the name in their heading -
the contact line is written out placeholder by placeholder:

    [{{EMAIL}}](mailto:{{EMAIL}}) - [LinkedIn]({{LINKEDIN}}) - {{PHONE}} ...

so the sources stay shareable while the layout of the line - which link carries
which label, what separates the parts, in what order they run - stays visible in
the markdown where it is edited. The values live in .env, which git does not
track, and every generator expands the placeholders before it does anything
else.

The placeholders: NAME, EMAIL, PHONE, PHONE_TEL, LINKEDIN, TELEGRAM,
TELEGRAM_URL, LOCATION, FORMAT. A value is looked up under the language prefix
first and then bare, so NAME reads EN_NAME for the English CV and RU_NAME for the Russian one,
while EMAIL - the same in both - needs no prefix. The .env file wins over the
process environment: it is the one place the values are written down.
"""
import os
import re
import sys
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parent.parent / ".env"

PLACEHOLDER = re.compile(r"\{\{\s*([A-Z_]+)\s*\}\}")

# The contacts of the Contacts block of the catalogue, in the order it prints
# them, and the label key make-catalogue.py writes for each.
ROW_LABELS = {
    "EMAIL": "email", "LINKEDIN": "linkedin", "PHONE": "phone",
    "TELEGRAM_URL": "telegram", "LOCATION": "location", "FORMAT": "format",
}

_values = None


def env():
    """The .env file as a dict, falling back to the process environment."""
    global _values
    if _values is None:
        _values = dict(os.environ)
        if ENV_FILE.exists():
            for raw in ENV_FILE.read_text(encoding="utf-8").splitlines():
                line = raw.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                _values[key.strip()] = value.strip().strip('"').strip("'")
    return _values


# A placeholder derived from another one's .env key: the Telegram link and the
# dialable form of the phone read TELEGRAM and PHONE.
DERIVED = {"TELEGRAM_URL": "TELEGRAM", "PHONE_TEL": "PHONE"}


def source(key):
    """The .env key a placeholder reads."""
    return DERIVED.get(key, key)


def value(key, lang):
    """One placeholder's value: the language-prefixed .env key first, then the
    bare one. TELEGRAM is normalised to @handle and TELEGRAM_URL to its link, so
    .env may write either form, and PHONE_TEL strips the number down to what a
    tel: URI can carry."""
    values = env()
    for name in (f"{lang.upper()}_{source(key)}", source(key)):
        if values.get(name):
            text = values[name]
            break
    else:
        return ""
    if key in ("TELEGRAM", "TELEGRAM_URL"):
        handle = text.rstrip("/").rsplit("/", 1)[-1].lstrip("@")
        return f"https://t.me/{handle}" if key == "TELEGRAM_URL" else f"@{handle}"
    if key == "PHONE_TEL":
        # Digits only: the brackets of "+375(29)133-79-01" would end the URL of
        # a markdown link early, leaving half the number in the visible text.
        digits = re.sub(r"\D", "", text)
        return f"+{digits}" if text.lstrip().startswith("+") else digits
    return text


def rows(lang):
    """The contacts as (label key, value) pairs for the catalogue: links as
    links - a resume builder wants the URL, not the anchor text."""
    return [(label, value(key, lang)) for key, label in ROW_LABELS.items() if value(key, lang)]


def expand(md, lang):
    """The markdown with every placeholder filled in. A placeholder without a
    value is fatal: a CV that ships a literal {{EMAIL}} is worse than no CV."""
    missing = []

    def fill(match):
        key = match.group(1)
        text = value(key, lang)
        if not text:
            missing.append(source(key))
        return text

    out = PLACEHOLDER.sub(fill, md)
    if missing:
        names = ", ".join(f"{lang.upper()}_{key} or {key}" for key in dict.fromkeys(missing))
        sys.exit(f"{ENV_FILE}: no value for {names}")
    return out
