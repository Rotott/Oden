# Transcript interface
[← Go back](interfaces.md)

## Responsibility

The Transcript interface defines the common representation and operations for transcript data within ODEN. It provides a consistent boundary between speech recognition, transcript review, storage, search, and other consumers.

---

## Inputs

The Transcript interface may receive:

* Transcribed text
* Timing information
* Speaker information, when available
* Confidence information, when available
* User corrections
* Transcript metadata

---

## Outputs

The Transcript interface provides:

* Transcript content
* Transcript metadata
* Segment information
* Revision or correction information, where applicable

---

## Contract

An implementation of the Transcript Interface shall:

* Represent transcript content in a consistent form.
* Preserve relevant metadata.
* Support corrections without exposing internal storage details.
* Allow consumers to access transcript information without knowing how it is stored.
* Clearly distinguish unavailable information from empty or intentionally omitted information.

---

## Consumers

Primary consumers include:

* STT
* Review / Correction
* Workflow
* Storage
* Search / Retrieval

---

## Dependencies

* [Storage interface](storage.md)

---

## Implementation independence

Consumers must not depend directly on:

* Database schemas
* Serialization formats
* ORM models
* Internal transcript storage structures

The representation may evolve as long as the public contract remains compatible.

[← Go back](interfaces.md)
