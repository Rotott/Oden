# Naming and coding conventions for ODEN

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. General Principles](#2-general-principles)
- [3. Formatting](#3-formatting)
- [4. Python](#4-python)
- [5. TypeScript / React](#5-typescript--react)
- [6. Type Hinting and Typing](#6-type-hinting-and-typing)
- [7. Database and Data](#7-database-and-data)
- [8. API](#8-api)
- [9. Tests](#9-tests)
- [10. Files and Directories](#10-files-and-directories)
- [11. Documentation](#11-documentation)
- [12. Abbreviations](#12-abbreviations)
- [13. Naming Priority](#13-naming-priority)

---

## 1. Purpose

This document defines the naming and coding conventions intended to be followed throughout ODEN's source code, configuration, data, tests, and documentation.

**Language-specific conventions should follow the relevant ecosystem's standards unless an ODEN convention explicitly overrides them.**

---

## 2. General Principles

- Prefer clear, descriptive names over short names.
- Use consistent domain terminology across components.
- Avoid unnecessary abbreviations.
- Use names that describe **what something represents or does**, rather than its implementation.
- Use nouns for data and concepts, and verbs for actions.
- Avoid reusing the same term for different concepts.
- Prefer explicit and predictable code over unnecessarily compact implementations.

ODEN-specific terminology should be defined consistently with the [architecture documentation](../architecture/architecture.md).

---

## 3. Formatting

Code formatting should be consistent and preferably enforced through automated formatting tools rather than individual preferences.

### General conventions

- Use consistent indentation within each language.
- Avoid unnecessarily long lines.
- Use whitespace to improve readability.
- Keep related functionality logically grouped.
- Avoid unnecessary formatting differences between files.

### Python //TODO move this down to ##4?

Python code should follow PEP 8, with the following project preferences:

| Element | Convention |
|---|---|
| Indentation | 4 spaces |
| Line length | 100 characters |
| Quotes | Double quotes |
| Imports | Grouped and consistently ordered |
| Formatting | Ruff Formatter |
| Linting | Ruff |

Formatting should preferably be automated and consistent across the project.

### TypeScript / React //TODO move this down to ##4?


Use the formatting conventions established by the frontend tooling.

Prettier is the preferred formatter, with consistent configuration across the frontend codebase.

---

## 4. Python

Python code should generally follow **PEP 8**.

| Element | Convention | Example |
|---|---|---|
| Variables | `snake_case` | `audio_path` |
| Functions | `snake_case` | `process_audio()` |
| Classes | `PascalCase` | `AudioProcessor` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_AUDIO_LENGTH` |
| Modules/files | `snake_case` | `audio_processor.py` |
| Private members | `_leading_underscore` | `_load_audio()` |

Boolean names should normally use a descriptive prefix such as `is_`, `has_`, `can_`, or `should_`.

```python
is_recording
has_transcript
can_process
```

---

## 5. TypeScript / React

TypeScript and React code should follow the established conventions of the ecosystem and project tooling.

| Element | Convention | Example |
|---|---|---|
| Variables | `camelCase` | `audioPath` |
| Functions | `camelCase` | `processAudio()` |
| Classes / types | `PascalCase` | `AudioProcessor` |
| React components | `PascalCase` | `AudioPlayer` |
| Constants | `UPPER_SNAKE_CASE` when appropriate | `MAX_AUDIO_LENGTH` |
| Files | Follow exported symbol | `AudioPlayer.tsx` |

Boolean names should use descriptive prefixes such as `is`, `has`, `can`, or `should`.

```ts
isRecording
hasTranscript
canProcess
```

Prefer explicit types for public interfaces and reusable components.

---

## 6. Type Hinting and Typing

ODEN should favour strong, explicit typing to improve readability, maintainability, and early error detection.

### Python

Python type hints should be used consistently.

- Public functions and methods must strive towards declared parameters and return types.
- Internal functions should also use type hints where they improve clarity.
- Use explicit types for class attributes and important data structures.
- Prefer specific types over `Any` whenever possible.
- Use type aliases or dedicated classes when complex types become difficult to understand.
- Use `None` explicitly when a value is optional.

Example:

```python
def process_audio_example(
    audio_path: Path,
    sample_rate: int,
) -> Transcript:
    ...
```

Static type checking should be used to detect type inconsistencies before runtime. Pyright or mypy may be used for this purpose **(TBD)**. The project should use a consistent type-checking configuration.

### TypeScript

Use TypeScript's type system rather than relying on untyped JavaScript patterns.

- Prefer explicit types for public interfaces and function boundaries.
- Avoid `any` unless there is a documented reason.
- Use interfaces or type aliases to define reusable data structures.
- Prefer explicit handling of nullable and optional values.
- Use strict TypeScript compiler settings where practical.

Example:

```ts
interface RecordingExample {
    id: string;
    audioPath: string;
    createdAt: Date;
}

function processAudioExample(recording: Recording): Promise<Transcript> {
    ...
}
```

**The goal is to make data structures and function contracts explicit, while avoiding unnecessary type complexity.**

---

## 7. Database and Data

Database tables, columns, constraints, and persistent data identifiers should use `snake_case`.

```text
# Tables (plural, snake_case)
recordings
transcripts
audio_datasets

# Columns (snake_case)
audio_path
created_at
transcript_id
is_active
```

- **Foreign Keys:** Name foreign keys explicitly as `<singular_target_table>_id` (e.g., `recording_id`).
- **Indexes:** Prefix indexes with `idx_` followed by the table and column names (e.g., `idx_recordings_created_at`).
- **Database File:** A local database file should have a clean and environment-agnostic name, such as `oden.db` or `oden.sqlite3`.

Database names should describe the **domain concept**, not the implementation that currently stores it.

---

## 8. API

API routes should use lowercase, plural resource names where appropriate.

```text
/api/recordings
/api/transcripts
/api/datasets
```

JSON fields should use `snake_case` unless a documented API convention requires otherwise.

---

## 9. Tests

Test files must mirror the structure of the source code or sit right alongside the implementation. Test names must clearly describe the behavior being verified rather than just the function name.



### Python

Python tests should follow pytest conventions.

Test files should use the `test_*.py` naming pattern.

Test functions should follow a predictable behavioural pattern:

`test_<unit>_<scenario>_<expected_result>()`

Examples:

```python
def test_audio_processor_with_invalid_file_raises_value_error():
    ...

def test_transcriber_returns_valid_transcript_on_success():
    ...
```

### TypeScript

TypeScript test files must mirror their corresponding source file name, appending `.test.ts` or `.test.tsx`.

```text
processAudio.test.ts
AudioPlayer.test.tsx
```

Examples:

```ts
it("should render the audio controls when a recording is loaded", () => {...});

it("should reject invalid audio formats", () => {...});
```

**Tests should use the same terminology as the functionality they validate.** Avoid lazy or generic names such as `test_data()` or `test_works()`.

---

## 10. Files and Directories

Use lowercase `kebab-case` for documentation files and directories unless a technology or framework convention requires another form.

Examples:

```text
docs/
docs/development/
docs/naming-conventions.md
docs/data/data-and-storage.md
```

Source-code filenames should follow the conventions of their language and framework.

---

## 11. Documentation

Documentation headings should use descriptive names and consistent terminology.

### Docstrings and comments

- Public functions, classes, and modules should have docstrings when their purpose or behaviour is not self-evident.
- Use Sphinx-style docstrings for Python.
- Comments should explain why something is done when the reasoning is not obvious, rather than simply repeating what the code does.
- Keep documentation close to the functionality it describes.
- Update relevant documentation when behaviour or interfaces change.

### Domain terminology

Use established ODEN terms such as:

* `recording`
* `transcript`
* `dataset`
* `memory`
* `workflow`
* `audio processing`
* `speech-to-text`

Avoid introducing alternative names for an existing concept without documenting the distinction.

---

## 12. Abbreviations

Common technical abbreviations may be used when they are widely understood:

```text
API
HTTP
URL
STT
TTS
LLM
ML
```

Otherwise, prefer the full term. For ODEN-specific concepts, use the canonical term consistently rather than creating shortened forms.

---

## 13. Naming Priority

When conventions conflict, use the following priority:

1. ODEN-specific conventions
2. Framework or ecosystem conventions
3. Language conventions
4. General readability and consistency

Conventions should be updated when the technology stack or architecture changes.