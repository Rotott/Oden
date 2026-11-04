# STT interface
[← Go back](interfaces.md)


## Responsibility

The STT interface defines how ODEN converts audio into textual transcription. It separates consumers of speech recognition from the specific speech-to-text implementation.

---

## Inputs

The STT interface accepts:

* Audio data
* Optional recognition configuration
* Optional language information

---

## Outputs

The STT interface provides:

* Transcribed text
* Transcript metadata
* Timing information, when available
* Confidence information, when available

---

## Contract

An implementation of the STT interface shall:

* Accept audio through the defined audio representation.
* Return transcription data through the defined transcript representation.
* Preserve relevant timing and metadata where supported.
* Report recognition failures through the defined error mechanism.
* Avoid exposing model-specific implementation details.

---

## Consumers

Primary consumers include:

* Workflow
* Transcript management

---

## Dependencies

* [Audio interface](audio.md)
* [Transcript interface](transcript.md)

---

## Implementation independence

Consumers must not depend directly on:

* A specific STT model
* A specific ML framework
* A specific inference engine
* Model-specific internal data structures

The STT implementation may be replaced without requiring changes to consumers that depend only on this interface.


[← Go back](interfaces.md)
