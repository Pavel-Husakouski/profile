# Pavel Husakouski

[phusakouski@gmail.com](mailto:phusakouski@gmail.com) · [LinkedIn](https://www.linkedin.com/in/pavel-husakouski/) · +375 (29) 133-79-01 · [@Pauelito](https://t.me/Pauelito)

> I am proud of my contribution to all of the projects below. My attitude is the strongest of my skills!

## Summary of Qualifications

- 20+ years of experience in developing enterprise applications
- Strong understanding of software design and principles, architecture
- Programming practices — spec-driven and agent-assisted development, TDD, code review, refactoring, functional testing, E2E testing
- Good understanding and horizon in Computer Science
- Cross-team collaboration, team coordination, coaching, mentoring

Experience with:
- Node.js, NestJS, Express, AWS, GraphQL, OData, .NET
- Backend, Frontend, API, DSL, and framework design
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

- **Scope:** Carried the backend and the infrastructure of three mobile products in parallel — 1M+, 100K+, and 1M+ users — as the sole backend engineer on all three.
- **API ownership:** Designed the APIs the Android, iOS, and admin clients were built against, and negotiated their shape with the mobile and product teams.
- **System Stabilization & Recovery:** Recovered three legacy products to a deployable, stable state; the measured outcomes are in the project sections below.
- **Documentation:** Maintained the feature, API, and infrastructure documentation for all three products in Confluence, with PlantUML diagrams for flows and integrations — the single reference that kept QA, the Android and iOS developers, and product on the same picture of the system.
- **Testing & Reliability:** Introduced unit, integration, and E2E test suites across the three products; after that only isolated defects reached production.
- **Infrastructure:** Rebuilt the logging and monitoring of the products, on Grafana and ELK respectively, to make production incidents diagnosable.

#### Project: NDA mobile call recording assistant, 1M+ users — 10.2023 – present
The backend for a mobile application for call recording and voice-to-text transcription.

**Key accomplishments:**

- Sole backend engineer on the product: owned every backend feature from design to release, together with the build, deployment, and production support behind it.
- Took over a product with severe issues: code spread over 30 repositories, parts of it missing from version control entirely, and package versions drifted apart across services.
- Recovered the missing pieces, realigned the dependencies, and restored the build and deployment of the whole application in about six months.
- Reworked the registration, purchase, and subscription handling, migrating the purchases to StoreKit 2.
- Identified several key features that had been missing and drove them to release.
- Wrote the operational runbook for the product — analytics, troubleshooting, maintenance, and debugging — with a script behind each recurring case.

**Stack:** Microservices, TypeScript, Node.js, Express, Koa, MySQL, BullMQ, Redis, AWS, Docker, Postman

#### Project: NDA AI education assistant, 100K+ users — 10.2023 – 03.2026
The backend and admin site for the mobile homework assistant application.

**Key accomplishments:**

- Sole backend engineer on the product: owned the backend and the infrastructure, and drove the API the mobile client and the admin site were built against.
- Delivered cross-device synchronization of the solution history, an append-only log for spend analysis, and third-party identity and attribution (Sign in with Apple and Google, AppsFlyer).
- Led the admin site: owned the design of the solution, bootstrapped the application and implemented its foundation — monorepo, authentication, backend communication, state management, builds and deployments — then reviewed, hardened, and released the features implemented by the frontend developers.
- Redesigned the LLM pipeline after the initial implementation proved unreliable.

**Stack:** TypeScript, Node.js, NestJS, OpenAPI, PostgreSQL, Redis, Prometheus, Grafana, AWS, Docker, Mocha, Postman, GitLab CI/CD

#### Project: NDA fax transmission/reception, 1M+ users — 10.2023 – 07.2025
The backend for a mobile fax application.

**Key accomplishments:**

- Sole backend engineer on the product: owned the backend and the infrastructure, from the vendor integrations to production support, and set the technical direction for the mobile developers building against it.
- Took over a delivery path that failed on 10–20% of transmissions and brought the failure rate down to 5–10% within six months.
- Traced the causes across infrastructure, the database, and a long tail of defects; the unattended service restarts and application hangs stopped altogether.
- Recovered the delivery analytics, which had stopped working, then reworked and optimized the pipeline behind it — the failures only became traceable after that.
- Built fax reception end to end, including automated procurement of virtual numbers from the telephony vendor.

**Stack:** TypeScript, Node.js, Koa, PostgreSQL, BullMQ, Redis, Prometheus, Grafana, AWS, Docker, Mocha, Postman

### Lead Software Engineer with multi-project focus — [Exadel](https://exadel.com/)
**06.2013 – 07.2023**

**Key accomplishments:**

- Mentored developers on every project of the decade — many of them went on to senior positions, and several I coached one-on-one for as long as two years each.
- Taught at the Belarusian State University for two years on behalf of Exadel.
- Co-developed and rolled out the engineering grading system for a 1000+ person company: how technical level was assessed, and how career paths were laid out for the engineers.
- Trained the engineers who ran the technical interviews.

#### Project: Inter-service communication platform — 05.2019 – 07.2023
An SDK platform for cross-service communication. The purpose is to unify the API of internal long-lived RESTful services within the large department. Used by numerous product teams.

**Key accomplishments:**

- Owned the TypeScript and Node.js side of the platform among six engineers, each covering a different stack — shared code review, the common test suites, and troubleshooting.
- Single-handedly implemented the server-side OData protocol SDK — parsing, interpretation, and (de)serialization of the SQL-like query language — and designed the framework built on top of it; the architecture is mine. OData is a large and intricate specification, and this was the most demanding engineering work of my career.
- Built it under TDD, with an extensive suite pinning the behavior of the protocol down to its edge cases.
- Revived the abandoned legacy client, brought it back to its former glory, added OData 4, and gave it a new query builder.
- Optimized and polished the OData pipeline architecture, achieving performance parity with native .NET and Java implementations for large-scale data processing.

**Stack:** TypeScript, Node.js, NestJS, Mocha, Apache Benchmark, GraphQL, Docker, AWS, Postman, Fiddler, Maven, Java, .NET, Jenkins, Confluence, Jira

#### Project: An edge-service and microservice communication engine — 05.2018 – 07.2023
A micro-platform for rapid API building that simplifies backend, frontend, and microservice integration. Used by numerous product teams.

**Key accomplishments:**

- Owned the framework from version 1.11 to 6.x: designed and implemented it end to end, and shipped every major version.
- Drove the technical direction the consuming teams needed: adaptation for microservices, instrumentation, call tracing, features, and performance work.
- Guided the product teams through adoption: documented the use cases, reviewed the solutions they built on top of the framework, and helped them troubleshoot.
- Hardened the framework with what the troubleshooting turned up, so the next team would not meet the same problem.
- Developed under TDD, with a test suite extensive enough to keep the major-version upgrades safe.

**Stack:** TypeScript, Express, Node.js, Mocha, Docker, GraphQL, AWS, Postman, Fiddler, Atlassian CI, Confluence, Jira

#### Project: Generic search-based reference application — 01.2018 – 05.2019
A reference application for large-scale corporate websites — the blueprint and starting point product teams used to get a typical large project off the ground quickly.

**Key accomplishments:**

- Redesigned the search module at the core of the application, built on the company's in-house search engine.
- Owned the testing approach: worked out how the platform should be tested, then migrated the existing suites to Cypress.
- Built the tracing through the platform in-house, wired to the tooling already in place, which made request flows diagnosable.

**Stack:** Angular, Redux, TypeScript, Node.js, Express, Web Components, Cypress, JSX, HTTP, Git, Jira, Atlassian CI, Docker

#### Project: Reader application for the worldwide publisher — 06.2013 – 12.2017
The multi-platform (Android, iOS, MacOS, Windows) reader application integrated into the Customer's ecosystem. Its main users were lawyers of all kinds.

**Key accomplishments:**

- Owned the hardest modules of the application from design through maintenance: the cross-platform API, full-text search, HTTP client, epub conversion and instrumentation, background task scheduler, persistence layer, and diagnostics.
- Optimized core processing for a proprietary book format, enabling seamless rendering of ultra-large files that previously caused most native reading applications to crash.

**Stack:** Angular, TypeScript, WebSQL, Cordova, NW.js, Node.js, HTTP, Git, Jira

### Side project: A warehouse automation startup for an automotive dealer
**01.2008 – 01.2009**

An independent startup, taken on as a side project to go deep on databases. The product covered warehouse automation and an offline trading assistant for the dealer's managers.

**Stack:** .NET, MS SQL Server

### Senior Software Developer — [VPI Systems Inc.](http://www.vpisystems.com/)
**02.2001 – 05.2013**

#### Projects: VPI OnePlan Transport™, VPI Network Optimizer™, VPI Network Configurator™, VPI TransportMaker™, VPI ServiceMaker™
The set of CAD-like software solutions for design, dimensioning, optimizing, planning of optical networks.

**Selected accomplishments over the twelve years:**
- Designed the domain and application model and the architecture behind it, and implemented the internal DSL on top of it.
- Automated the applications with scripting built on that model, so design and analysis work could be driven programmatically instead of through the UI.
- Redesigned and reimplemented the network editor and visualization (2D rendering) and the what-if, hierarchical, and routing analyses, along with the import/export, reporting, and persistence APIs.
- Optimized model architecture and runtime memory efficiency, achieving a 10x reduction in memory footprint and CPU consumption for large-scale models and complex computations.

**Stack:** .NET 1.0–3.5, LINQ, NUnit, GDI+, DevExpress, Redgate ANTS Profiler, JetBrains dotTrace, Visual Studio, SSCLI, .NET Reflector

## Education

**Engineer's degree in Computer Science: Belarusian State University of Informatics and Radioelectronics**, Minsk, Belarus — 2002
