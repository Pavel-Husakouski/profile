# Pavel Husakouski
[phusakouski@gmail.com](mailto:phusakouski@gmail.com) · [LinkedIn](https://www.linkedin.com/in/pavel-husakouski/) · +375(29)133-79-01 · [@Pauelito](https://t.me/Pauelito)

**Senior Software Engineer** — platform SDKs, recovery of legacy systems

## Summary of Qualifications

- 25 years of experience in developing enterprise and consumer applications
- Spec-driven and agent-assisted development, TDD, code review, refactoring, functional/E2E testing
- Cross-team collaboration, team coordination, coaching, mentoring
- English: B2 (Upper-Intermediate)

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
**Oct 2023 – Present**

**Key accomplishments**

- **Scope:** Carried the backend and the infrastructure of three mobile products in parallel — 100K+ to 1M+ users each — as the sole backend engineer on all three.
- **API ownership:** Designed the APIs the Android, iOS, and admin clients were built against, and negotiated their shape with the mobile teams.
- **System Stabilization & Recovery:** Recovered three legacy products to a deployable, stable state.
- **Documentation:** Kept the feature, API, and infrastructure documentation of all three products in Confluence, with PlantUML — the reference for QA and the mobile developers.
- **Testing & Reliability:** Introduced unit, integration, and E2E test suites; after that only isolated defects reached production.
- **Infrastructure:** Rebuilt logging and monitoring on Grafana and ELK, which made incidents diagnosable.

#### Project: NDA mobile call recording assistant, 1M+ users — Oct 2023 – Present
The backend for a mobile application for call recording and voice-to-text transcription.

**Key accomplishments**

- Owned every backend feature from design to release, plus the build, deployment, and production support.
- Took over a product spread over 30 repositories, with parts of it missing from version control and package versions out of sync.
- Recovered the missing pieces, realigned the dependencies, and restored the build and deployment of the whole application in about six months.
- Reworked the registration, purchase, and subscription handling, migrating the purchases to StoreKit 2.
- Identified several key features that had been missing and drove them to release.
- Wrote the operational runbook for recurring cases — troubleshooting, maintenance, analytics.

**Stack:** Microservices, TypeScript, Node.js, Express, Koa, MySQL, BullMQ, Redis, AWS, Docker

#### Project: NDA AI education assistant, 100K+ users — Oct 2023 – Mar 2026
The backend and admin site for the mobile homework assistant application.

**Key accomplishments**

- Owned the backend and the infrastructure, and drove the API for the mobile client and the admin site.
- Delivered cross-device synchronization of the solution history, an append-only log for spend analysis, and identity and attribution (Apple, Google, AppsFlyer).
- Led the admin site: built its foundation — monorepo, authentication, backend communication, state management, deployments — then reviewed, hardened, and released the frontend developers' work.
- Redesigned the LLM pipeline after the initial implementation proved unreliable.

**Stack:** TypeScript, Node.js, NestJS, OpenAPI, PostgreSQL, Redis, Prometheus, Grafana, AWS, Docker, Mocha, GitLab

#### Project: NDA fax transmission/reception, 1M+ users — Oct 2023 – Jul 2025

**Key accomplishments**

- Owned the backend and the infrastructure, from vendor integrations to production support, and set the direction for the mobile developers building against it.
- Took over a delivery path that failed on 10–20% of transmissions and brought the failure rate down to 5–10% within six months.
- Traced the causes across infrastructure, the database, and a long tail of defects; the unattended service restarts and application hangs stopped altogether.
- Reworked the pipeline behind the dead analytics — only then did the failures become traceable.
- Built fax reception end to end, including automated procurement of virtual numbers from the vendor.

**Stack:** TypeScript, Node.js, Koa, PostgreSQL, BullMQ, Redis, Prometheus, Grafana, AWS, Docker, Mocha

### Lead Software Engineer with multi-project focus — [Exadel](https://exadel.com/)
**Jun 2013 – Jul 2023**

**Key accomplishments**

- Mentored developers; all of them went on to senior roles, with one-on-one coaching running up to two years.
- Taught web application engineering at the Belarusian State University for two years on behalf of Exadel.
- Co-developed and rolled out the engineering grading system for a 1000+ person company — technical level assessment and career paths.
- Trained numerous engineers to ran the technical interviews.

#### Project: Inter-service communication platform — May 2019 – Jul 2023
An SDK platform unifying the API of internal long-lived RESTful services across the department.

**Key accomplishments**

- Owned the TypeScript/Node side of the platform SDK in a multi-stack team of six.
- Implemented the server-side OData SDK — parsing/interpretation/(de)serialization of a SQL-like query language.
- Built a server-side framework for the SDK to run against
- Optimized the SDK to performance parity with the .NET and Java implementations.
- Revamped the client library: restored it to working order, added OData 4, and gave it a query-builder DSL.
- For the sake of TDD wrote a matcher DSL library for partial expectations — making the growing suite readable.

**Stack:** TypeScript, Node.js, NestJS, Mocha, Apache Benchmark, GraphQL, Docker, AWS, Java, .NET

#### Project: An edge-service and microservice communication engine — May 2018 – Jul 2023
A micro-platform for rapid API building across backend, frontend, and microservices.

**Key accomplishments**

- Owned the framework from version 1.11 to 6.x: designed and implemented it end to end.
- Drove the direction the consuming teams needed: BFF and microservice support, instrumentation, call tracing.
- Carried the consuming teams through adoption and hardened the framework with every finding.
- Developed under TDD, with a test suite extensive enough to keep the major-version upgrades safe.

**Stack:** TypeScript, Express, Node.js, Mocha, Docker, GraphQL, AWS

#### Project: Generic search-based reference application — Jan 2018 – May 2019
The blueprint product teams started large corporate websites from.

**Key accomplishments**

- Redesigned the search module at the core of the application, built on the company's in-house search engine.
- Worked out how the platform should be tested, then migrated the existing suites to Cypress.
- Built the tracing through the platform, which made request flows diagnosable.

**Stack:** Angular, Redux, TypeScript, Node.js, Express, Web Components, Cypress, Docker

#### Project: Reader application for the worldwide publisher — Jun 2013 – Dec 2017
The multi-platform (Android, iOS, macOS, Windows) reader application integrated into the customer's ecosystem. Its users were lawyers.

**Key accomplishments**

- Owned the hardest modules: cross-platform API, full-text search, background processing, persistence.
- Optimized core processing for a proprietary book format, rendering ultra-large files that crashed most readers.
- Co-authored the application automation model, which let developers write plugin-like modules, e.g. renting.

**Stack:** Angular, TypeScript, WebSQL, Cordova, NW.js, Node.js

### Senior Software Developer — [VPI Systems Inc.](http://www.vpisystems.com/)
**Feb 2001 – May 2013**

#### OnePlan Transport™, Network Optimizer™, Network Configurator™, TransportMaker™, ServiceMaker™
The set of CAD-like software solutions for design, dimensioning, optimizing, planning of optical networks.

Selected accomplishments over the twelve years:
- Designed the application, domain, automation model and architecture behind them.
- Redesigned the network editor and 2D visualization to add analytic capabilities.
- Optimized the application for large-scale models: 10x less memory and CPU.

**Stack:** .NET 1.0–3.5, LINQ, NUnit, GDI+, DevExpress

## Education

**Engineer's degree in Computer Science: Belarusian State University of Informatics and Radioelectronics**, Minsk, Belarus — 2002
