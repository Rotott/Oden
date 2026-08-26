# Oden requirements specification

## Requirement tag legend

Before reviewing the specifications, use this table to cross-reference the requirement identifiers:

| Tag Prefix | Category | Description |
| :--- | :--- | :--- |
| **REQ-AUDIO** | Functional | Audio capture, recording, processing, and storage. |
| **REQ-STT** | Functional | Speech-to-Text processing and transcription. |
| **REQ-TRANSCRIPT** | Functional | Transcript review, correction, metadata, and lifecycle management. |
| **REQ-DATA** | Functional | Dataset creation, storage, validation, and versioning. |
| **REQ-MEM** | Functional | Search, retrieval, semantic memory, and long-term context. |
| **REQ-AGENT** | Functional | Agent/persona configuration and execution. |
| **REQ-WORKFLOW** | Functional | Workflow orchestration and external lib integration (eg. FlowKit ). |
| **REQ-API** | Functional | Application and service API design. |
| **REQ-ERR** | Functional | Validation failures, exceptions, and error handling. |
| **REQ-PRIV** | Non-Functional | Local-first operation, privacy, and data ownership. |
| **REQ-PERF** | Non-Functional | Runtime performance and resource usage. |
| **REQ-ARCH** | Non-Functional | Modularity, separation of concerns, and architectural constraints. |
| **REQ-OBS** | Non-Functional | Observability, traceability, and version tracking. |
| **REQ-TEST** | Non-Functional | Automated testing and testability requirements. |

---

## Table of Contents

* [1. Functional requirements](#1-functional-requirements)
    * [1.1 Audio capture & storage](#11-audio-capture--storage)
    * [1.2 Speech-to-Text (STT)](#12-speech-to-text)
    * [1.3 Transcript management](#13-transcript-management)
    * [1.4 Dataset management](#14-dataset-management)
    * [1.5 Memory & retrieval](#15-memory--retrieval)
    * [1.6 Agents & personas](#16-agents--personas)
    * [1.7 Workflow orchestration](#17-workflow-orchestration)
    * [1.8 Public API](#18-public-api)
    * [1.9 Error handling & validation](#19-error-handling--validation)
* [2. Non-functional requirements](#2-non-functional-requirements)
    * [2.1 Privacy & local-first operation](#21-privacy--local-first-operation)
    * [2.2 Performance](#22-performance)
    * [2.3 Architecture & maintainability](#23-architecture--maintainability)
    * [2.4 Observability & reproducibility](#24-observability--reproducibility)
    * [2.5 Testability](#25-testability)
* [3. Future requirements](#3-future-requirements)

---

# 1. Functional requirements

## 1.1 Audio capture & storage

- [ ] **REQ-AUDIO-001:** Oden shall provide a mechanism for recording audio from a supported local input device.
- [ ] **REQ-AUDIO-002:** Oden shall store recorded audio locally without requiring a cloud storage service.
- [ ] **REQ-AUDIO-003:** Each recording shall be associated with a unique identifier.
- [ ] **REQ-AUDIO-004:** Each recording shall store sufficient metadata to identify when and how it was created.
- [ ] **REQ-AUDIO-005:** Oden shall support Voice Activity Detection (VAD) for identifying speech segments within recorded audio.
- [ ] **REQ-AUDIO-006:** The audio pipeline shall expose failures such as unavailable input devices or invalid audio data through structured error handling.
- [ ] **REQ-AUDIO-007:** Audio format and sampling configuration shall be explicitly defined by the recording pipeline.
- [ ] **REQ-AUDIO-008:** The system shall preserve the relationship between an audio recording and its resulting transcription.

## 1.2 Speech-to-Text (STT)

- [ ] **REQ-STT-001:** Oden shall provide a STT interface for converting locally recorded speech into text.
- [ ] **REQ-STT-002:** The STT pipeline shall support locally executed models.
- [ ] **REQ-STT-003:** The STT implementation shall be replaceable without requiring changes to unrelated application components.
- [ ] **REQ-STT-004:** Each generated transcription shall record the STT model or model version used to produce it.
- [ ] **REQ-STT-005:** The STT pipeline shall support a fixed selection of languages.
    - [ ] **REQ-STT-005.1:** The pipeline shall support Swedish speech. 
    - [ ] **REQ-STT-005.2:** The pipeline shall support English speech.
- [ ] **REQ-STT-006:**  The STT pipeline should support mixed Swedish/English technical terminology.
- [ ] **REQ-STT-007:** STT failures shall be reported without corrupting the original audio recording.
- [ ] **REQ-STT-008:** STT failures shall be reported without deleting the original audio recording.
- [ ] **REQ-STT-009:** The STT pipeline shall expose sufficient metadata to evaluate transcription performance.

## 1.3 Transcript management

- [ ] **REQ-TRANSCRIPT-001:** Oden shall persist generated transcripts locally.
- [ ] **REQ-TRANSCRIPT-002:** Each transcript shall be associated with its source audio recording.
- [ ] **REQ-TRANSCRIPT-003:** The user shall be able to manually correct a generated transcript.
- [ ] **REQ-TRANSCRIPT-004:** The system shall preserve the original generated transcription when a corrected transcription is created.
- [ ] **REQ-TRANSCRIPT-005:** The system shall record when a transcript was created.
    - [ ] **REQ-TRANSCRIPT-005.1:** The system shall recored when a transcript was modified. **(?)**
- [ ] **REQ-TRANSCRIPT-006:** Corrected transcripts shall be identifiable as user-corrected data.
- [ ] **REQ-TRANSCRIPT-007:** Transcript data shall be searchable using text-based queries.
- [ ] **REQ-TRANSCRIPT-008:** Retrieved transcripts shall provide access to associated metadata and, where available, the original audio.

## 1.4 Dataset management

- [ ] **REQ-DATA-001:** Oden shall be able to generate a structured training dataset from eligible audio recordings and their corresponding user-corrected transcripts.
- [ ] **REQ-DATA-002:** Dataset generation shall preserve the relationship between source audio and transcript.
- [ ] **REQ-DATA-003:** User-corrected transcripts shall be distinguishable from uncorrected machine-generated transcripts.
- [ ] **REQ-DATA-004:** Dataset generation shall allow unsuitable or incomplete samples to be excluded.
- [ ] **REQ-DATA-005:** Dataset versions shall have unique identifiers.
- [ ] **REQ-DATA-006:** Dataset metadata shall record the source and generation configuration where practical.
- [ ] **REQ-DATA-007:** Oden shall not require private training datasets to be stored in the public source repository.
- [ ] **REQ-DATA-008:** Dataset generation shall be reproducible from recorded source data and configuration where practical.

## 1.5 Memory & retrieval

- [ ] **REQ-MEM-001:** Oden shall provide a persistent storage mechanism for previously recorded thoughts and associated metadata.
- [ ] **REQ-MEM-002:** The system shall support retrieval of previously stored transcripts using text-based search.
- [ ] **REQ-MEM-003:** Retrieved memories shall retain references to their original source data.
- [ ] **REQ-MEM-004:** The memory subsystem shall be replaceable without requiring changes to the audio or STT subsystems.
- [ ] **REQ-MEM-005:** The architecture shall allow future semantic/vector-based retrieval.
- [ ] **REQ-MEM-006:** The architecture shall allow future long-term memory and contextual retrieval mechanisms.

## 1.6 Agents & personas

- [ ] **REQ-AGENT-001:** Oden shall provide an abstraction for configurable AI agents/personas.
- [ ] **REQ-AGENT-002:** Agents shall be configurable independently of the core Oden infrastructure.
- [ ] **REQ-AGENT-003:** An agent shall be able to define its own personality, system instructions, and available capabilities.
    - [ ] **REQ-AGENT-003:** **//TODO TBD define exact def of this, eg. name+voice+x...**
- [ ] **REQ-AGENT-004:** Agents shall be able to access approved tools through controlled interfaces.
- [ ] **REQ-AGENT-005:** Multiple agents shall be able to use the same underlying memory and infrastructure where permitted.
- [ ] **REQ-AGENT-006:** Agent configuration shall not require duplicating the underlying AI models or system components.
- [ ] **REQ-AGENT-007:** Agent execution shall be isolated from unrelated application components.

## 1.7 Workflow orchestration

- [ ] **REQ-WORKFLOW-001:** Oden shall support deterministic workflow execution for suitable system operations.
- [ ] **REQ-WORKFLOW-002:** Workflow execution shall be compatible with FlowKit where FlowKit is selected as the workflow orchestration layer. **(? TBD ?)**
- [ ] **REQ-WORKFLOW-003:** Oden workflows shall be able to compose independent system capabilities such as audio processing, STT, storage, memory, and tool execution.
- [ ] **REQ-WORKFLOW-004:** Workflow failures shall expose sufficient information to identify the failed operation.
    - [ ] **REQ-WORKFLOW-004.1:** **//TODO TBD define exact meaning of sufficient info**
- [ ] **REQ-WORKFLOW-005:** Workflow orchestration shall remain separate from the implementation details of individual Oden components.

## 1.8 Public API

- [ ] **REQ-API-001:** Oden shall expose programmatic interfaces for core application capabilities.
- [ ] **REQ-API-002:** Core interfaces shall avoid exposing internal storage or implementation details unnecessarily.
- [ ] **REQ-API-003:** Components such as STT, TTS, memory, agents, and workflows shall communicate through defined interfaces.
- [ ] **REQ-API-004:** API contracts shall remain stable where practical as internal implementations evolve.
- [ ] **REQ-API-005:** The API shall support programmatic access to recordings, transcripts, and relevant metadata.
- [ ] **REQ-API-006:** The API shall provide structured responses for successful and failed operations.

## 1.9 Error handling & validation

- [ ] **REQ-ERR-001:** Oden shall provide structured error handling for failures occurring within core subsystems.
    - [ ] **REQ-ERR-001.1:** **//TODO TBD define exacly what the core is
- [ ] **REQ-ERR-002:** Failures in one processing stage shall not silently corrupt source data.
- [ ] **REQ-ERR-003:** STT failures shall preserve the original audio recording.
- [ ] **REQ-ERR-004:** Storage failures shall be reported to the caller.
- [ ] **REQ-ERR-005:** Invalid input data shall be rejected with an identifiable error.
- [ ] **REQ-ERR-006:** External or optional integrations shall not prevent the core local system from starting unless explicitly required by the current workflow.

---

# 2. Non-functional requirements

## 2.1 Privacy & local-first operation

-  **REQ-PRIV-001:** Core Oden functionality shall operate without requiring a cloud AI provider.
-  **REQ-PRIV-002:** Personal recordings shall remain under the user's control.
-  **REQ-PRIV-003:** Personal transcripts shall remain under the user's control.
-  **REQ-PRIV-004:** Personal datasets shall remain under the user's control.
-  **REQ-PRIV-005:** Private recordings, transcripts, databases, datasets, model checkpoints, and private configuration shall not be required to reside in the public source repository.
-  **REQ-PRIV-006:** Oden shall clearly distinguish between public project resources and private user data.
-  **REQ-PRIV-007:** Optional external services shall be explicitly identifiable and shall not be treated as implicit dependencies of the local-first architecture.

## 2.2 Performance

-  **REQ-PERF-001:** The architecture shall support low-latency local audio capture.
-  **REQ-PERF-002:** The audio recording pipeline shall not introduce unnecessary blocking operations during capture.
-  **REQ-PERF-003:** STT inference performance shall be measurable using defined evaluation procedures.
-  **REQ-PERF-004:** Memory and storage operations shall avoid loading the complete personal dataset into memory unnecessarily.
-  **REQ-PERF-005:** Performance-critical components may use alternative languages such as C++ or Rust where justified by measurable requirements.
-  **REQ-PERF-006:** Performance optimizations shall not compromise data integrity or system observability without explicit justification.

## 2.3 Architecture & maintainability

-  **REQ-ARCH-001:** The system shall separate audio capture, STT, transcript management, storage, memory, agents, and workflow orchestration into distinct components with clearly defined responsibilities.
-  **REQ-ARCH-002:** AI model implementations shall be replaceable without requiring major changes to unrelated application components.
-  **REQ-ARCH-003:** The architecture shall avoid coupling application logic directly to a specific STT, TTS, or LLM implementation where practical.
-  **REQ-ARCH-004:** Private user data shall be separated from source-code concerns.
-  **REQ-ARCH-005:** Components shall expose explicit interfaces for dependencies where practical.
-  **REQ-ARCH-006:** The system shall support incremental replacement or extension of individual components.
-  **REQ-ARCH-007:** Workflow orchestration shall remain conceptually separate from the implementation of individual tasks or AI models.

## 2.4 Observability & reproducibility

-  **REQ-OBS-001:** Oden shall track the STT model or model version used for generated transcripts.
-  **REQ-OBS-002:** Dataset versions shall be identifiable and traceable to their source data.
-  **REQ-OBS-003:** Model-training experiments shall record relevant configuration and version information where practical.
-  **REQ-OBS-004:** Significant processing operations should expose timestamps and relevant execution metadata.
- **REQ-OBS-005:** The system shall provide sufficient information to determine which model produced a stored transcription.
-  **REQ-OBS-006:** Changes to important model, dataset, and processing configurations should be traceable.

## 2.5 Testability

-  **REQ-TEST-001:** The architecture shall accommodate automated unit testing of core components.
-  **REQ-TEST-002:** Audio processing components shall be testable independently of the user interface.
-  **REQ-TEST-003:** STT integrations shall be testable using deterministic or controlled test inputs where practical.
-  **REQ-TEST-004:** Transcript correction and storage behavior shall be covered by automated tests.
-  **REQ-TEST-005:** Workflow execution and failure behavior shall be covered by automated tests.
-  **REQ-TEST-006:** Core API contracts shall be covered by automated tests.
-  **REQ-TEST-007:** Integration tests shall verify important interactions between major subsystems.

---

# 3. Future requirements

The following requirements describe capabilities that are part of the long-term direction of Oden but are intentionally not part of the initial implementation scope.

## 3.1 Personal STT model

- [ ] **REQ-STT-100:** Oden should support fine-tuning an existing open STT model using user-generated training data.
- [ ] **REQ-STT-101:** The system should support evaluation of personalized STT models against a defined validation dataset.
- [ ] **REQ-STT-102:** Oden should support comparing personalized STT models against baseline models.
- [ ] **REQ-STT-103:** The system should support versioning and rollback of personalized STT models.

## 3.2 Semantic memory

- [ ] **REQ-MEM-100:** Oden should support semantic retrieval of previously stored information.
- [ ] **REQ-MEM-101:** Oden should support persistent long-term contextual memory.
- [ ] **REQ-MEM-102:** Memory retrieval should be able to provide relevant context to an AI agent.

## 3.3 Personal assistant

- [ ] **REQ-AGENT-100:** Oden should support local LLM inference.
- [ ] **REQ-AGENT-101:** Oden should support natural-language intent recognition.
- [ ] **REQ-AGENT-102:** Oden should support tool invocation based on recognized intent.
- [ ] **REQ-AGENT-103:** Oden should support tasks and reminders.
- [ ] **REQ-AGENT-104:** Oden should support voice-based conversational interaction.

## 3.4 Advanced agent system

- [ ] **REQ-AGENT-200:** Oden should support multiple independently configurable agents/personas.
- [ ] **REQ-AGENT-201:** Agents should be able to use different prompts, models, voices, tools, and memory configurations.
- [ ] **REQ-AGENT-202:** Oden should support controlled agent-to-agent interaction where justified.
- [ ] **REQ-AGENT-203:** Agent actions should be observable and traceable.

## 3.5 Experimental STT research

- [ ] **REQ-STT-200:** Oden should provide infrastructure for evaluating the feasibility of training a smaller STT model from scratch.
- [ ] **REQ-STT-201:** Such a model should be evaluated for single-speaker Swedish speech.
- [ ] **REQ-STT-202:** Evaluation should include technical vocabulary and personal speech patterns.
- [ ] **REQ-STT-203:** The feasibility of low-latency local inference should be measured before committing to a custom model architecture.

---

[← Back to README](../README.md)