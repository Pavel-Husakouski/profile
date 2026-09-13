# CV fix plan

План правок `cv.md`. Пересобран 13.09.2026: статус каждого пункта сверен с текущим файлом
построчно, пункты сгруппированы в шаги, которые можно делать по одному и коммитить.

Легенда: **[текст]** — правка вносится сразу; **[факт]** — нужен ответ от тебя; **[решение]** — выбор твой.

---

## Где всё сейчас

Сверка с `cv.md` на 13.09.2026 (1183 слова, PDF — две страницы).

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

**Потеряно при сокращении** — вернуть вместе с фактами на шаге 3:

- Масштаб обеих платформ Exadel: строки `Used by numerous product teams` вырезаны, а числа вместо
  них так и не появились. Сейчас в документе нет ни одного сигнала, сколько команд ими пользовалось.
- `Single-handedly` в OData-пункте: снято вместе с суперлятивом, хотя факт был сильный и проверяемый.
- Внутренний DSL и доменная модель VPI; скрипты в рунбуке call recording.

---

## Шаг 1. Правки, которые не требуют твоих данных

Всё готово текстом, делается за один заход. Закрывает три пункта рекрутёра сразу и чинит
разбор резюме парсерами.

### 1.1 `Professional Summary` вместо `Summary of Qualifications` **[текст]**

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

### 1.2 `Skills` вместо `Experience with:` **[текст]**

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

### 1.3 Единый стиль меток в шапке AlpariGroup **[текст]**

`Scope`, `API ownership`, `Documentation`, `Infrastructure` — один стиль;
`System Stabilization & Recovery`, `Testing & Reliability` — остатки прежнего.
Привести к первому: `Recovery`, `Testing`.

### 1.4 Три формулировки, ослабить или починить **[текст]**

- Строка 72: `Trained numerous engineers to ran the technical interviews` — грамматическая ошибка
  (`to ran`) и `numerous` без числа. → `Trained the engineers who ran the technical interviews.`
- Строка 69: `Mentored developers; all of them went on to senior roles` — `all of them` читается
  как преувеличение и приписывает тебе чужой карьерный рост. → `several went on to senior roles`.
- Строка 31: `after that only isolated defects reached production` — абсолютное утверждение без
  базы. → `after that regressions stopped reaching production` или дать число (см. шаг 2).
- Строка 79: `Built a server-side framework for the SDK to run against` — нет точки в конце.

**Готово, когда:** `make-pdf.py` собирает две страницы, а в PDF есть разделы с именами
`Professional Summary` и `Skills`.

---

## Шаг 2. Собрать факты — один заход

Всё, что ниже, блокирует шаг 3. Отвечать лучше разом: правки потом вносятся за один проход.

1. **AlpariGroup, окружение.** Сколько мобильщиков и QA было вокруг; была ли платформенная или
   DevOps-команда; порядок размера кодовых баз.
2. **Остаточные 5–10% отказов факса.** Что именно осталось: сторона вендора и получателя
   (занятая линия, неверный номер, отказ приёмника) или часть была своя и не успели.
3. **Чем была AlpariGroup** в части этих трёх продуктов. Alpari — известный форекс-брокер;
   три консьюмерских мобильных продукта про факсы, звонки и домашние задания под этим именем
   выглядят нестыковкой, и читатель тратит внимание на неё вместо твоих достижений.
4. **Что было сломано в заброшенном OData-клиенте** до тебя: не собирался? не поддерживал версию
   протокола? никто не мог им пользоваться?
5. **Масштаб платформ Exadel:** сколько команд и сколько сервисов жило на каждой, хотя бы порядок.
6. **Судьба платформ после Jul 2023:** живы, переданы, закрыты. Первый вопрос любого, кто сам вёл
   платформу; его отсутствие читается как «проект кончился вместе с моим уходом».
7. **Результаты незакрытых проектов:** что дал редизайн LLM-пайплайна и чем кончился education
   assistant в Mar 2026; вышел ли reader на четыре платформы.
8. **AI-практика:** какими агентами работаешь и как именно (спеки, прогон по задачам, ревью
   агентом), что это дало измеримо (скорость, объём, качество), подхватила ли это команда.
9. **Город, формат работы** (`Remote` / `Open to relocation`), уровень английского подтвердить.
10. **LinkedIn:** совпадают ли там даты Exadel (`Jun 2013 – Jul 2023`) и VPI (`Feb 2001 – May 2013`).
11. **Alpari, дата окончания** — см. 3.4.

---

## Шаг 3. Вставить факты в проекты

Делается после шага 2, по одному пункту на ответ. Здесь же тратится запас в 120–150 слов.

### 3.1 Якорь под «единственный бэкендщик на трёх продуктах» **[факт → 2.1]**

Самый сильный и самый уязвимый пункт резюме. Форма, в которую встают числа:

```markdown
- **Scope:** Carried the backend and the infrastructure of three mobile products in parallel — two
  with 1M+ users, one with 100K+ — as the sole backend engineer on all three, alongside ⟨N⟩ mobile
  developers and ⟨N⟩ QA engineers, with no platform or DevOps team behind me.
```

### 3.2 Строка контекста про AlpariGroup **[факт → 2.3]**

Одна строка под заголовком роли — чем была эта часть бизнеса (портфель мобильных продуктов?
отдельное подразделение? продукты по заказу?).

### 3.3 Результат в каждом проекте **[факт → 2.7, 2.5, 2.6]**

Схема рекрутёра: проблема → за что отвечал лично → что спроектировал и реализовал → технологии →
с кем взаимодействовал и масштаб → результат. Первые пять звеньев закрыты почти везде; последнее —
нет, ровно в четырёх местах: AI education assistant, inter-service communication platform,
edge-service engine, reader application. Числа команд и сервисов из 2.5 возвращаются сюда же —
на место вырезанных `numerous product teams`.

### 3.4 Дата окончания в Alpari **[решение]**

`Oct 2023 – Present` при двух закрытых проектах из трёх (`Mar 2026`, `Jul 2025`). Если контракт
заканчивается — поставить дату; если работа продолжается — `Present` корректен, и пункт снят.

### 3.5 Остаточные отказы факса **[факт → 2.2]**

Если остаток на стороне вендора и получателя — сказать прямо одной вставкой:
`the residual failures sit on the carrier and recipient side`. Если часть была своя — что осталось
нерешённым и почему.

### 3.6 Заброшенный OData-клиент **[факт → 2.4]**

`Revamped the client library: restored it to working order` — что именно было сломано и что стало.
Заодно вернуть `single-handedly` в пункт про OData SDK: факт проверяемый, и без него пункт
не отличается от работы в команде из шести человек.

```markdown
- Single-handedly implemented the server-side OData SDK — parsing, interpretation, and
  (de)serialization of the SQL-like query language — and designed the framework it runs on.
  OData is a large and intricate specification; the SDK covers it down to its edge cases.
```

### 3.7 AI как процесс, а не ярлык **[факт → 2.8]**

Рекрутёр просит четыре вещи: какие задачи решаются, какими инструментами, как AI встроен в процесс
разработки, какой результат. Сейчас в файле остались ровно те две строки, которые он просил
заменить: `spec-driven and agent-assisted development` в практиках и `LLM APIs — OpenAI, Anthropic,
Gemini` в инвентаре. Пет-проект с оркестрацией агентов в резюме ты не хочешь — значит, практика
остаётся единственным носителем этой линии и должна быть описана как процесс.

---

## Шаг 4. Шапка и поля для ATS

Короткий шаг, но трогает то, что парсер читает первым.

### 4.1 Заголовок под именем **[решение]**

Сейчас: `**Senior Software Engineer** — platform SDKs, recovery of legacy systems`.
Строка уже занята должностью — главное сделано. Открыт один вопрос: в ней нет ни `Backend`,
ни `TypeScript/Node.js`, а многие парсеры берут «current title» именно отсюда. Вариант рекрутёра:

```
Senior Software Engineer | Backend (TypeScript/Node.js)
20+ Years in Enterprise Application Development | Architecture, Infrastructure & Technical Coordination
```

`Senior` шире по числу вакансий; `Lead` точнее отражает систему грейдов, подготовку интервьюеров
и техническое направление для мобильных команд. Решение твоё; вторая строка в любом случае должна
нести архитектуру, инфраструктуру и техническую координацию.

Заодно: названия ролей `Backend Software Engineer with multi-project focus` и `Lead Software
Engineer with multi-project focus` — хвост `with multi-project focus` мешает сопоставлению
должностей и ничего не сообщает; масштаб уже сказан в `Scope`.

### 4.2 Контактная строка **[факт → 2.9]**

Сейчас единственный географический сигнал — телефон `+375`. Для международных вакансий отсутствие
города, формата работы и разрешения на работу — причина отложить резюме, а не задать вопрос.
Добавить: город и страну, `Remote` / `Open to relocation`. Проверить заодно, что адрес
`phusakouski@gmail.com` — тот, на который ты ждёшь ответ.

### 4.3 Языки отдельной строкой **[текст]**

Сейчас английский спрятан четвёртым пунктом в саммари. Вынести вместе с родными:
`English — B2 (Upper-Intermediate) · Russian/Belarusian — Native`.

### 4.4 Сверить даты с LinkedIn **[факт → 2.10]**

Рекрутёр открывает профиль параллельно с резюме; расхождение в годах он трактует не как опечатку,
а как редактирование биографии.

---

## Шаг 5. Экспорт и проверка

Делается последним, после того как текст замер.

- [ ] Экспорт в **текстовый PDF** (не картинка) и `.docx`; отправлять их, а не ссылку на
      репозиторий — парсер её не откроет. `python3 make-pdf.py`, или `./watch-cv.sh` во время правок.
- [ ] **Контакты плоским текстом** — email, телефон, город; markdown-ссылки и разделители `·`
      при конвертации теряются вместе с содержимым.
- [ ] **Типографику заменить на ASCII** — `—`, `–`, `·`, `™` в части парсеров превращаются в мусор
      и склеивают слова.
- [ ] Прогнать результат через любой резюме-парсер: совпали ли имя, титул, компании, даты.
- [ ] **Телефонию в стек факсового проекта** — `Telnyx`, `Twilio`, `Plivo`, `RabbitMQ`, если они там
      были: сейчас этих слов в резюме нет вообще, а работа за ними стоит.

### 5.1 Двухколоночную версию в ATS не отправлять

Установлено на файле (12.09.2026, `pdftotext` на обоих): из-за двух колонок `SUMMARY` и `EXPERIENCE`
выдаются вплотную, а сайдбар (`LANGUAGE`, `SKILLS AND TOOLS`, `EDUCATION & CERTIFICATIONS`)
извлекается **внутри** блока Alpari — между его пунктами и его же проектами. Парсер, привязывающий
содержимое к ближайшему предшествующему заголовку, отнесёт три продуктовых проекта к разделу
«Education». Это потеря данных, а не вопрос стиля.

- [ ] Для всех подач через ATS — одноколоночный PDF из `make-pdf.py`.
- [ ] Если Canva-версия остаётся для отправки человеку — синхронизировать её с `cv.md`. Сейчас там
      версия до правок: `20+ years`, `2–3x` без базы, `Oct 2026` как дата окончания в будущем,
      `Sep 2010 — Present` у Exadel, несуществующий `Apple Store Server SDK`, `Vue.js Pinia Angular`
      без разделителей, склейка `agentand` при извлечении. Иначе по двум каналам уходят две
      разные биографии.

---

## Гигиена репозитория — закрыт

- [x] **Разбор резюме в репозитории.** Репозиторий приватный, поэтому `Pavel Husakouski — Resume
      Audit.md`, `Recruiter feedback.md` и этот план остаются в нём осознанно.
- [x] **Каталог не путается с резюме.** Переименован в `catalogue.generated.md`, собирается из
      `cv.md` через `make-catalogue.py`; имя говорит, что ручные правки будут затёрты.

Единственное, что вернёт раздел к жизни: если репозиторий станет публичным, вместе с резюме станут
читаемыми и три документа о его слабых местах. Тогда либо вынести их, либо оставить приватным.
