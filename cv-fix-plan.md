# CV fix plan

План правок `cv.md`. Пересобран 13.09.2026: статус каждого пункта сверен с текущим файлом
построчно, пункты сгруппированы в шаги, которые можно делать по одному и коммитить.

Легенда: **[текст]** — правка вносится сразу; **[факт]** — нужен ответ от тебя; **[решение]** — выбор твой.

---

## Где всё сейчас

Сверка с `cv.md` на 13.09.2026, вечер (1337 слов, PDF — две страницы; шаги 1–4 закрыты, кроме LinkedIn).

**Закрыто** (пункты прежних разделов P0–P3, снятые с плана):

- Рекомендации убраны; дата окончания Exadel стоит; общий блок Key Accomplishments распределён
  по проектам; ранний опыт сжат до трёх пунктов на двенадцать лет VPI.
- Строка про attitude заменена заголовком с позицией (строка 4).
- Общие фразы вычищены: `My attitude…`, `Good understanding and horizon…`,
  `Strong understanding of software design…` — ни одной не осталось.
- NDA-проекты расшифрованы по домену: call recording assistant, AI education assistant,
  fax transmission/reception, с числом пользователей в заголовке.
- Из OData-пункта убраны `the architecture is mine` и `the most demanding work of my career`;
  идиома `brought it back to its former glory` заменена на `restored it to working order`.
- Резюме больше не ссылается само на себя (`…outcomes are in the project sections below`).
- Первое лицо вычищено из всех пунктов.
- Даты в формате `Oct 2023 – Present` во всех десяти местах; `make-pdf.py` принимает оба формата.
- Объём: 1683 → 1183 слова, две страницы. Требование рекрутёра выполнено, и появился запас
  примерно на 120–150 слов — его тратим на результаты из шага 3, а не на новые описания.
- Side project (склад, 2008–2009) убран из документа целиком — вопрос обратной хронологии снят.

**Сделано после пересборки плана** (правки по одной строке, 13.09.2026):

- Строка 30 — документация: вернулись `Confluence`, `PlantUML` и «всех трёх продуктов».
- Строки 38–39 — `Inherited a product in 30 repositories` вместо `Took over…`; срок «шесть месяцев» убран.
- Строки 59–60 — restarts/hangs сжаты до одной фразы с причиной и результатом; `within six months`
  убран и здесь.
- Строка 69 — `all of them went on to senior roles` → `several reached senior roles, some after two
  years of one-on-one coaching`. Пункт 1.4 в этой части закрыт.
- Строка 106 — описание reader'а: аудитория вперёд, висящее `Its users were lawyers.` убрано.
- Строка 50 — начата переделка под аудит расходов, но осталась сломанной грамматика (см. 1.4).

**Потеряно при сокращении** — вернуть вместе с фактами на шаге 3:

- Масштаб обеих платформ Exadel: строки `Used by numerous product teams` вырезаны, а числа вместо
  них так и не появились. Сейчас в документе нет ни одного сигнала, сколько команд ими пользовалось.
- `Single-handedly` в OData-пункте: снято вместе с суперлятивом, хотя факт был сильный и проверяемый.
- Внутренний DSL и доменная модель VPI; скрипты в рунбуке call recording.

---

## Шаг 1. Правки, которые не требуют твоих данных

Всё готово текстом, делается за один заход. Закрывает три пункта рекрутёра сразу и чинит
разбор резюме парсерами.

### 1.1 `Professional Summary` вместо `Summary of Qualifications` — сделано 13.09.2026

Рекрутёр просит два раздела — смысловой и технический. Сейчас первый состоит из четырёх
строк-качеств, в которых нет ни одного события.

```markdown
## Professional Summary

- 25 years in software engineering: 10 at a services company building platforms and frameworks for
  other engineering teams, 3 as the sole backend engineer of three consumer mobile products.
- Build what others depend on — an OData SDK and framework, a microservice communication engine
  shipped from 1.11 to 6.x, API contracts for Android, iOS, and admin clients.
- Recover broken systems: a product spread over 30 repositories restored to a deployable state,
  fax delivery failures cut from 10–20% to 5–10%, an abandoned OData client revived.
- Technical coordination without a management title: initiate the design discussions, write the
  specifications, record the decisions, and settle who owns what across mobile, QA, and product.
- Set engineering standards beyond my own code: co-authored the technical grading system for
  a 1000+ person company, trained the engineers who ran technical interviews, taught web
  engineering at a university for two years.
```

Четвёртый пункт — формула из раздела 2 аудита рекрутёра, которой в резюме нет вообще.
`10 at a services company` — Exadel Jun 2013 – Jul 2023; VPI идёт отдельной строкой опыта.

### 1.2 `Skills` вместо `Experience with:` — сделано 13.09.2026 (без `Jenkins` и `RabbitMQ`: фактами документа не подтверждены)

`Experience with:` для парсера не заголовок — весь инвентарь технологий уходит в никуда.
Раздел с именем `Skills` ищут буквально.

```markdown
## Skills

**Backend** TypeScript, Node.js, NestJS, Express, Koa, REST, GraphQL, OData, microservices,
distributed systems, SDK and framework design
**Data** PostgreSQL, MySQL, Redis, DynamoDB, Elasticsearch, SQL
**Async** BullMQ, NATS, RabbitMQ
**Cloud and CI/CD** AWS, Docker, GitLab CI/CD, Jenkins
**Observability** Grafana, Prometheus, ELK, Kibana, tracing
**Testing** TDD, unit testing, integration testing, E2E, Mocha, Cypress
**AI** OpenAI, Anthropic, Gemini APIs; spec-driven and agent-assisted development
**Also** C#, .NET, Python, C++, Angular, Vue.js, Pinia
```

Фронтенд и ранние стеки — в `Also` последней строкой: остаются для ATS и полноты, но перестают
конкурировать с бэкендом за внимание. Ключевые слова `REST`, `CI/CD`, `observability`,
`unit testing`, `integration testing`, `distributed systems`, `RabbitMQ` сейчас в файле
отсутствуют — все они закрываются фактами документа, это починка фильтров, а не накрутка.

### 1.3 Единый стиль меток в шапке AlpariGroup — сделано 13.09.2026

`Scope`, `API ownership`, `Documentation`, `Infrastructure` — один стиль;
`System Stabilization & Recovery`, `Testing & Reliability` — остатки прежнего.
Привести к первому: `Recovery`, `Testing`.

### 1.4 Три формулировки, ослабить или починить — сделано 13.09.2026

- ~~Строка 72: `to ran`~~ — исправлено на `to conduct` 13.09.2026. Осталось `numerous` без числа:
  → `Trained the engineers who conducted the technical interviews.`
- ~~Строка 69: `all of them went on to senior roles`~~ — сделано 13.09.2026.
- Строка 31: `Introduced unit/integration/E2E tests suites` — `tests suites` вместо `test suites`;
  и `after that only isolated defects reached production` — абсолютное утверждение без базы.
  → `after that regressions stopped reaching production` или дать число (см. шаг 2).
- Строка 50: `spends to be traceable to the user/request behind it` — `spends` (неисчисляемое) и
  сломанная конструкция. → `spend traceable to the user and the request behind it`.
- ~~Строка 79: нет точки в конце~~ — исправлено 13.09.2026.

### 1.5 Два решения, всплывшие при правках **[решение]**

- **Строка 71:** `Architected and rolled out the grading system` — было `Co-developed`. Если систему
  делали вдвоём-втроём, `Architected` завышает роль, и это ровно тот случай, когда проверка на
  интервью стоит дорого. Текст саммари в 1.1 сейчас написан под `co-authored` — выбрать одно.
- **Строка 77:** `Solely owned the TypeScript/Node side of the huge platform SDK in a multi-stack team
  of six` — `huge` это прилагательное без события, ровно то, что вычищали из саммари, а `Solely` рядом
  с `team of six` спотыкает читателя. Факт сильный, ему нужна прямая форма:
  `Sole TypeScript/Node engineer on the platform SDK, in a multi-stack team of six.`
- **Сроки.** `in about six months` (восстановление сборки) и `within six months` (факс) убраны оба.
  Первое — правильно, там срок работал против тебя. Второе стоило оставить: там он подпирал
  измеримую дельту 10–20% → 5–10%, то есть отвечал на вопрос «за сколько». Вернуть или нет — решить.

**Готово:** 13.09.2026 — 1285 слов, две страницы, разделы `Professional Summary` и `Skills` на месте.
Английский переехал строкой `**Languages**` в `Skills` — часть пункта 4.3 закрыта попутно.

---

## Шаг 2. Собрать факты — один заход

Всё, что ниже, блокирует шаг 3. Отвечать лучше разом: правки потом вносятся за один проход.

1. ~~**AlpariGroup, окружение**~~ — закрыто 13.09.2026: 2 Android + 3 iOS, до 3 QA, PM и PdM;
   DevOps вне команды, выдают ресурсы; кодовые базы — десятки KLOC каждая.
2. ~~**Остаточные 5–10% отказов факса**~~ — ответ 13.09.2026: обычная телефония на стороне
   получателя (нет факса на номере, занято, не отвечает). Внесено в строку факсового проекта.
3. ~~**Чем была AlpariGroup**~~ — снято 13.09.2026 решением: подробностей не даём. Риск остаётся:
   читатель спотыкается о связку «форекс-брокер + приложения про факсы», но это осознанный выбор.
4. ~~**Что было сломано в OData-клиенте**~~ — ответ 13.09.2026: кодогенерация и билды сломаны,
   отставание по версии протокола, диспаритет по фичам с .NET и Java, дыры в типизации. Внесено
   двумя пунктами. Асинхронная десериализация в конструкторе оставлена для интервью.
5. ~~**Масштаб платформ Exadel**~~ — ответ 13.09.2026: десятки команд, внесено в оба проекта.
   Открыто только число сервисов, если оно известно.
6. ~~**Судьба платформ после Jul 2023**~~ — снято 13.09.2026: Exadel ушёл из региона, дальнейшая
   судьба неизвестна. В резюме не пишем — на интервью это один спокойный ответ.
7. ~~**Результаты незакрытых проектов**~~ — закрыто 13.09.2026: education assistant заморожен после
   неудачной закупки трафика, работал без падений; пайплайн перестал падать, зависать и обрезать
   ответы; reader вышел на все четыре платформы.
8. ~~**AI-практика**~~ — закрыто 13.09.2026: Claude Code и GitHub Copilot, spec-driven, время от
   проектирования до деливери примерно вдвое меньше. Подхватила ли команда — неизвестно, в резюме
   не пишем.
9. ~~**Город, формат работы**~~ — закрыто 13.09.2026: `Minsk, Belarus · Office or remote` в контактной
   строке; английский B2 подтверждён и стоит строкой `Languages` в `Skills`.
10. **LinkedIn:** совпадают ли там даты Exadel (`Jun 2013 – Jul 2023`) и VPI (`Feb 2001 – May 2013`).
11. ~~**Alpari, дата окончания**~~ — 13.09.2026: `Present` верен, работа продолжается.

---

## Шаг 3. Вставить факты в проекты

Делается после шага 2, по одному пункту на ответ. Здесь же тратится запас в 120–150 слов.

### 3.1 Якорь под «единственный бэкендщик на трёх продуктах» — сделано 13.09.2026

Ответ: 2 Android + 3 iOS, до 3 QA, PM и PdM; DevOps вне команды, выдают ресурсы. Внесено в строку 27
(команда) и строку 32 (граница с DevOps: ресурсы — их, всё, что на них работает, — бэкенд).

Осталось из вопроса 1: порядок размера кодовых баз — он объясняет, как один человек тянул три
продукта.

### 3.2 Строка контекста про AlpariGroup **[факт → 2.3]**

Одна строка под заголовком роли — чем была эта часть бизнеса (портфель мобильных продуктов?
отдельное подразделение? продукты по заказу?).

### 3.3 Результат в каждом проекте — сделано 13.09.2026

Схема рекрутёра: проблема → за что отвечал лично → что спроектировал и реализовал → технологии →
с кем взаимодействовал и масштаб → результат. Первые пять звеньев закрыты почти везде; последнее —
нет, ровно в четырёх местах: AI education assistant, inter-service communication platform,
edge-service engine, reader application. Числа команд и сервисов из 2.5 возвращаются сюда же —
на место вырезанных `numerous product teams`.

### 3.4 Дата окончания в Alpari — снято 13.09.2026

Работа продолжается, `Present` корректен.

### 3.5 Остаточные отказы факса — сделано 13.09.2026

`…brought it down to 5–10% — the telephony baseline: no fax at the number, busy, no answer.`

### 3.6 Заброшенный OData-клиент — сделано 13.09.2026

Осталось вернуть `single-handedly` в пункт про OData SDK: факт проверяемый, и без него пункт
не отличается от работы в команде из шести человек.

```markdown
- Single-handedly implemented the server-side OData SDK — parsing, interpretation, and
  (de)serialization of the SQL-like query language — and designed the framework it runs on.
  OData is a large and intricate specification; the SDK covers it down to its edge cases.
```

### 3.7 AI как процесс, а не ярлык — сделано 13.09.2026

Пункт `**AI in the workflow:**` в шапке роли AlpariGroup (спека → агенты → ревью, время от
проектирования до деливери вдвое меньше) и строка `**AI**` в `Skills` с именами инструментов.

К интервью держать наготове один конкретный пример под «вдвое»: какая фича, сколько заняла бы
и сколько заняла. Множитель без базы — первое, что спрашивают.

---

## Шаг 4. Шапка и поля для ATS

Короткий шаг, но трогает то, что парсер читает первым.

### 4.1 Заголовок под именем — сделано 13.09.2026

Строка 4: `**Senior Backend Engineer (TypeScript/Node.js)** — platform SDKs, recovery of legacy
systems`. Хвост `with multi-project focus` убран из названий обеих ролей (строки 28 и 72).

Решение по `Backend` против `Backend/Fullstack`: слэш не ставим — он читается как неуверенность,
а парсер кладёт титул в одно поле и не совпадёт ни с одним фильтром. Если понадобится fullstack-
воронка, делаем вторую версию строки 4, а не двойной титул в одной.

### 4.2 Контактная строка — сделано 13.09.2026

`Minsk, Belarus · Office or remote` добавлено хвостом контактной строки. Открыто: подтвердить, что
`phusakouski@gmail.com` — адрес, на который ты ждёшь ответ; и решить, нужна ли пометка про
разрешение на работу для международных вакансий.

### 4.3 Языки отдельной строкой — сделано 13.09.2026

Строка `**Languages**` в `Skills`: `English — B2 (Upper-Intermediate), Russian — Native`.

### 4.4 Синхронизировать LinkedIn — чек-лист готов 13.09.2026, правки за тобой

Готовый текст и порядок действий — в `linkedin-sync.md`: headline, About, три роли с датами,
описания, порядок навыков, финальная сверка чисел.

Даты не совпадают (подтверждено 13.09.2026). Рекрутёр открывает профиль параллельно с резюме;
расхождение в годах он трактует не как опечатку, а как редактирование биографии. Привести профиль
к датам резюме: Exadel `Jun 2013 – Jul 2023`, VPI `Feb 2001 – May 2013`. Заодно сверить названия
ролей и состав проектов — резюме за сегодня ушло далеко вперёд профиля.

---

## Шаг 5. Экспорт и проверка

Делается последним, после того как текст замер.

Объём: после всех вставок фактов резюме выросло до трёх страниц и было возвращено на две
13.09.2026 — сжаты два пункта саммари, убраны повтор `Owned every backend feature`, миграция на
Cypress, подводка VPI и перечисление обвязки админки; `™` и `Minsk` из `Education` тоже ушли.

- [x] **Экспорт** — сделано 13.09.2026. Два артефакта из `cv.md`, оба в ATS-виде:
      `python3 make-pdf.py` → `Pavel Husakouski - CV.pdf`, `python3 make-docx.py` →
      `Pavel Husakouski - CV.docx`. Красивая версия не делается: решено 13.09.2026, что резюме
      уходит только через порталы, а два разных файла с одной биографией — источник расхождений.
      В PDF типографика свёрнута в ASCII, контакты видны адресами и при этом кликабельны;
      в docx — плоский текст. Отправлять файлы, а не ссылку на репозиторий — парсер её не откроет.
      `make-docx.py` пишет zip с XML вручную, без зависимостей, и переиспользует `to_ascii`
      из `make-pdf.py`. Проверено: все части well-formed, типографики не осталось.
      **Не проверено:** как файл открывается в настоящем Word — office-пакета в системе нет.
- [x] **Контакты плоским текстом** и **типографика в ASCII** — сделано 13.09.2026 в `make-pdf.py`:
      флаг `--ascii` собирает `Pavel Husakouski - CV (ATS).pdf`, где `—`, `–`, `·`, `™`, кавычки и
      многоточия свёрнуты в ASCII, а ссылки контактной строки развёрнуты в адрес и URL
      (`linkedin.com/in/pavel-husakouski`, `t.me/Pauelito`). Обычный `python3 make-pdf.py` по-прежнему
      даёт красивый PDF для человека. Обе версии — две страницы.
- [ ] Прогнать результат через любой резюме-парсер: совпали ли имя, титул, компании, даты.
- [x] **Телефония в стеке факсового проекта** — сделано 13.09.2026: `Telnyx`, `Twilio`, `Plivo`
      в `Stack`, «три вендора» в пункте про владение. `RabbitMQ` не добавлен: не подтверждён — спросить, был ли он в факсовом пайплайне.

### 5.1 Canva-версия — выброшена 13.09.2026

Решение: не используется, не синхронизируется, никуда не отправляется. Единственный источник —
`cv.md`, единственные артефакты — PDF и `.docx` из скриптов репозитория.

Почему не стоило её тащить дальше:

- Две колонки ломают извлечение: `SUMMARY` и `EXPERIENCE` выдаются вплотную, а сайдбар
  (`LANGUAGE`, `SKILLS AND TOOLS`, `EDUCATION & CERTIFICATIONS`) вытаскивается **внутри** блока
  Alpari — между его пунктами и его же проектами. Парсер, привязывающий содержимое к ближайшему
  предшествующему заголовку, относит три продуктовых проекта к разделу «Education».
- Содержание отстало навсегда: `20+ years`, `2–3x` без базы, `Oct 2026` как дата окончания
  в будущем, `Sep 2010 — Present` у Exadel, несуществующий `Apple Store Server SDK`,
  склейка `agentand` при извлечении.

## Гигиена репозитория — закрыт

- [x] **Разбор резюме в репозитории.** Репозиторий приватный, поэтому `Pavel Husakouski — Resume
      Audit.md`, `Recruiter feedback.md` и этот план остаются в нём осознанно.
- [x] **Каталог не путается с резюме.** Переименован в `catalogue.generated.md`, собирается из
      `cv.md` через `make-catalogue.py`; имя говорит, что ручные правки будут затёрты.

Единственное, что вернёт раздел к жизни: если репозиторий станет публичным, вместе с резюме станут
читаемыми и три документа о его слабых местах. Тогда либо вынести их, либо оставить приватным.
