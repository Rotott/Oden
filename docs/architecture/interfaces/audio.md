# Audio interface
[← Go back](interfaces.md)

## Responsibility

The Audio interface defines how audio data is provided to and consumed by ODEN components. It separates audio consumers from the specific mechanism used to capture, process, or represent audio.

---

## Inputs

The Audio interface may receive:

* Raw or captured audio
* Audio metadata
* Processing configuration, where applicable

---

## Outputs

The Audio interface provides:

* Audio data in a defined representation
* Relevant audio metadata
* Processing status or errors, where applicable

---

## Contract

An implementation of the Audio interface shall:

* Provide audio data through the defined interface.
* Use a representation that consumers can process without knowing the implementation details.
* Preserve required audio properties such as timing and sample information.
* Report failures through the defined error mechanism.
* Avoid exposing internal capture or processing mechanisms.

---

## Consumers

Primary consumers include:

* STT
* Workflow

---

## Implementation independence

Consumers must not depend directly on:

* A specific audio capture library
* A specific audio device
* A specific audio processing library
* Internal audio-processing steps

The implementation may be replaced without requiring changes to consumers that use only this interface.



#### Note
//**TBD**: Consider splitting Audio into Audio Capture and Audio Processing, since capture is device/client-specific while processing such as VAD may run elsewhere. This would allow future clients (e.g. mobile) to capture audio locally while keeping the rest of the pipeline location-independent.

[← Go back](interfaces.md)
