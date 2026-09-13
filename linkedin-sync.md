# LinkedIn sync

Профиль отстал от `cv.md`: даты не совпадают, названия ролей и состав проектов — версия
до правок 13.09.2026. Рекрутёр открывает профиль параллельно с резюме, и расхождение в годах
он читает не как опечатку, а как редактирование биографии.

Источник истины — `cv.md`. Ниже — что и на что менять, сверху вниз по профилю.

---

## 1. Headline

```
Senior Backend Engineer (TypeScript/Node.js) — platform SDKs, recovery of legacy systems
```

Тот же титул, что в строке 4 резюме. Headline — главное поле поиска у рекрутёров: они ищут
`Backend Engineer`, `Node.js`, `TypeScript`, и все три слова должны стоять здесь буквально.

## 2. Location и Open to work

- Location: `Minsk, Belarus`.
- Open to work → Job titles: `Backend Engineer`, `Senior Backend Engineer`, `Software Engineer`.
- Locations: `Minsk` плюс `Remote`.
- Start date: `Immediately` или как есть на самом деле.

## 3. About

```
25 years in software engineering: 10 at a services company building platforms and frameworks for
other engineering teams, 3 as the sole backend engineer of three consumer mobile products.

I build what others depend on — an OData SDK and framework, a microservice communication engine
shipped from 1.11 to 6.x, API contracts for Android, iOS, and admin clients.

I recover broken systems: a product spread over 30 repositories restored to a deployable state,
fax delivery failures cut from 10–20% to 5–10%, an abandoned OData client revived.

Technical coordination without a management title: specifications, recorded decisions, and settled
ownership across mobile, QA, and product. Engineering standards beyond my own code: the grading
system for a 1000+ person company, interviewer training, two years of university teaching.

Backend: TypeScript, Node.js, NestJS, Express, Koa, REST, GraphQL, OData, microservices.
AI: Claude Code, GitHub Copilot, spec-driven development; OpenAI, Anthropic, Gemini APIs.
Data: PostgreSQL, MySQL, Redis, DynamoDB, Elasticsearch.
Cloud: AWS, Docker, GitLab CI/CD, Grafana, Prometheus, ELK.
```

Первое лицо здесь уместно — About читает человек, а не парсер; в резюме оно остаётся безличным.

## 4. Experience — даты в первую очередь

| Компания | Title | Даты |
|---|---|---|
| AlpariGroup | Backend Software Engineer | `Oct 2023 – Present` |
| Exadel | Lead Software Engineer | `Jun 2013 – Aug 2023` |
| VPI Systems Inc. | Senior Software Developer | `Feb 2001 – Feb 2013` |

Проверить построчно: даты в профиле и в резюме должны совпадать до месяца. Внутри Exadel проекты
заканчиваются `Jul 2023`, а сама роль — `Aug 2023`; это нормально (последний месяц без проекта),
но в профиле проекты отдельными записями не заводить, иначе расхождение придётся объяснять.

Между VPI (`Feb 2013`) и Exadel (`Jun 2013`) теперь три месяца разрыва. Рекрутёры такие промежутки
замечают и спрашивают — ответ должен быть наготове, либо даты стоит поправить, если разрыва
на самом деле не было.

### AlpariGroup — описание

```
Sole backend engineer on three consumer mobile products in parallel — 100K+ to 1M+ users each —
alongside five mobile developers and up to three QA.

• Designed and negotiated the APIs the Android, iOS, and admin clients were built against.
• Recovered three legacy products to a deployable, stable state.
• Spec-first work with Claude Code and GitHub Copilot, roughly halving design-to-delivery time.
• Feature, API, and infrastructure documentation in Confluence and PlantUML.
• Unit, integration, and E2E suites; logging and monitoring rebuilt on Grafana and ELK.
```

Названия трёх продуктов под NDA — в профиле их тоже не называть, только домен: call recording
and transcription, AI homework assistant, fax transmission and reception.

### Exadel — описание

```
• Owned the TypeScript/Node side of a platform SDK (100K+ lines) used by dozens of product teams.
• Implemented the server-side OData SDK and the framework it runs on; brought it to performance
  parity with the .NET and Java implementations.
• Owned an edge-service and microservice framework from version 1.11 to 6.x end to end.
• Architected the engineering grading system, assessment and career paths for a 1000+ person company.
• Mentored engineers; trained the engineers who conducted technical interviews; taught web
  application engineering at the Belarusian State University for two years.
```

### VPI Systems — описание

```
CAD-like software for design, dimensioning, optimization, and planning of optical networks.
Designed the application, domain, and automation model; redesigned the network editor and 2D
visualization; optimized for large-scale models — 10x less memory and CPU.
```

## 5. Skills

Первые три позиции закреплять вручную — их видно без раскрытия списка и по ним ранжируется поиск:

1. `Node.js`
2. `TypeScript`
3. `Backend Development`

Дальше: `NestJS`, `Express.js`, `REST APIs`, `GraphQL`, `OData`, `Microservices`, `Distributed Systems`,
`PostgreSQL`, `MySQL`, `Redis`, `DynamoDB`, `Elasticsearch`, `AWS`, `Docker`, `CI/CD`, `Grafana`,
`Prometheus`, `ELK`, `TDD`, `Unit Testing`, `Integration Testing`, `Mocha`, `Cypress`, `Software
Architecture`, `SDK Development`, `Technical Documentation`, `Mentoring`.

Старые навыки (`C#`, `.NET`, `C++`, `Angular`, `Vue.js`) не удалять, но и не держать наверху —
они перетягивают на себя выдачу.

## 6. Education

```
Belarusian State University of Informatics and Radioelectronics
Engineer's degree, Computer Science — 2002
```

## 7. Сверить напоследок

- [x] Даты трёх ролей совпадают с `cv.md` до месяца.
- [x] Ни одного названия NDA-продукта.
- [ ] Headline, About и Experience не противоречат резюме по числам: 25 лет, 10 в Exadel,
      3 продукта, 1M+/100K+ пользователей, 10–20% → 5–10%, 1.11 → 6.x, 1000+ человек.
- [ ] Custom URL профиля — `linkedin.com/in/pavel-husakouski` (уже так, в резюме ссылка на него).
- [ ] Фото и баннер на месте: профиль без фото рекрутёры открывают заметно реже.
