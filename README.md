# CV

Исходники резюме в markdown — `cv-en.md` и `cv-ru.md`. Сборка даёт три артефакта на язык:
PDF (для людей), DOCX (для ATS) и `catalogue-*.generated.md` (разбор текста по пунктам).

Личных данных в markdown нет, кроме имени в заголовке: контакты лежат в `.env`, а в
исходниках стоят плейсхолдеры, которые подклеивает генератор.

## Пререквизиты
- `just` — раннер сборки;
- `chromium` — им печатается PDF (`make-pdf.py` возьмёт `google-chrome-stable`, `chromium` или `chrome`);
- `python` — скрипты сборки, сторонних библиотек не требуют;
- `nodejs`/`npm` — только для `just watch` (через `npx onchange`).

## Установка (Arch / Manjaro)

```sh
sudo pacman -S just
sudo pacman -S nodejs npm
sudo pacman -S google-chrome-stable
```

## Имя, должность и контакты

Всё это лежит в `.env` (шаблон — `.env.example`):

```sh
EN_NAME="Pavel Husakouski"
RU_NAME="Павел Гусаковский"
ROLE="Nodejs-backend-fullstack"

EMAIL="you@example.com"
PHONE="+000(00)000-00-00"
LINKEDIN="https://www.linkedin.com/in/your-handle/"
TELEGRAM="@your_handle"
EN_LOCATION="City, Country"
RU_LOCATION="Город, Страна"
EN_FORMAT="Office or remote"
RU_FORMAT="Офис или удалённо"
```

Из имён и должности собираются имена файлов выхлопа: `Pavel Husakouski -
Nodejs-backend-fullstack.pdf` (и `.docx`), и то же для русской версии. Кавычки обязательны:
без них just спотыкается о пробел в значении.

Ключ без префикса — одно значение на оба языка, с префиксом `EN_`/`RU_` — своё на каждый;
генератор сначала ищет значение под префиксом своего языка, потом без него.

Имя в заголовке `cv-*.md` написано как есть — плейсхолдером его держать незачем, язык резюме
и так задаёт форму имени. `EN_NAME`/`RU_NAME` из `.env` идут только в имена файлов выхлопа,
так что менять имя нужно в двух местах.

В `cv-*.md` вместо контактов стоят плейсхолдеры, по одному на значение, — их заполняет
`scripts/contacts.py`. Сама строка контактов остаётся в markdown, поэтому вся вёрстка —
порядок, разделители, какая ссылка с каким текстом — видна там, где её и правят:

```markdown
[{{EMAIL}}](mailto:{{EMAIL}}) · [LinkedIn]({{LINKEDIN}}) · [{{PHONE}}](tel:{{PHONE_TEL}}) · [{{TELEGRAM}}]({{TELEGRAM_URL}}) · {{LOCATION}} · {{FORMAT}}
```

| Плейсхолдер | Что подставляется |
| --- | --- |
| `{{EMAIL}}` `{{PHONE}}` `{{LINKEDIN}}` `{{LOCATION}}` `{{FORMAT}}` | значение из `.env` как есть |
| `{{TELEGRAM}}` | `@handle` |
| `{{TELEGRAM_URL}}` | `https://t.me/handle` |
| `{{PHONE_TEL}}` | номер без разметки: `+375291337901` |

`TELEGRAM` в `.env` можно писать и как `@handle`, и как ссылку — генератор приведёт к нужному
виду сам. Телефон в ссылке — только `{{PHONE_TEL}}`: скобки из `+375(29)133-79-01` оборвали бы
URL на первой `)`, и половина номера утекла бы в видимый текст.

Плейсхолдер без значения в `.env` — ошибка сборки: резюме с буквальным `{{EMAIL}}` хуже,
чем отсутствие резюме.

## Команды

| Команда | Что делает |
| --- | --- |
| `just` | всё: обе языковые версии целиком |
| `just en` / `just ru` | одна версия: PDF, DOCX, каталог |
| `just pdf <src> <out> [lang]` | только PDF |
| `just docx <src> <out> [lang]` | только DOCX |
| `just catalogue <src> <out> [lang]` | только каталог |
| `just build <src>` | PDF для одного исходника, имя и язык — по имени файла |
| `just watch [src...]` | пересборка PDF на каждое сохранение; без аргументов — оба CV |
