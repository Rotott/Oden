
# Oden
## Local Personal Intelligence

Oden is a local-first personal AI system designed to capture, understand, remember, and eventually act on spoken thoughts and ideas.

The project started as a personal Speech-to-Text (STT) tool for quickly recording thoughts and voice notes without interrupting the user's workflow. It is intended to evolve into a modular personal AI system with local speech processing, memory, workflows, and agent capabilities.

The primary goals are **privacy, personalization, modularity, and continuous improvement** without depending on paid cloud AI services.

## Vision

Oden should become a personal voice journal and AI assistant that gets better through everyday use.

A typical interaction might be:

> "I need to buy milk and eggs."

or:

> "I had an idea for how a bug could be fixed to handle context between the nodes in the graph."

Over time, Oden should be able to:

- Record voice locally
- Transcribe speech locally
- Store audio and transcripts
- Search and retrieve previous thoughts
- Correct transcription errors
- Learn from corrections
- Build a personal training dataset
- Improve its STT model over time
- Understand intent
- Perform tasks through tools and workflows
- Support multiple agents/personas such as Bettan, Kaj, and Albert

## Core Principles

- **Local-first** — personal data remains under the user's control
- **Privacy-focused** — no required dependency on cloud AI services
- **Modular** — STT, TTS, LLM, memory, and other components should be replaceable
- **Personalized** — the system should adapt to the user's voice, language, vocabulary, and usage patterns
- **Incremental** — Oden should evolve from a simple, reliable foundation
- **Observable** — models, datasets, experiments, and workflows should be traceable
- **Open architecture** — the system should not depend on a specific AI model or vendor




## Current (intitial) Focus

Oden is currently focused on becoming a reliable personal voice journal:

```text
Record
  ↓
Voice Activity Detection
  ↓
Speech-to-Text
  ↓
Review / Correction
  ↓
Store Audio + Transcript
  ↓
Search / Retrieve
```

The initial goal is **not** to build a general-purpose autonomous AI assistant or compete with models such as Whisper. The initial goal is to build the infrastructure required for a highly personalized local system.


## High-Level Architecture
 ```text
                  ODEN
        Local Personal Intelligence
                    │
        ┌───────────┴───────────┐
        │                       │
   Voice Interface         Agent Runtime
        │                       │
   ┌────┴────┐             ┌────┴────┐
   │         │             │         │
  STT       TTS          Memory    Tools
   │         │             │         │
   └─────────┴──────┬──────┴─────────┘
                    │
              Workflow Layer
 ```


Oden is primarily developed in Python. Performance-critical components may use C++ or Rust where justified.





## Status

**Early development / experimental**

The architecture and individual components are expected to evolve significantly. The current priority is building a solid and observable foundation rather than prematurely optimizing for a fully autonomous assistant.



## Documentation
- [Architecture](docs/architecture.md) — system architecture and component relationships
- [Project summary](docs/Project%20Summary.md) — overall project definition, vision, scope, and long-term direction
- [Requirements](docs/Requirements.md) — functional and non-functional requirements
- [Technology](docs/technology.md) - selected, planned, and TBD technologies, including their purpose, status, and selection rationale



## Development Roadmap

ODEN is developed incrementally through GitHub milestones. Each milestone defines a specific development stage and is broken down into issues linked to the project's requirements.

The current and planned milestones are:

| Milestone | Focus |
| :--- | :--- |
| **M01** | Voice Journal |
| **M02** | Personal Dataset |
| **M03** | Personal STT |
| **M04** | Memory **(TBD)**|
| **M05** | Personal Assistant **(TBD)** |
| **M06** | Agent System **(TBD)**|

For the current implementation status, planned work, individual issues, and milestone progress, see the project's **GitHub Milestones and Issues**.


## Getting Started

> **Note:** Setup instructions are preliminary and subject to change.

```bash
# Clone the repository
git clone https://github.com/Rotott/oden.git

# Install dependencies
pip install -r requirements.txt

# Install frontend dependencies
npm install --prefix frontend

# Run backend
python -m backend.main
```



## Privacy

Oden is designed around a local-first architecture.

The public repository contains source code, documentation, tests, and non-sensitive examples. Personal recordings, transcripts, datasets, databases, model checkpoints, and private configuration are not part of the public repository.

The long-term goal is for Oden to remain fully usable without requiring external AI APIs or paid cloud services.

