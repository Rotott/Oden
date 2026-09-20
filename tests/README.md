# Tests
This directory contains tests that verify ODEN as a complete system or verify interactions between multiple components.

## Purpose

Tests in this directory are intended for behavior that cannot be adequately tested within a single component.

Examples include:

* Frontend-to-backend interactions
* End-to-end user workflows
* Cross-component data flows
* Integration of multiple ODEN subsystems
* System-level behavior and requirements




Component-specific tests should remain within their respective directories:

* `backend/tests/` — Backend tests
* `frontend/tests/` — Frontend tests

## System

Tests involving multiple ODEN components or cross-component behavior.

## E2E

End-to-end tests covering complete user workflows through ODEN's external interfaces.


