#!/usr/bin/env bash
# Rebuild the CV PDF whenever cv.md changes.
#
#   ./watch-cv.sh                     # watch cv.md
#   ./watch-cv.sh cv.md make-pdf.py   # watch these files instead
#
# Needs node (for npx) and Chrome; both are reached through make-pdf.py.
set -euo pipefail
cd "$(dirname "$0")"

files=("${@:-cv.md}")

# --initial builds once at start, so the PDF matches the file right away.
# --await-write-finish waits for the write to settle: editors save atomically
# (temp file, then rename), which otherwise fires twice per save and can hand
# Chrome a half-written file.
exec npx --yes onchange@7 --initial --await-write-finish 400 "${files[@]}" \
  -- python3 make-pdf.py
