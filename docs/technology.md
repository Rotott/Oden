# ODEN Technology

[← Back to README](../README.md)

This document describes the technologies used or planned for ODEN, along with their current status and intended purpose.

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
| **Testing** | pytest | Planned | Backend testing |
| **Database** | SQLite | Planned | Local application data storage |
| ***ORM*** | SQLAlchemy | **TBD** | Database abstraction and data access |
| **Frontend** | React | Planned | User interface |
| **Frontend Language** | TypeScript | Planned | Type-safe frontend development |
| **Frontend Testing** | Jest | Planned | Automated frontend/unit testing |
| ***Build Tooling*** | Vite | **TBD** | Frontend development and build tooling |
| ***Styling*** | Tailwind CSS | **TBD** | Frontend styling |
| ***AI / ML*** | PyTorch | **TBD** | Local AI/ML development and model training |
| **Speech-to-Text** | Local STT | Planned | Local speech recognition |
| ***LLM Runtime*** | Local LLM runtime | **TBD** | Local language-model inference |
| ***Workflow Engine*** | FlowKit | **TBD** | Workflow orchestration |
| **CI/CD** | GitHub Actions | Planned | Automated testing and CI |
| **Version Control** | Git / GitHub | Planned | Source control and collaboration |
| **Documentation / Diagrams** | Mermaid | Planned | Diagram rendering in Markdown documentation |

---

## Backend

### Python

**Status:** Planned

Python is the primary backend language for ODEN. It will be used for application logic, data processing, AI/ML components, and supporting services.

**Target version:** Python 3.11+

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

### TypeScript

**Status:** Planned

TypeScript will be used as the primary frontend programming language to provide static typing and improve maintainability.

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

## CI/CD

### GitHub Actions

**Status:** Planned

GitHub Actions will be used for automated development workflows, such as:

- Running automated tests
- Checking code quality
- Building project components
- Verifying pull requests
- Other CI tasks as the project evolves

---
### Mermaid

**Status:** Planned

Mermaid is used to create diagrams within Markdown documentation, including architecture and workflow diagrams.

---

## Technology Selection Principles

Technology choices for ODEN should generally follow these principles:

1. **Local-first** — Prefer local processing where practical, particularly for AI and audio processing.
2. **Open-source friendly** — Prefer technologies with permissive licensing and no unnecessary vendor lock-in.
3. **Maintainability** — Prefer technologies that are well-supported and maintainable over the project's expected lifetime.
4. **Simplicity** — Avoid introducing infrastructure or dependencies that are not justified by project requirements.
5. **Testability** — Technologies should support reliable automated testing.
6. **Modularity** — Components should remain replaceable where practical.
7. **Resource efficiency** — Consider CPU, RAM, storage, and GPU requirements when selecting AI and audio technologies.

---


[← Back to README](../README.md)