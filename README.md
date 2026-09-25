# CV

Исходники резюме в markdown — `cv-en.md` и `cv-ru.md`. Сборка даёт три артефакта на язык:
PDF (для людей), DOCX (для ATS) и `catalogue-*.generated.md` (разбор текста по пунктам).

## Установка (Arch / Manjaro)

```sh
sudo pacman -S just python chromium nodejs npm
```

- `just` — раннер сборки;
- `chromium` — им печатается PDF (`make-pdf.py` возьмёт `google-chrome-stable`, `chromium` или `chrome`);
- `python` — скрипты сборки, сторонних библиотек не требуют;
- `nodejs`/`npm` — только для `just watch` (через `npx onchange`).

## Имя и должность

Имена файлов выхлопа собираются из `.env` (шаблон — `.env.example`):

```sh
EN_NAME="Pavel Husakouski"
RU_NAME="Павел Гусаковский"
ROLE="Nodejs-backend-fullstack"
```

Отсюда получается `Pavel Husakouski - Nodejs-backend-fullstack.pdf` (и `.docx`), и то же для
русской версии. Кавычки обязательны: без них just спотыкается о пробел в значении.

## Команды

| Команда | Что делает |
| --- | --- |
| `just` | всё: обе языковые версии целиком |
| `just en` / `just ru` | одна версия: PDF, DOCX, каталог |
| `just pdf <src> <out> [lang]` | только PDF |
| `just docx <src> <out>` | только DOCX |
| `just catalogue <src> <out> [lang]` | только каталог |
| `just build <src>` | PDF для одного исходника, имя и язык — по имени файла |
| `just watch [src...]` | пересборка PDF на каждое сохранение; без аргументов — оба CV |
