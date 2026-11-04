# External services
[← Go back](constraints.md)

## Purpose

This document defines the architectural rules for using external services in ODEN. External services include cloud-based AI providers, remote APIs, cloud storage, hosted databases, authentication services, and other services that require communication with systems outside the user's local environment.

## Optional by default

External services shall be treated as optional dependencies. ODEN's core functionality shall not require:

* Cloud AI providers
* Cloud storage
* Remote databases
* Third-party authentication
* External APIs
* Continuous internet connectivity

An external service may be used to provide additional or enhanced functionality, but it shall not become a mandatory dependency of the local core without an explicit architectural decision.

## External AI services

Cloud-based AI services, including external STT, LLM, or other AI providers, may be supported as optional implementations. When an external AI service is used:

* The service shall be explicitly identified.
* The affected functionality shall be documented.
* Data sent to the service shall be documented.
* The local alternative or degraded behavior shall be documented where applicable.
* Provider-specific code should be isolated from the core architecture.

## Service isolation

External-service integrations should be isolated behind explicit interfaces (see: [Interfaces](../interfaces/interfaces.md)). The core system should depend on the these interface rather than directly on a specific external provider. This allows external providers to be:

* Replaced
* Disabled
* Added
* Updated
* Removed

without requiring fundamental changes to the local architecture.
 

## Failure handling

External services may become unavailable due to:

* Network failures
* Service outages
* Authentication failures
* API changes
* Rate limits
* Provider changes
* Provider termination

ODEN shall not treat such failures as failures of the local core unless the affected functionality is explicitly defined as optional and unavailable.

## External service documentation

Each external service integration should document:

* Service name
* Purpose
* Affected ODEN component
* Data transferred
* Required credentials
* Network requirements
* Local alternative or degraded behavior
* Whether the service is optional

**//TODO add link to dir** 

## Provider independence

ODEN should avoid unnecessary coupling to a single external provider. Provider-specific functionality should be contained within the relevant integration layer where practical. The architecture should allow an external provider to be replaced without redesigning unrelated parts of ODEN.

[← Go back](constraints.md)
