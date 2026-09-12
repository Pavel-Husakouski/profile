# Pavel Husakouski

[phusakouski@gmail.com](mailto:phusakouski@gmail.com) · [LinkedIn](https://www.linkedin.com/in/pavel-husakouski/) · +375 (29) 133-79-01 · [@Pauelito](https://t.me/Pauelito)

**Senior Software Engineer** — platform SDKs, recovery of legacy systems

## Summary of Qualifications

- 20+ years of experience in developing enterprise applications
- Programming practices — spec-driven and agent-assisted development, TDD, code review, refactoring, functional testing, E2E testing
- Cross-team collaboration, team coordination, coaching, mentoring

Experience with:
- Node.js, NestJS, Express, AWS, GraphQL, OData, .NET
- TypeScript, C#, Python, C++, SQL
- Vue.js, Pinia, Angular
- Relational and NoSQL databases — PostgreSQL, MySQL, Redis, DynamoDB
- Elasticsearch, Grafana, Prometheus, Kibana
- BullMQ, NATS
- LLM APIs — OpenAI, Anthropic, Gemini

## Professional Experience

### Backend Software Engineer with multi-project focus — AlpariGroup
**10.2023 – present**

**Key accomplishments:**

- **Scope:** Carried the backend and the infrastructure of three mobile products in parallel — 100K+ to 1M+ users each — as the sole backend engineer on all three.
- **API ownership:** Designed the APIs the Android, iOS, and admin clients were built against, and negotiated their shape with the mobile teams.
- **System Stabilization & Recovery:** Recovered three legacy products to a deployable, stable state.
- **Documentation:** Kept the feature, API, and infrastructure documentation of my products in Confluence, with PlantUML — the reference for QA and the mobile guys.
- **Testing & Reliability:** Upgraded the test suites; after that only isolated defects reached production.
- **Infrastructure:** Rebuilt logging and monitoring on Grafana and ELK, which made incidents diagnosable.

#### Project: NDA mobile call recording assistant, 1M+ users — 10.2023 – present
The backend for a mobile application for call recording and voice-to-text transcription.

**Key accomplishments:**

- Sole backend engineer: owned every backend feature from design to release, plus the build, deployment, and production support.
- Took over a product spread over 30 repositories, with parts of it missing from version control and package versions out of sync.
- Recovered the missing pieces, realigned the dependencies, and restored the build and deployment of the whole application in about six months.
- Reworked the registration, purchase, and subscription handling, migrating the purchases to StoreKit 2.
- Identified several key features that had been missing and drove them to release.
- Wrote the operational runbook — troubleshooting, maintenance, analytics — with a script behind each recurring case.

**Stack:** Microservices, TypeScript, Node.js, Express, Koa, MySQL, BullMQ, Redis, AWS, Docker

#### Project: NDA AI education assistant, 100K+ users — 10.2023 – 03.2026
The backend and admin site for the mobile homework assistant application.

**Key accomplishments:**

- Sole backend engineer: owned the backend and the infrastructure, and drove the API the mobile client and the admin site were built against.
- Delivered cross-device synchronization of the solution history, an append-only log for spend analysis, and identity and attribution (Apple, Google, AppsFlyer).
- Led the admin site: designed it, bootstrapped it, built its foundation — monorepo, authentication, backend communication, state management, deployments — then reviewed, hardened, and released the frontend developers' work.
- Redesigned the LLM pipeline after the initial implementation proved unreliable.

**Stack:** TypeScript, Node.js, NestJS, OpenAPI, PostgreSQL, Redis, Prometheus, Grafana, AWS, Docker, Mocha, GitLab CI/CD

#### Project: NDA fax transmission/reception, 1M+ users — 10.2023 – 07.2025

**Key accomplishments:**

- Sole backend engineer: owned the backend and the infrastructure, from vendor integrations to production support, and set the direction for the mobile developers building against it.
- Took over a delivery path that failed on 10–20% of transmissions and brought the failure rate down to 5–10% within six months.
- Traced the causes across infrastructure, the database, and a long tail of defects; the unattended service restarts and application hangs stopped altogether.
- Recovered the dead delivery analytics and reworked the pipeline behind it — only then did the failures become traceable.
- Built fax reception end to end, including automated procurement of virtual numbers from the telephony vendor.

**Stack:** TypeScript, Node.js, Koa, PostgreSQL, BullMQ, Redis, Prometheus, Grafana, AWS, Docker, Mocha

### Lead Software Engineer with multi-project focus — [Exadel](https://exadel.com/)
**06.2013 – 07.2023**

**Key accomplishments:**

- Mentored developers across a decade of projects; several went on to senior roles, with one-on-one coaching running up to two years.
- Taught web application engineering at the Belarusian State University for two years on behalf of Exadel.
- Co-developed and rolled out the engineering grading system for a 1000+ person company — technical level assessment and career paths.
- Trained the engineers who ran the technical interviews.

#### Project: Inter-service communication platform — 05.2019 – 07.2023
An SDK platform unifying the API of internal long-lived RESTful services across the department.

**Key accomplishments:**

- Owned the TypeScript/Node side of the platform SDK in a multi-stack team of six.
- Single-handedly implemented the server-side OData SDK — parsing, interpretation, and (de)serialization of the SQL-like query language — and built the framework on top of it.
- Optimized the SDK to performance parity with the .NET and Java implementations.
- Revamped the client library: restored it to working order, added OData 4, and gave it a query-builder DSL.
- For the sake of TDD wrote an asymmetric-matcher DSL library for partial expectations — that kept the growing suite readable.

**Stack:** TypeScript, Node.js, NestJS, Mocha, Apache Benchmark, GraphQL, Docker, AWS, Java, .NET

#### Project: An edge-service and microservice communication engine — 05.2018 – 07.2023
A micro-platform for rapid API building across backend, frontend, and microservices.

**Key accomplishments:**

- Owned the framework from version 1.11 to 6.x: designed and implemented it end to end.
- Drove the technical direction the consuming teams needed: adaptation for microservices, instrumentation, call tracing, features, and performance work.
- Carried the consuming teams through adoption — use cases, reviews, troubleshooting — and folded every finding back into the framework.
- Developed under TDD, with a test suite extensive enough to keep the major-version upgrades safe.

**Stack:** TypeScript, Express, Node.js, Mocha, Docker, GraphQL, AWS

#### Project: Generic search-based reference application — 01.2018 – 05.2019
The blueprint product teams started large corporate websites from.

**Key accomplishments:**

- Redesigned the search module at the core of the application, built on the company's in-house search engine.
- Worked out how the platform should be tested, then migrated the existing suites to Cypress.
- Built the tracing through the platform, which made request flows diagnosable.

**Stack:** Angular, Redux, TypeScript, Node.js, Express, Web Components, Cypress, Docker

#### Project: Reader application for the worldwide publisher — 06.2013 – 12.2017
The multi-platform (Android, iOS, macOS, Windows) reader application integrated into the customer's ecosystem. Its users were lawyers.

**Key accomplishments:**

- Owned the hardest modules: cross-platform API, full-text search, epub conversion, background task scheduler, persistence, diagnostics.
- Optimized core processing for a proprietary book format, rendering ultra-large files that crashed most native readers.
- Co-authored the application state and automation model, which allowed developers to write plugin-like modules, e.g. renting.

**Stack:** Angular, TypeScript, WebSQL, Cordova, NW.js, Node.js

### Senior Software Developer — [VPI Systems Inc.](http://www.vpisystems.com/)
**02.2001 – 05.2013**

#### Projects: VPI OnePlan Transport™, VPI Network Optimizer™, VPI Network Configurator™, VPI TransportMaker™, VPI ServiceMaker™
The set of CAD-like software solutions for design, dimensioning, optimizing, planning of optical networks.

**Selected accomplishments over the twelve years:**
- Designed the domain and application model and the architecture behind it, and implemented the internal DSL on top of it.
- Automated the applications with scripting built on that model.
- Redesigned the network editor and 2D visualization, the what-if, hierarchical, and routing analyses, and the reporting and persistence APIs.
- Optimized the model architecture for a 10x cut in memory footprint and CPU on large-scale models and complex computations.

**Stack:** .NET 1.0–3.5, LINQ, NUnit, GDI+, DevExpress

## Education

**Engineer's degree in Computer Science: Belarusian State University of Informatics and Radioelectronics**, Minsk, Belarus — 2002
