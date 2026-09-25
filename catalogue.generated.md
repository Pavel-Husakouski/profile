Contacts:

  Name: Pavel Husakouski
  Title: Senior Backend Engineer (TypeScript/Node.js)
  Focus: platform SDKs, recovery of legacy systems
  Email: phusakouski@gmail.com
  LinkedIn: https://www.linkedin.com/in/pavel-husakouski/
  Phone: +375(29)133-79-01
  Telegram: https://t.me/Pauelito
  Location: Minsk, Belarus
  Work format: Office or remote

Professional Summary:

  - 25 years in software engineering: 10 at a services company building platforms and frameworks for other engineering teams, 3 as the sole backend engineer of three consumer mobile products.
  - Build what others depend on: an OData SDK and framework, a microservice communication engine shipped from 1.11 to 6.x, API contracts for Android, iOS, and admin clients.
  - Recover broken systems: restored a product spread across 30 repositories to a deployable state, cut fax delivery failures from 10–20% to 5–10%, revived an abandoned OData client.
  - Technical coordination without a management title: specifications, recorded decisions, and settled ownership across mobile, QA, and product.
  - Set engineering standards beyond my own code: the grading system for a 1000+ person company, interviewer training, two years of university teaching.

Skills:

  - Backend: TypeScript, Node.js, NestJS, Express, Koa, REST, GraphQL, OData, microservices, distributed systems, SDK and framework design.
  - AI: Claude Code, GitHub Copilot, spec-driven development, OpenAI, Anthropic, Gemini APIs.
  - Telephony: Telnyx, Twilio, Plivo, Documo, SrFax, Nexmo, Avoxi.
  - Data: PostgreSQL, MySQL, Redis, DynamoDB, Elasticsearch, SQL.
  - Async: BullMQ, NATS.
  - Cloud and CI/CD: AWS, Docker, GitLab CI/CD.
  - Observability: Grafana, Prometheus, ELK, Kibana, tracing.
  - Testing: TDD, unit testing, integration testing, E2E, Mocha, Cypress.
  - Also: Vue.js, Pinia, Angular, C#, .NET, Python, C++.
  - Languages: English — B2 (Upper-Intermediate), Russian — Native.

Professional Experience:

  Position: Backend Software Engineer, AlpariGroup
    Period: Oct 2023 – Present

    Key accomplishments:
      - Carried the backend and the infrastructure of three mobile products in parallel — 100K+ to 1M+ users each, tens of thousands of lines each — as the sole backend engineer for five mobile developers and up to three QA.
      - Designed and negotiated the shape of APIs for Android, iOS, and admin clients.
      - Recovered three legacy products to a deployable, stable state.
      - Integrated AI tooling (Claude Code and GitHub Copilot) into spec-driven development, cutting feature delivery time by ~50%.
      - Authored the feature, API, and infrastructure documentation (Confluence and PlantUML) used as the reference by QA and the mobile teams.
      - Introduced unit, integration, and E2E test suites; post-deployment defects dropped to isolated edge cases.
      - Owned and rebuilt logging and monitoring (Grafana, ELK), making incidents diagnosable.

    Project: mobile call recording assistant, 1M+ users
      Period: Oct 2023 – Present
      Summary: The backend for a mobile application for call recording and voice-to-text transcription.

      Key accomplishments:
        - Inherited a product fragmented across 30 repositories, with code missing from version control and package versions adrift; reconstructed the missing pieces and restored the build and deployment of the whole application.
        - Reworked the registration, purchase, and subscription handling, migrating the purchases to StoreKit 2.
        - Identified several key features that had been missing and drove them to release.
        - Wrote the operational runbook for recurring cases — troubleshooting, maintenance, analytics.

      Stack: Microservices, TypeScript, Node.js, Express, Koa, MySQL, BullMQ, Redis, NDA vendors, AWS, Docker

    Project: AI education assistant, 100K+ users
      Period: Oct 2023 – Mar 2026
      Summary: The backend and admin site for the mobile homework assistant application.

      Key accomplishments:
        - Owned the backend and the infrastructure, and drove the API for the mobile client and the admin site.
        - Built the audit trail and the analytics over it, making spend on every paid service traceable to users and requests.
        - Led the admin site: built its foundation, then reviewed, hardened, and released the frontend developers' work.
        - Redesigned the LLM pipeline: the crashes, the hangs, and the truncated answers stopped.

      Stack: TypeScript, Node.js, NestJS, OpenAPI, PostgreSQL, Redis, Prometheus, Grafana, AWS, Docker, Mocha, GitLab

    Project: fax transmission/reception, 1M+ users
      Period: Oct 2023 – May 2025
      Summary: The backend and infrastructure for a consumer fax application built on three telephony vendors.

      Key accomplishments:
        - Owned it from the vendor integrations to production support, and set the direction for the mobile developers building against the API.
        - Took over a delivery path that failed on 10–20% of transmissions and brought it down to the 5–10% baseline.
        - Diagnosed and resolved infrastructure instability, database bottlenecks, and defect backlog causing restarts and hangs.
        - Reworked the pipeline behind the dead analytics — only then did the failures become traceable.
        - Built fax reception end-to-end, including automated procurement of virtual numbers from the vendors.

      Stack: TypeScript, Node.js, Koa, PostgreSQL, BullMQ, Redis, NDA vendors, Prometheus, Grafana, AWS, Docker, Mocha

  Position: Lead Software Engineer, Exadel
    Period: Jun 2013 – Aug 2023

    Key accomplishments:
      - Mentored software engineers; several reached senior roles, some after two years of one-on-one coaching.
      - Taught web application engineering at the Belarusian State University for two years on behalf of Exadel.
      - Architected the engineering grading system, assessment, and career paths for a 1000+ person company.
      - Trained the engineers who conducted the technical interviews.

    Project: Inter-service communication platform
      Period: May 2019 – Jul 2023
      Summary: An SDK platform unifying the API of long-lived RESTful services across the department's dozens of product teams.

      Key accomplishments:
        - Owned the TypeScript/Node side of the platform SDK — 100K+ lines — in a multi-stack team of six.
        - Implemented the server-side OData SDK — parsing/interpretation/(de)serialization of a SQL-like query language.
        - Built a server-side framework for the SDK to run against.
        - Optimized the SDK to achieve performance parity with the .NET and Java implementations.
        - Revived the abandoned OData client: fixed the broken code generation and build, brought it to OData 4 and feature parity with the .NET and Java clients, and added a query-builder DSL.
        - Wrote an asymmetric matcher DSL library for partial expectations under TDD, keeping the suite readable as it grew.

      Stack: TypeScript, Node.js, NestJS, Mocha, Apache Benchmark, GraphQL, Docker, AWS, Java, .NET

    Project: An edge-service and microservice communication engine
      Period: May 2018 – Jun 2023
      Summary: A micro-platform for rapid API building across backend, frontend, and microservices.

      Key accomplishments:
        - Owned the framework from version 1.11 to 6.x: designed and implemented it end-to-end.
        - Drove the framework roadmap from what the consuming teams needed: BFF and microservice support, instrumentation, distributed call tracing.
        - Carried dozens of consuming teams through adoption and hardened the framework with every finding.
        - Developed under TDD, with a test suite extensive enough to keep the major-version upgrades safe.

      Stack: TypeScript, Express, Node.js, Mocha, Docker, GraphQL, AWS

    Project: Generic search-based reference application
      Period: Jan 2018 – May 2019
      Summary: The blueprint product teams used to build large corporate websites.

      Key accomplishments:
        - Redesigned the search module at the core of the application, built on the company's in-house search engine.
        - Built platform-wide tracing, making request flows diagnosable.

      Stack: Angular, Redux, TypeScript, Node.js, Express, Web Components, Cypress, Docker

    Project: Reader application for a worldwide publisher
      Period: Jun 2013 – Dec 2017
      Summary: A reader for lawyers, shipped on Android, iOS, macOS, and Windows, integrated into the customer's ecosystem.

      Key accomplishments:
        - Owned the hardest modules: cross-platform API, full-text search, background processing, persistence.
        - Built the in-house converter for the proprietary book format (SAX/DOM parsing, rendering, optimization), enabling ultra-large files to render where competing readers crashed.
        - Co-authored the application automation model, which let developers write plugin-like modules, e.g., renting.

      Stack: Angular, TypeScript, WebSQL, Cordova, NW.js, Node.js

  Position: Senior Software Developer, VPI Systems Inc.
    Period: Feb 2001 – Feb 2013

    Project: OnePlan Transport, Network Optimizer, Network Configurator, TransportMaker
      Summary: CAD-like software for designing, dimensioning, optimizing, and planning optical networks.

      Key accomplishments:
        - Designed the application, domain, automation model, and architecture behind them.
        - Redesigned the network editor and 2D visualization to add analytic capabilities.
        - Optimized the application for large-scale models: 10x less memory and CPU.

      Stack: .NET 1.0–3.5, LINQ, NUnit, GDI+, DevExpress

Education:

  University: Belarusian State University of Informatics and Radioelectronics
  Degree: Engineer's degree
  Field: Computer Science
  Years: 1995 – 2002
