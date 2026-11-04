# ODEN Supported Environments

[← Back to README](../../README.md)

## 1. Purpose

Defines ODEN's supported platforms, runtime versions, and development environment. Requirements may evolve as the project develops.

## 2. Operating Systems

### Desktop

| Operating System | Status |
| :--- | :--- |
| Windows 11 (64-bit) | Supported |
| Windows 10 (64-bit) | Supported |
| Linux | Untested |
| macOS | Untested |


### Mobile

| Platform | Status |
| :--- | :--- |
| iOS | Planned |
| Android | TBD |

***( Mobile support requirements will be defined when the frontend approach is selected. )***

## 3. Runtime Versions

- **Python:** 3.11+ target. Higher versions must be compatible with project dependencies and verified through testing.
- **Node.js:** Version 24 LTS, **(TBD / provisionally)**, for frontend development tooling.

Exact development and testing versions should be recorded in project configuration.

## 4. Hardware Requirements

Minimum hardware requirements are TBD and will be established through performance testing of audio processing, STT, and local AI workloads. Optional hardware acceleration might be documented separately.

## 5. Development Environment

- Git for version control.
- Python with an isolated environment and dependency management.
- Node.js and npm for frontend development.

## 6. Compatibility and Maintenance

Supported environments must be verified through relevant functionality and testing. Untested platforms are not guaranteed to work.

Review this document when runtime support ends, dependencies change, new platforms are introduced, or testing identifies compatibility issues.

---

[← Back to README](../../README.md)