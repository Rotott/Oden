# ODEN Technology

[← Back to README](../README.md)

## Table of Contents

- [Document purpose](#document-purpose)
- [Technology Status](#technology-status)
- [Technology Stack](#technology-stack)
- [Backend](#backend)
  - [Python](#python)
  - [Ruff](#ruff)
  - [Pyright](#pyright)
  - [FastAPI](#fastapi)
  - [pytest](#pytest)
- [Database](#database)
  - [SQLite](#sqlite)
  - [SQLAlchemy](#sqlalchemy)
- [Frontend](#frontend)
  - [React](#react)
  - [React Native (Expo)](#react-native-expo)
  - [TypeScript](#typescript)
  - [ESLint](#eslint)
  - [Prettier](#prettier)
  - [Jest](#jest)
  - [Vite](#vite)
  - [Tailwind CSS](#tailwind-css)
- [Desktop Wrapper](#desktop-wrapper)
  - [Tauri](#tauri)
- [AI & Audio Processing](#ai--audio-processing)
  - [PyTorch](#pytorch)
  - [Local Speech-to-Text](#local-speech-to-text)
  - [Local LLM Runtime](#local-llm-runtime)
- [Workflow Engine](#workflow-engine)
  - [FlowKit](#flowkit)
- [Testing & Quality Assurance](#testing--quality-assurance)
  - [Playwright](#playwright)
- [CI/CD](#cicd)
  - [GitHub Actions](#github-actions)
  - [Mermaid](#mermaid)
- [Technology Selection Principles](#technology-selection-principles)

---

## Document purpose

This document describes the technologies used or planned for ODEN, along with their current status and intended purpose.

Supported operating systems, runtime versions, hardware requirements, and development environment requirements are defined in the [Supported Environments](development/supported-environments.md) document.

Technology choices may change as the project develops. Major changes should be reflected in this document.

---

## Technology Status

The following status labels are used in this document:

| Status | Meaning |
| :--- | :--- |
| **Planned** | Intended to be used, but implementation may not yet exist |
| **Implemented** | Currently used by the project |
| **TBD** | No final decision has been made |
| **Deprecated** | Previously used or planned, but no longer intended for use |

Technology decisions should be updated as ODEN progresses through its milestones.

---

## Technology Stack

| Area | Technology | Status | Purpose |
| :--- | :--- | :--- | :--- |
| **Backend** | Python 3.11+ | Planned | Core application and backend logic |
| **Backend API** | FastAPI | Planned | HTTP API and backend services |
| **Backend Testing** | pytest | Planned | Backend testing |
| **Backend Linting / Formatting** | Ruff | Implemented | Python linting and code formatting |
| **Backend Type Checking** | Pyright | Implemented | Python static type checking |
| **Database** | SQLite | Planned | Local application data storage |
| **ORM** | SQLAlchemy | **TBD** | Database abstraction and data access |
| **Frontend** | React | Planned | User interface |
| **Frontend Language** | TypeScript | Planned | Type-safe frontend development |
**Frontend Mobile** | React Native (Expo) | **TBD** | Cross-platform mobile GUI (iOS/Android) sharing logic with web 
| **Frontend Runtime / Tooling** | Node.js | Planned | Runs frontend development and build tools |
| **Frontend Linting** | ESLint | Implemented | Static analysis and code quality checks |
| **Frontend Formatting** | Prettier | Implemented | Consistent frontend code formatting |
| **Frontend Testing** | Jest **OR** Vitest | **TBD** | Automated frontend/unit testing |
| **Build Tooling** | Vite | **TBD** | Frontend development and build tooling |
| **Styling** | Tailwind CSS | **TBD** | Frontend styling |
**Desktop Wrapper / Build Tooling** | Tauri | **TBD** | Desktop application packaging and system integration (global shortcuts, tray)
**E2E-Testing** | Playwright | **TBD** | End-to-end integration testing for web and API flows
| **AI / ML** | PyTorch | **TBD** | Local AI/ML development and model training |
| **Speech-to-Text** | Local STT | Planned | Local speech recognition |
| **LLM Runtime** | Local LLM runtime | **TBD** | Local language-model inference |
| **Workflow Engine** | FlowKit | **TBD** | Workflow orchestration |
| **CI/CD** | GitHub Actions | Planned | Automated testing and CI |
| **Version Control** | Git / GitHub | Planned | Source control and collaboration |
| **Documentation / Diagrams** | Mermaid | Implemented | Diagram rendering in Markdown documentation |

---

## Backend

### Python

**Status:** Planned

Python is the primary backend language for ODEN. It will be used for application logic, data processing, AI/ML components, and supporting services.

**Target version:** Python 3.11+

### Ruff

**Status:** Implemented

Ruff is used for Python linting and code formatting. It provides static code analysis and enforces consistent formatting across the backend.

**Current version:** 0.17.4

### Pyright

**Status:** Implemented

Pyright is used for static type checking of ODEN's Python code. It identifies type inconsistencies and helps maintain reliable interfaces between backend components.

### FastAPI

**Status:** Planned

FastAPI will provide the HTTP API between the backend and frontend and expose backend functionality to other components where required.

### pytest

**Status:** Planned

pytest will be used for automated backend testing.

---

## Database

### SQLite

**Status:** Planned

SQLite is intended to provide a lightweight local database for ODEN.

The initial database solution should remain simple and local. A different database system may be considered later if project requirements justify it.

### SQLAlchemy

**Status:** TBD

SQLAlchemy may be used as the ORM and database abstraction layer.

The decision will depend on the complexity of ODEN's data model and whether an ORM provides sufficient benefit over direct SQLite access.

---

## Frontend

### React

**Status:** Planned

React will be used to build ODEN's graphical user interface.

### React Native (Expo)

**Status:** TBD

React Native (via Expo) is a candidate for building the mobile user interface. It will allow maximum code sharing (TypeScript types, business logic, API clients) between the web GUI and mobile clients.

### TypeScript

**Status:** Planned

TypeScript will be used as the primary frontend programming language to provide static typing and improve maintainability.

### ESLint

**Status:** Implemented

ESLint is used for static analysis and code quality checks in the TypeScript/React frontend.

**Current version:** 9.39.5

### Prettier

**Status:** Implemented

Prettier is used for automatic code formatting in the frontend. It provides consistent formatting across TypeScript, JavaScript, and related frontend files.

**Current version:** 3.9.10

### Jest

**Status:** Planned

Jest will be used for automated testing of the frontend, including unit tests and component-related tests where appropriate.

Jest will be configured to work with the TypeScript-based frontend.

### Vite

**Status:** TBD

Vite is a candidate for frontend development and build tooling.

### Tailwind CSS

**Status:** TBD

Tailwind CSS is a candidate for frontend styling.

---
## Desktop Wrapper

### Tauri

**Status:** TBD

Tauri is a candidate for packaging the React frontend into a lightweight native desktop application, enabling desktop features such as system tray integration and global keyboard shortcuts.

---

## AI & Audio Processing

### PyTorch

**Status:** TBD

PyTorch is a candidate for AI/ML development, particularly if ODEN includes locally trained or fine-tuned models.

### Local Speech-to-Text

**Status:** Planned

ODEN is intended to support local speech-to-text processing in order to reduce reliance on external cloud services.

The specific STT implementation is **TBD**.

### Local LLM Runtime

**Status:** TBD

ODEN may use a local LLM runtime for language-model inference.

Potential technologies include:

- Whisper
- llama.cpp
- Ollama
- Other suitable local runtimes

This is **TBD**.

The final implementation will depend on ODEN's performance, hardware, model, and integration requirements.

---

## Workflow Engine

### FlowKit

**Status:** TBD

FlowKit is being considered as the workflow engine for ODEN.

The decision will depend on whether FlowKit provides the required workflow orchestration, execution, and integration capabilities without introducing unnecessary complexity or coupling.

---
## Testing & Quality Assurance

### Playwright

**Status:** TBD

Playwright is a candidate for End-to-End (E2E) automated testing. It will be used to test complete user workflows (e.g., audio capture triggering backend processing and displaying transcripts in the GUI) across UIs.

---

## CI/CD

### GitHub Actions

**Status:** Planned

GitHub Actions will be used for automated development workflows, such as:

- Running automated tests
- Checking code quality
- Running static type checks
- Building project components
- Verifying pull requests
- Other CI tasks as the project evolves

---

### Mermaid

**Status:** Implemented

Mermaid is used to create diagrams within Markdown documentation, including architecture and workflow diagrams.

---

## Technology Selection Principles

Technology choices for ODEN should generally follow these principles:

1. **Local-first** - Prefer local processing where practical, particularly for AI and audio processing.
2. **Open-source friendly** - Prefer technologies with permissive licensing and no unnecessary vendor lock-in.
3. **Maintainability** - Prefer technologies that are well-supported and maintainable over the project's expected lifetime.
4. **Simplicity** - Avoid introducing infrastructure or dependencies that are not justified by project requirements.
5. **Testability** - Technologies should support reliable automated testing.
6. **Modularity** - Components should remain replaceable where practical.
7. **Resource efficiency** - Consider CPU, RAM, storage, and GPU requirements when selecting AI and audio technologies.

---

[← Back to README](../README.md)