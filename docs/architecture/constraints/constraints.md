# Architecture constraints
[← Back to  ODEN Architecture](../architecture.md)

## Purpose

This document defines the architectural constraints that guide the design and implementation of ODEN.

The constraints exist to preserve ODEN's core philosophies regarding, e.g., local-first architecture, protecting personal data, and preventing unnecessary dependencies on external services or infrastructure.


These constraints apply across ODEN's components and should be considered when introducing new features, services, or dependencies.

## Constraint categories

| Constraint            | Purpose                                                             | Documentation                                     |
| --------------------- | ------------------------------------------------------------------- | ------------------------------------------------- |
| Local-First           | Defines requirements for offline operation and local processing     | [Local-First](local-first.md)                     |
| Data Storage          | Defines requirements for storing and handling personal data         | [Data Storage](data-storage.md)                   |
| External Services     | Defines requirements for optional external and cloud services       | [External Services](external-services.md)         |
| Repository Boundaries | Defines what data and assets may be stored in the public repository | [Repository Boundaries](repository-boundaries.md) |


## General Principles

* Core functionality shall not require cloud services.
* Core functionality shall not require cloud storage.
* Personal data shall remain under local control by default.
* External services shall be explicitly optional.
* External-service failures shall not prevent core local functionality from operating.
* Credentials, personal data, and other sensitive information shall not be committed to the public repository.
* Architectural decisions that introduce external dependencies shall explicitly document those dependencies and their purpose.

These constraints apply unless a future architectural decision explicitly changes them.


[← Back to  ODEN Architecture](../architecture.md)
