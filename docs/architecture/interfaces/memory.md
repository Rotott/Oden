# Memory interface
[← Go back](interfaces.md)

## Responsibility

The Memory interface defines how ODEN components provide, retrieve, and update information intended to persist as contextual memory.

The interface establishes the boundary between memory consumers and the internal mechanisms used to store, organize, retrieve, or rank memories.

---

## Inputs

The Memory interface may receive:

* Information to store as memory
* Context for retrieval
* Retrieval criteria
* Requests to update or remove memory

---

## Outputs

The Memory interface provides:

* Relevant memory entries
* Associated metadata
* Retrieval status
* Errors, where applicable

---

## Contract

An implementation of the Memory Interface shall:

* Allow authorized components to store and retrieve memory.
* Provide memory without exposing internal storage or retrieval mechanisms.
* Accept contextual information when required to determine relevant memories.
* Provide predictable behavior when no relevant memory is available.
* Report failures through the defined error mechanism.

The exact memory model, retrieval strategy, ranking mechanism, and storage representation are implementation details.

---

## Consumers

Primary consumers include:

* Workflow
* Agent runtime

Additional consumers may be introduced as the memory architecture develops.

---

## Dependencies

* [Storage Interface](storage.md)

---

## Implementation independence

Consumers must not depend directly on:

* A specific memory algorithm
* A specific vector database
* Embedding models
* Retrieval or ranking algorithms
* Internal memory representations

The memory implementation may evolve substantially as long as the public contract remains compatible.

[← Go back](interfaces.md)
