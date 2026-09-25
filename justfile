# Build the CV artifacts. Names are always passed in; the recipes below only
# carry the defaults for the two languages the CV is written in.

set dotenv-load

# the real names live in .env; the file names of the artifacts follow from them
role   := env_var_or_default("ROLE", "Nodejs-backend-fullstack")
en_src := "cv-en.md"
en_pdf := env_var_or_default("EN_NAME", "Pavel Husakouski") + " - " + role + ".pdf"
ru_src := "cv-ru.md"
ru_pdf := env_var_or_default("RU_NAME", "Павел Гусаковский") + " - " + role + ".pdf"

# both languages
default: en ru

# the English CV: PDF, DOCX, catalogue
en: (update "en" en_src en_pdf)

# the Russian CV: PDF, DOCX, catalogue
ru: (update "ru" ru_src ru_pdf)

# every artifact of one CV; the DOCX and the catalogue are named after the PDF
update lang src out:
    python3 scripts/make-pdf.py "{{src}}" "{{out}}" {{lang}}
    python3 scripts/make-docx.py "{{src}}" "{{without_extension(out)}}.docx"
    python3 scripts/make-catalogue.py "{{src}}" "catalogue-{{lang}}.generated.md" {{lang}}

pdf src out lang="en":
    python3 scripts/make-pdf.py "{{src}}" "{{out}}" {{lang}}

docx src out:
    python3 scripts/make-docx.py "{{src}}" "{{out}}"

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

# rebuild a PDF on every save; with no arguments, both CVs are watched
watch +srcs=(en_src + " " + ru_src):
    ./scripts/watch-cv.sh {{srcs}}
