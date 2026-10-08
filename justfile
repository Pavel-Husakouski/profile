# Build the CV artifacts. A CV is any "<Name> - <Role>.md" in the repository
# root: its PDF takes the same name, its language is read off its title
# (see lang_of in scripts/contacts.py), so a new variant needs no entry here.

set dotenv-load

# the English CV that also goes to Drive under a role-free name
main_cv := "Pavel Husakouski - Nodejs-backend-fullstack.pdf"
main_cv_alias := "Pavel Husakouski - CV.pdf"

# where the built PDFs are published; the folder must already exist on the remote
drive := env_var_or_default("DRIVE_DIR", "MyDrive:@cv")

# the PDF of every CV
default: (each "pdf")

# run one recipe on every CV source
[private]
each recipe:
    #!/usr/bin/env bash
    set -euo pipefail
    shopt -s nullglob
    for src in *" - "*.md; do
      just {{recipe}} "$src"
    done

# the PDF of one CV, named after its source; the language is read off the source unless given
pdf src out=(without_extension(src) + ".pdf") lang="":
    python3 scripts/make-pdf.py "{{src}}" "{{out}}" {{lang}}

# the PDF of one source file; an empty argument (the watcher's first run) builds every CV
build src="":
    #!/usr/bin/env bash
    set -euo pipefail
    if [ -n "{{src}}" ]; then just pdf "{{src}}"; else just each pdf; fi

# publish one artifact to Google Drive, under its own name unless another is given
upload file name=file_name(file):
    #!/usr/bin/env bash
    set -euo pipefail
    dest="{{drive}}/{{name}}"
    # the Drive fileId: the "/d/<id>/" part of a share link. Empty while the
    # file is not on Drive yet, hence the dash.
    drive_id() { rclone lsf --format i "$1" 2>/dev/null || true; }
    before="$(drive_id "$dest")"
    echo "id before: ${before:--}"
    # rclone updates the file that is already on Drive instead of recreating it,
    # so the id stays put and a share link handed out earlier keeps working
    rclone copyto --checksum --progress "{{file}}" "$dest"
    after="$(drive_id "$dest")"
    echo "id after:  ${after:--}"

# the PDF of one source on Drive
[private]
upload-pdf src: (upload without_extension(src) + ".pdf")

# the main English PDF on Drive under the role-free name
upload-cv: (upload main_cv main_cv_alias)

# every PDF on Drive
upload-all: (each "upload-pdf") upload-cv

# rebuild every artifact and publish the PDFs
publish: default upload-all

# rebuild a PDF on every save; with no arguments, every CV is watched
[positional-arguments]
watch *srcs:
    ./scripts/watch-cv.sh "$@"
