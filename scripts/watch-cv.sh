#!/usr/bin/env bash
# Rebuild a CV PDF whenever its markdown changes.
#
#   ./scripts/watch-cv.sh                          # every "<Name> - <Role>.md"
#   ./scripts/watch-cv.sh "Pavel Husakouski - Nodejs-backend-fullstack.md"
#   just watch                                     # the same, through the justfile
#
# With no arguments the watch is a glob, so a CV added while it runs is picked
# up too. The rebuild goes back through "just build <file>", which names the
# PDF after its source.
#
# Needs node (for npx), just and Chrome; Chrome is reached through make-pdf.py.
set -euo pipefail
# the CV sources and the artifacts live in the repository root, one level up
cd "$(dirname "$0")/.."

if [ "$#" -eq 0 ]; then
  set -- "* - *.md"
fi

# --initial builds once at start, so every PDF matches its source right away.
# --await-write-finish waits for the write to settle: editors save atomically
# (temp file, then rename), which otherwise fires twice per save and can hand
# Chrome a half-written file.
# {{changed}} is the file onchange saw change, so only that CV is rebuilt;
# on the initial run it is empty and "just build" falls back to every source.
exec npx --yes onchange@7 --initial --await-write-finish 400 "$@" \
  -- just build "{{changed}}"
