# Build the CV artifacts. Names are always passed in; the recipes below only
# carry the defaults for the two languages the CV is written in.

set dotenv-load

# the real names and contacts live in .env; cv-*.md holds only placeholders,
# and the file names of the artifacts follow from the names
role   := env_var_or_default("ROLE", "Nodejs-backend-fullstack")
en_src := "cv-en.md"
en_pdf := env_var_or_default("EN_NAME", "Pavel Husakouski") + " - " + role + ".pdf"
ru_src := "cv-ru.md"
ru_pdf := env_var_or_default("RU_NAME", "Павел Гусаковский") + " - " + role + ".pdf"
# on Drive the English PDF is also kept under a role-free name
en_cv  := env_var_or_default("EN_NAME", "Pavel Husakouski") + " - CV.pdf"

# where the built PDFs are published; the folder must already exist on the remote
drive := env_var_or_default("DRIVE_DIR", "MyDrive:@cv")

# both languages
default: en ru

# the English CV: PDF, DOCX, catalogue
en: (update "en" en_src en_pdf)

# the Russian CV: PDF, DOCX, catalogue
ru: (update "ru" ru_src ru_pdf)

# every artifact of one CV; the DOCX and the catalogue are named after the PDF
update lang src out:
    python3 scripts/make-pdf.py "{{src}}" "{{out}}" {{lang}}
    python3 scripts/make-docx.py "{{src}}" "{{without_extension(out)}}.docx" {{lang}}
    python3 scripts/make-catalogue.py "{{src}}" "catalogue-{{lang}}.generated.md" {{lang}}

pdf src out lang="en":
    python3 scripts/make-pdf.py "{{src}}" "{{out}}" {{lang}}

docx src out lang="en":
    python3 scripts/make-docx.py "{{src}}" "{{out}}" {{lang}}

catalogue src out lang="en":
    python3 scripts/make-catalogue.py "{{src}}" "{{out}}" {{lang}}

# the PDF of one source file; the language and the output name follow from it.
# An empty argument (the initial run of the watcher) builds both.
build src="":
    #!/usr/bin/env bash
    set -euo pipefail
    case "$(basename "{{src}}")" in
      "{{ru_src}}") just pdf "{{ru_src}}" "{{ru_pdf}}" ru ;;
      "{{en_src}}") just pdf "{{en_src}}" "{{en_pdf}}" en ;;
      *) just pdf "{{en_src}}" "{{en_pdf}}" en
         just pdf "{{ru_src}}" "{{ru_pdf}}" ru ;;
    esac

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

# the Russian PDF on Drive
upload-ru: (upload ru_pdf)

# the English PDF on Drive
upload-en: (upload en_pdf)

# the English PDF on Drive under the role-free name
upload-cv: (upload en_pdf en_cv)

# every PDF on Drive
upload-all: upload-ru upload-en upload-cv

# rebuild every artifact and publish the PDFs
publish: default upload-all

# rebuild a PDF on every save; with no arguments, both CVs are watched
watch +srcs=(en_src + " " + ru_src):
    ./scripts/watch-cv.sh {{srcs}}
