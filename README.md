# Oden
## Local Personal Intelligence

Oden is a local-first personal AI system designed to capture, understand, remember, and act on spoken thoughts and ideas.

The project started as a personal Speech-to-Text (STT) tool for quickly recording thoughts and voice notes without having to stop and write. Over time, Oden is intended to evolve into a modular personal AI assistant with local speech, memory, workflows, and agent capabilities.

The primary goal is privacy, personalization, and continuous improvement without relying on paid cloud AI services or external APIs.

## Vision

Oden should become a personal voice journal and AI assistant that gets better through everyday use.

A typical interaction might be as simple as:

> "Jag behöver köpa mjölk och ägg."

or:

> "Jag fick en idé om hur FlowKit skulle kunna hantera context mellan noder."

Oden should be able to:

- Record voice locally
- Transcribe speech locally
- Store audio and transcripts
- Search and retrieve previous thoughts
- Correct transcription errors
- Learn from corrections
- Build a personal training dataset
- Improve its STT model over time
- Eventually understand intent and perform tasks
- Support multiple agents/personas such as Bettan and Kaj

## Core Principles

- **Local-first** — personal data remains strictly on the user's hardware under full user control
- **Privacy-focused** — no dependency on cloud AI services
- **Modular** — STT, TTS, LLM, memory, and other components should be replaceable
- **Personalized** — optimized for the user's voice, language, vocabulary, and usage patterns
- **Incremental** — start simple and evolve into a more capable system
- **Observable** — model versions, datasets, workflows, and experiments should be traceable
- **Open architecture** — the technical system should be useful independently of any specific AI model


## Getting Started
> **Note:** The setup instructions below are preliminary and subject to change.
```bash
### Clone the repository
git clone https://github.com/Rotott/oden.git

### Install dependencies (Example) TBD
pip install -r requirements.txt
npm install --prefix frontend

### Run backend
python -m backend.main
```



## Status

**Early development / experimental**

The architecture and individual components are expected to evolve significantly as the project develops. The current priority is building a solid foundation rather than prematurely optimizing for a fully autonomous AI assistant.


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
              Workflow Layer (FlowKit)
 ```






Oden is primarily developed in Python for its AI and audio ecosystem, while performance-critical components may use C++ or Rust when justified.

FlowKit is intended to provide deterministic workflow orchestration for suitable Oden pipelines.

## Initial Focus

The first version of Oden will focus on being a reliable personal voice journal:

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


The initial goal is not to build a general-purpose AI assistant or compete with models such as Whisper. Instead, the project focuses on building the infrastructure required to eventually create a highly personalized system.

## Personal Learning Loop

A central part of Oden is the feedback loop between usage and model improvement:

    Speak
      │
      ▼
     STT
      │
      ▼
 Transcription
      │
   Correction
      │
      ▼
Training Dataset
      │
      ▼
  Model Training
      │
      ▼
 New Model Version
      │
      └──────────────► STT



Corrections made during normal use can become high-quality training data for future model versions.

This allows Oden to gradually adapt to:

- Personal pronunciation
- Speech patterns
- Swedish language usage
- English technical terminology
- Programming terminology
- Personal vocabulary
- Common phrases and expressions

## Agents

Oden is designed to support multiple agents/personas using the same underlying system. For example:

- **Bettan**  
  A general-purpose personal assistant focused on everyday interaction, notes, reminders, and personal information.
- **Kaj**  
  A more technically oriented assistant, potentially optimized for programming, software development, and technical reasoning.
- **Albert**
  An analytical assistant focused on research, synthesis, and structured reasoning.

These are personas/agents rather than separate AI systems. Their voices, personalities, prompts, and available tools can be configured independently of Oden's core infrastructure.

## Technology

Current/expected technologies:



- **Backend:** Python 3.11+, FastAPI, pytest, SQLite / (SQLAlchemy)?, Jest
- **Frontend:** React, TypeScript, (Tailwind CSS)?, (Vite)?
- **AI & Audio Processing:** (PyTorch)?, (Local STT/LLM runtimes (e.g., Whisper, llama.cpp / Ollama))?
- **Workflow Engine:** (FlowKit)? --> tbd 
- **CI/CD:** GitHub Actions








The exact STT, TTS, and LLM models are intentionally kept replaceable.

## Project Structure

The project is expected to evolve toward a structure similar to:

oden/
├── backend/
│   ├── stt/
│   ├── tts/
│   ├── ai/
│   ├── memory/
│   ├── agents/
│   └── workflows/
│
├── frontend/
│
├── training/
│
├── tests/
│
├── docs/
│
├── examples/
│
└── scripts/


Personal recordings, databases, datasets, model checkpoints, and other private data are kept outside the public repository.

## Roadmap

### Phase 1 — Voice Journal
- Local audio recording
- VAD
- Local STT
- Transcript storage
- Manual correction
- Basic search

### Phase 2 — Personal Dataset
- Structured dataset generation
- Dataset validation
- Audio preprocessing
- Evaluation metrics
- Dataset versioning

### Phase 3 — Personal STT
- Fine-tuning an existing open model
- Personal vocabulary adaptation
- Model evaluation
- Model versioning

### Phase 4 — Memory
- Semantic search
- Personal knowledge retrieval
- Context management
- Long-term memory

### Phase 5 — Personal Assistant
- Local LLM integration
- Intent recognition
- Tool calling
- Tasks and reminders
- Natural language interaction

### Phase 6 — Agent System
- Multiple agents/personas
- Workflow orchestration
- Planning
- Tool execution
- Voice-based interaction

## Long Term

Investigate the feasibility of training a smaller STT model from scratch, specifically optimized for:

- A single speaker
- Swedish
- Technical vocabulary
- Personal speech patterns
- Low-latency local inference

## Privacy

Oden is designed around a local-first architecture.

The public repository contains source code, documentation, tests, and non-sensitive examples. Personal recordings, transcripts, datasets, databases, model checkpoints, and private configuration are not part of the public repository.

The long-term goal is for Oden to remain fully usable without requiring external AI APIs or paid cloud services.



## Documentation

More detailed documentation will be maintained separately:

- `docs/architecture.md` — System architecture
- `docs/requirements.md` — Requirements and functional goals
- `docs/ai.md` — AI and model strategy
- `docs/stt.md` — Speech-to-Text pipeline
- `docs/tts.md` — Text-to-Speech pipeline
- `docs/memory.md` — Memory and retrieval architecture
- `docs/agents.md` — Agent architecture
- `docs/training.md` — Dataset and training pipeline
- `docs/workflows.md` — Workflow orchestration
- `docs/privacy.md` — Privacy and data handling
- `docs/roadmap.md` — Development roadmap

## Philosophy

Oden should be a tool that listens, remembers, learns, and helps — while keeping the user's data on the user's machine.
