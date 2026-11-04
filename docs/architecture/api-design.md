# API Design

[← Back to ODEN Architecture](architecture.md)

## 1. Purpose

This document defines the design principles for ODEN's programmatic APIs, including public interface boundaries, response conventions, and API stability.

## 2. Design principles

### REST by default

HTTP-based programmatic APIs should use REST over HTTP with JSON. Internal component communication does not need to use HTTP.

### Explicit contracts

Public APIs must define supported operations, inputs, outputs, and errors without exposing internal implementation details, storage structures, or database schemas.

### Consistent responses

Successful responses and errors must follow documented conventions and HTTP APIs must use appropriate status codes with appropiate error information.

### API specifications

Concrete HTTP endpoints, request and response schemas, and status codes should be documented alongside implementation.

## 3. Relationship to other documentation

- **[Architecture](architecture.md):** Defines overall architectural principles and component boundaries.
- **[Interface documentation](interfaces/interfaces.md):** Defines internal component contracts and dependencies.
- **API specification:** Defines concrete HTTP endpoints and their contracts. **(TBD/NYI)**
- **[Data and storage](../data/data-and-storage.md):** Defines storage organization and constraints.

These documents complement one another and should avoid duplicating detailed specifications.

## 4. Scope

This document defines intended API conventions, not individual endpoints. Authentication, authorization, pagination, versioning details, and other endpoint-specific decisions should be defined when concrete requirements justify them.

[← Back to ODEN Architecture](architecture.md)
