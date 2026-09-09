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
**10.2023 – 10.2026**

**Key accomplishments:**

- **Scope:** Carried the backend and the infrastructure of three mobile products in parallel — 1M+, 100K+, and 1M+ users — as the sole backend engineer on all three.
- **API ownership:** Designed the APIs the Android, iOS, and admin clients were built against, and negotiated their shape with the mobile and product teams.
- **System Stabilization & Recovery:** Recovered three legacy products to a deployable, stable state; the measured outcomes are in the project sections below.
- **Documentation:** Maintained the feature, API, and infrastructure documentation for all three products in Confluence, with PlantUML diagrams for flows and integrations — the single reference that kept QA, the Android and iOS developers, and product on the same picture of the system.
- **Testing & Reliability:** Introduced unit, integration, and E2E test suites across the three products; after that only isolated defects reached production.
- **Infrastructure:** Rebuilt the logging and monitoring of the products, on Grafana and ELK respectively, to make production incidents diagnosable.

#### Project: NDA mobile call recording assistant, 1M+ users — 10.2023 – 10.2026
The backend for a mobile application for call recording and voice-to-text transcription.

**Key accomplishments:**

- Sole backend engineer on the product: owned every backend feature from design to release, together with the build, deployment, and production support behind it.
- Took over a product with severe issues: code spread over 30 repositories, parts of it missing from version control entirely, and package versions drifted apart across services.
- Recovered the missing pieces, realigned the dependencies, and restored the build and deployment of the whole application in about six months.
- Reworked the registration, purchase, and subscription handling, migrating the purchases to StoreKit 2.
- Identified several key features that had been missing and drove them to release.
- Covered the routine maintenance and debugging cases with scripting.

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
**09.2010 – 07.2023**

#### Project: Inter-service communication platform — 05.2019 – 07.2023
An SDK platform for cross-service communication. The purpose is to unify the API of internal long-lived RESTful services within the large department. Used by numerous product teams.

**Key accomplishments:**

- Single-handedly implemented the OData protocol SDK (SQL-like query language, both client and server) and a framework on top of it, including parsing, interpretation, and (de)serialization.
- Optimized and polished the OData pipeline architecture, achieving performance parity with native .NET and Java implementations for large-scale data processing.

**Stack:** TypeScript, Node.js, NestJS, Mocha, GraphQL, Docker, AWS, Postman, Fiddler, Maven, Jenkins, Jira

#### Project: An edge-service and microservice communication engine — 05.2018 – 07.2023
A micro-platform for rapid API building that simplifies backend, frontend, and microservice integration. Used by numerous product teams.

**Key accomplishments:** End-to-end design and implementation of the framework.

**Stack:** TypeScript, Express, Node.js, Mocha, Docker, GraphQL, AWS, RabbitMQ, Postman, Fiddler, Atlassian CI, Jira

#### Project: Generic search-based software application — 01.2018 – 05.2019
The purpose of the application is to facilitate the easy creation of large-scale corporate websites.

**Responsibilities included:** Meetings; Workshops; Problem-solving and troubleshooting; Platform API design and implementation; Business logic implementation; E2E architecture, bootstrapping, guide, and monitoring; Code review; Unit testing; Integration testing; E2E testing.

**Stack:** Angular, Redux, TypeScript, Node.js, Express, Web Components, Cypress, JSX, HTTP, Git, Jira, Atlassian CI, Docker

#### Project: Reader application for the worldwide publisher — 06.2013 – 12.2017
The multi-platform (Android, iOS, MacOS, Windows) reader application integrated into the Customer's ecosystem. Its main users were lawyers of all kinds.

**Key accomplishments:**

- Design and implementation of complicated components — cross-platform API, full-text search, HTTP client, epub conversion and instrumentation, background task scheduler, persistence layer, and diagnostics.
- Optimized core processing for a proprietary book format, enabling seamless rendering of ultra-large files that previously caused most native reading applications to crash.

**Responsibilities included:** Meetings; Problem-solving and troubleshooting; Requirements analysis; Code review; Mentoring and coaching; Cross-platform layer design and maintenance.

**Stack:** Angular, TypeScript, WebSQL, Cordova, NW.js, Node.js, HTTP, Git, Jira

### Senior Software Developer — NDA company
**01.2008 – 01.2009**

#### Project: Warehouse automation software
A warehouse application and the offline trading assistant for the automotive dealer. This application enabled managers to easily place orders, reserve commodities, and manage returns and transfers.

**Stack:** .NET, MS SQL Server, MS Access

### Senior Software Developer — [VPI Systems Inc.](http://www.vpisystems.com/)
**02.2001 – 07.2011**

#### Projects: VPI OnePlan Transport™, VPI Network Optimizer™, VPI Network Configurator™, VPI TransportMaker™, VPI ServiceMaker™
The set of CAD-like software solutions for design, dimensioning, optimizing, planning of optical networks.

**Key accomplishments:**

- Design and implementation of the network editor and visualization (2D rendering); Analysis: what-if, hierarchical, routing; Import/export, reporting and persistence API redesign; Domain and application model design; Internal DSL implementation.
- Optimized model architecture and runtime memory efficiency, achieving a 10x reduction in memory footprint and CPU consumption for large-scale models and complex computations.

**Responsibilities included:** Design, implementation, performance tuning, prototyping; TDD, unit testing, refactoring; resurrection of the legacy codebase.

**Stack:** .NET 1.0–3.5, LINQ, MSTest, NUnit, DevExpress, GDI+, XML, Redgate ANTS Profiler, JetBrains dotTrace, Visual Studio, SSCLI, .NET Reflector

## Education

**MC CS: Belarusian State University of Informatics and Radioelectronics**, Minsk, Belarus — 2002

## Recommendations from my colleagues

**[Olga Belaya](https://www.linkedin.com/in/belayaolga) — Human Resources Director, HR Consultant**
It was a great pleasure working with Pavel on this huge project of developing and implementing a grading system at Exadel (1000+ employees). Pavel's experience and wide technical outlook helped us to create and evolve the approach to evaluating technical level and creating development plan and clear career path for employees.

**[Alexey Nesteruk](https://www.linkedin.com/in/anesteruk) — Delivery Manager at Exadel**
As both my mentor and teammate on the same project, Pavel's dedication and expertise have left a lasting impact on both the project's success and my professional growth. Patient, approachable, and always willing to share knowledge, he fostered a collaborative environment where ideas flourished, and learning was encouraged. His mentorship not only enhanced my coding abilities but also instilled a sense of confidence and a passion for continuous improvement.

**[Olga Chikvina](https://www.linkedin.com/in/olga-chikvina-88652033) — Front-end developer at Exadel**
Pavel has a professional approach and strong opinion on how the things should be implemented and always can justify it. I learnt a lot from Pavel when we were in one team as he's always glad to help, share knowledge, teach and at the same time open to new things to learn.

**[Siarhei Aksiuchenka](https://www.linkedin.com/in/siarhei-aksiuchenka-19aa6067) — Lead Product Software Engineer at Wolters Kluwer**
I worked along with Pavel for many years on different jobs. He is a truly highly skilled Engineer. Pavel would easily crack any hard-to-solve problem. I've seen it countless times. If you are considering him to fill a position, don't wait. Hire sooner than later while Pavel didn't accept someone else's offer.

**[Jan Arend Jansen](https://www.linkedin.com/in/janarend) — Director of Architecture and Engineering at Wolters Kluwer**
Pavel has been a pleasure to work with. On my project he has single handedly developed an Api development sdk for Javascript matching functionality with existing sdks for Java and dotnet. He is a great guy, who cares for the results he produces and is helpful to others. He works well alone and in a team. I highly recommend Pavel.

**[Przemysław Pankowski](https://www.linkedin.com/in/przemys%C5%82aw-pankowski-profile) — Software Engineer at ArdentCode**
Pavel is a true professional and a man of dedication. His experience in building tools and frameworks, which also requires a good understanding of what your users are up to, makes him a valuable asset for any team.

**[Andrey Borozdin](https://www.linkedin.com/in/andreyborozdin) — Software Development Manager at Exadel**
Pavel is an expert in object-oriented design and application architecture, and he was always ready to share his knowledge and insights with other developers on our team. Pavel is not only a great developer, but also a great mentor and leader. He has a positive attitude, a strong work ethic, and a passion for excellence. He is extremely valuable to any team and I highly recommend him.

**[Siarhei Astapovich](https://www.linkedin.com/in/sastapovich) — Lead Application & Product Architect at Wolters Kluwer**
One of Pavel's standout attributes is his ability to mentor and guide others. He goes above and beyond to share his knowledge generously with team members, fostering a culture of continuous learning and growth within the organization. His approachable demeanor and patience make him an approachable mentor for colleagues of all experience levels.
