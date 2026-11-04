# Storage interface
[← Go back](interfaces.md)

## Responsibility

The Storage interface defines how ODEN components persist and retrieve data without depending on a specific storage technology.

---

## Inputs

The Storage interface may receive:

* Data to persist
* Identifiers
* Queries or retrieval criteria
* Update or deletion requests

---

## Outputs

The Storage Interface provides:

* Stored data
* Identifiers
* Query results
* Operation status
* Errors, where applicable

---

## Contract

An implementation of the Storage interface shall:

* Persist data according to the requirements of the calling component.
* Retrieve data through defined queries or identifiers.
* Provide predictable behavior for missing data.
* Report storage failures through the defined error mechanism.
* Avoid exposing implementation-specific storage details.

---

## Consumers

Primary consumers include:

* Workflow
* Transcript management
* Memory
* Search / Retrieval
* Dataset system

---

## Implementation independence

Consumers must not depend directly on:

* A specific database
* A specific filesystem layout
* A specific ORM
* SQL queries or other implementation-specific query mechanisms
* Internal storage schemas

The underlying storage implementation may be replaced without requiring changes to consumers that use only this interface.

[← Go back](interfaces.md)
