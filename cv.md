# Pavel Husakouski
[phusakouski@gmail.com](mailto:phusakouski@gmail.com) · [LinkedIn](https://www.linkedin.com/in/pavel-husakouski/) · +375(29)133-79-01 · [@Pauelito](https://t.me/Pauelito) · Minsk, Belarus · Office or remote

**Senior Backend Engineer (TypeScript/Node.js)** — platform SDKs, recovery of legacy systems

## Professional Summary

- 25 years in software engineering: 10 at a services company building platforms and frameworks for other engineering teams, 3 as the sole backend engineer of three consumer mobile products.
- Build what others depend on — an OData SDK and framework, a microservice communication engine shipped from 1.11 to 6.x, API contracts for Android, iOS, and admin clients.
- Recover broken systems: a product spread over 30 repositories restored to a deployable state, fax delivery failures cut from 10–20% to 5–10%, an abandoned OData client revived.
- Technical coordination without a management title: specifications, recorded decisions, and settled ownership across mobile, QA, and product.
- Set engineering standards beyond my own code: the grading system for a 1000+ person company, interviewer training, two years of university teaching.

## Skills

**Backend** TypeScript, Node.js, NestJS, Express, Koa, REST, GraphQL, OData, microservices, distributed systems, SDK and framework design
**AI** Claude Code, GitHub Copilot, spec-driven development; OpenAI, Anthropic, Gemini APIs
**Telephony** Telnyx, Twilio, Plivo, Documo, etc.
**Data** PostgreSQL, MySQL, Redis, DynamoDB, Elasticsearch, SQL
**Async** BullMQ, NATS
**Cloud and CI/CD** AWS, Docker, GitLab CI/CD
**Observability** Grafana, Prometheus, ELK, Kibana, tracing
**Testing** TDD, unit testing, integration testing, E2E, Mocha, Cypress
**Also** C#, .NET, Python, C++, Angular, Vue.js, Pinia
**Languages** English — B2 (Upper-Intermediate), Russian — Native

## Professional Experience

### Backend Software Engineer — AlpariGroup
**Oct 2023 – Present**

- **Scope:** Carried the backend and the infrastructure of three mobile products in parallel — 100K+ to 1M+ users each, tens of thousands of lines each — as the sole backend engineer for five mobile developers and up to three QA.
- **API ownership:** Designed and negotiated the shape of APIs for Android, iOS, and admin clients.
- **Recovery:** Recovered three legacy products to a deployable, stable state.
- **AI in the workflow:** Wrote the specification first, then drove Claude Code and GitHub Copilot against it through implementation and review — roughly halving the time from design to delivery on feature work.
- **Documentation:** Wrote the feature, API, and infrastructure documentation of all three products in Confluence and PlantUML — the reference for QA and the mobile teams.
- **Testing:** Introduced unit, integration, and E2E test suites; after that only isolated defects reached production.
- **Infrastructure:** Rebuilt logging and monitoring on Grafana and ELK, which made incidents diagnosable; DevOps provisioned the resources, everything running on them was backend work.

#### Project: NDA mobile call recording assistant, 1M+ users — Oct 2023 – Present
The backend for a mobile application for call recording and voice-to-text transcription.

- Inherited a product in 30 repositories, with code missing from version control and package versions out of sync.
- Recovered the missing pieces, dependencies, and restored the whole build and deployment.
- Reworked the registration, purchase, and subscription handling, migrating the purchases to StoreKit 2.
- Identified several key features that had been missing and drove them to release.
- Wrote the operational runbook for recurring cases — troubleshooting, maintenance, analytics.

**Stack:** Microservices, TypeScript, Node.js, Express, Koa, MySQL, BullMQ, Redis, NDA vendors, AWS, Docker

#### Project: NDA AI education assistant, 100K+ users — Oct 2023 – Mar 2026
The backend and admin site for the mobile homework assistant application.

- Owned the backend and the infrastructure, and drove the API for the mobile client and the admin site.
- Built the request audit trail and the analytics over it — spend traceable to the users and requests behind them.
- Led the admin site: built its foundation, then reviewed, hardened, and released the frontend developers' work.
- Redesigned the LLM pipeline: the crashes, the hangs, and the truncated answers stopped.

**Stack:** TypeScript, Node.js, NestJS, OpenAPI, PostgreSQL, Redis, Prometheus, Grafana, AWS, Docker, Mocha, GitLab

#### Project: NDA fax transmission/reception, 1M+ users — Oct 2023 – Jul 2025

- Owned the backend and the infrastructure, from three telephony vendor integrations to production support, and set the direction for the mobile developers building against it.
- Took over a delivery path that failed on 10–20% of transmissions and brought it down to the 5–10% baseline.
- Traced the restarts and hangs to infrastructure, the database, and a long tail of defects, and ended them.
- Reworked the pipeline behind the dead analytics — only then did the failures become traceable.
- Built fax reception end to end, including automated procurement of virtual numbers from the vendors.

**Stack:** TypeScript, Node.js, Koa, PostgreSQL, BullMQ, Redis, NDA vendors, Prometheus, Grafana, AWS, Docker, Mocha

### Lead Software Engineer — [Exadel](https://exadel.com/)
**Jun 2013 – Jul 2023**

- Mentored software engineers; several reached senior roles, some after two years of one-on-one coaching.
- Taught web application engineering at the Belarusian State University for two years on behalf of Exadel.
- Architected the engineering grading system, assessment and career paths for a 1000+ person company.
- Trained the engineers who conducted the technical interviews.

#### Project: Inter-service communication platform — May 2019 – Jul 2023
An SDK platform unifying the API of long-lived RESTful services across the department — dozens of product teams.

- Owned the TypeScript/Node side of the platform SDK - 100K+ lines - in a multi-stack team of six.
- Implemented the server-side OData SDK — parsing/interpretation/(de)serialization of a SQL-like query language.
- Built a server-side framework for the SDK to run against.
- Optimized the SDK to performance parity with the .NET and Java implementations.
- Revived the abandoned client library: the code generation and the build were broken, the protocol version and the feature set lagged the .NET and Java clients, and the typings had holes.
- Closed the gap with the other platforms, added OData 4, and gave it a query-builder DSL.
- For the sake of TDD wrote a matcher DSL library for partial expectations — making the growing suite readable.

**Stack:** TypeScript, Node.js, NestJS, Mocha, Apache Benchmark, GraphQL, Docker, AWS, Java, .NET

#### Project: An edge-service and microservice communication engine — May 2018 – Jul 2023
A micro-platform for rapid API building across backend, frontend, and microservices.

- Owned the framework from version 1.11 to 6.x: designed and implemented it end to end.
- Drove the direction the consuming teams needed: BFF and microservice support, instrumentation, call tracing.
- Carried dozens of consuming teams through adoption and hardened the framework with every finding.
- Developed under TDD, with a test suite extensive enough to keep the major-version upgrades safe.

**Stack:** TypeScript, Express, Node.js, Mocha, Docker, GraphQL, AWS

#### Project: Generic search-based reference application — Jan 2018 – May 2019
The blueprint product teams started large corporate websites from.

- Redesigned the search module at the core of the application, built on the company's in-house search engine.
- Built the tracing through the platform, which made request flows diagnosable.

**Stack:** Angular, Redux, TypeScript, Node.js, Express, Web Components, Cypress, Docker

#### Project: Reader application for the worldwide publisher — Jun 2013 – Dec 2017
A reader for lawyers, shipped on Android, iOS, macOS, and Windows, integrated into the customer's ecosystem.

- Owned the hardest modules: cross-platform API, full-text search, background processing, persistence.
- Optimized core processing for a proprietary book format, rendering ultra-large files that crashed most readers.
- Co-authored the application automation model, which let developers write plugin-like modules, e.g. renting.

**Stack:** Angular, TypeScript, WebSQL, Cordova, NW.js, Node.js

### Senior Software Developer — [VPI Systems Inc.](http://www.vpisystems.com/)
**Feb 2001 – May 2013**

#### OnePlan Transport, Network Optimizer, Network Configurator, TransportMaker, ServiceMaker
CAD-like software for design, dimensioning, optimization, and planning of optical networks.

- Designed the application, domain, automation model and architecture behind them.
- Redesigned the network editor and 2D visualization to add analytic capabilities.
- Optimized the application for large-scale models: 10x less memory and CPU.

**Stack:** .NET 1.0–3.5, LINQ, NUnit, GDI+, DevExpress

## Education

**Engineer's degree in Computer Science** — Belarusian State University of Informatics and Radioelectronics, 2002
