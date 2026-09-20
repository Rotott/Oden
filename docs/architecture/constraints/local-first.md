# Local-First architecture
[← Go back](constraints.md)

## Purpose

ODEN is designed as a local-first system. Its core functionality shall operate on the user's local system without requiring cloud services, cloud storage, or continuous network connectivity. Network connectivity may be used by optional functionality, but it shall not be a requirement for core operation.

## Core principle

> ODEN's core functionality shall remain usable without network connectivity.

Local processing and local storage are therefore the default architectural choices.

External services may extend ODEN's capabilities, but they shall not replace functionality that is required for the core local workflow unless explicitly defined by a future architectural decision.

## Core offline functionality

The following functionality is intended to operate without network connectivity:

* Local audio recording
* Local audio processing
* Local speech-to-text processing
* Transcript storage
* Transcript correction
* Local search
* Local memory functionality
* Local dataset generation where applicable
* Access to locally stored user data

The exact seelction and/or implementation of these capabilities may evolve, but their core operation shall not depend on a cloud service.

## Network access

Core functionality shall not require:

* An active internet connection
* A cloud account
* A cloud API key
* A remote database
* Cloud storage
* A third-party authentication service

Network access may be used by explicitly optional or enhancing functionality. Any network-dependent functionality shall be documented and isolated from the core functionality so that the core system remains usable without network access.


## Degraded operation

Optional external services may become unavailable due to:

* Lack of network connectivity
* Service outages
* Authentication failures
* API changes
* Rate limits
* Provider removal

Such failures shall not prevent the remaining local core functionality from operating.

Where an optional service provides functionality that cannot be reproduced locally, ODEN should provide an appropriate degraded state rather than treating the service as a mandatory system dependency.

## Architectural implications

Components that may use external services should be separated from the local core through explicit interfaces or adapters. This allows an external implementation to be replaced, disabled, or removed without requiring fundamental changes to the local architecture.


[← Go back](constraints.md)
