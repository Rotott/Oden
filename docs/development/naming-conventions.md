# Naming conventions for ODEN


## 1. Purpose

This document defines the naming conventions intended to be followed throughout ODEN’s source code, configuration, data, tests, and documentation.

**Language-specific conventions should follow the relevant ecosystem's standard unless an ODEN convention explicitly overrides them.**

---

## 2. General Principles

* Prefer clear, descriptive names over short names.
* Use consistent domain terminology across components.
* Avoid unnecessary abbreviations.
* Use names that describe **what something represents or does**, rather than its implementation.
* Use nouns for data and concepts, and verbs for actions.
* Avoid reusing the same term for different concepts.

ODEN-specific terminology should be defined consistently with the [architecture documentation](../architecture/architecture.md).

---

## 3. Python

Python code should generally follow **PEP 8**.

| Element         | Convention            | Example              |
| --------------- | --------------------- | -------------------- |
| Variables       | `snake_case`          | `audio_path`         |
| Functions       | `snake_case`          | `process_audio()`    |
| Classes         | `PascalCase`          | `AudioProcessor`     |
| Constants       | `UPPER_SNAKE_CASE`    | `MAX_AUDIO_LENGTH`   |
| Modules/files   | `snake_case`          | `audio_processor.py` |
| Private members | `_leading_underscore` | `_load_audio()`      |

Boolean names should normally use a descriptive prefix such as `is_`, `has_`, `can_`, or `should_`.

```python
is_recording
has_transcript
can_process
```

---

## 4. TypeScript / React

TypeScript and React code should follow the established conventions of the ecosystem and project tooling.

| Element          | Convention                          | Example            |
| ---------------- | ----------------------------------- | ------------------ |
| Variables        | `camelCase`                         | `audioPath`        |
| Functions        | `camelCase`                         | `processAudio()`   |
| Classes / types  | `PascalCase`                        | `AudioProcessor`   |
| React components | `PascalCase`                        | `AudioPlayer`      |
| Constants        | `UPPER_SNAKE_CASE` when appropriate | `MAX_AUDIO_LENGTH` |
| Files            | Follow exported symbol              | `AudioPlayer.tsx`  |

Boolean names should use descriptive prefixes such as `is`, `has`, `can`, or `should`.

```ts
isRecording
hasTranscript
canProcess
```

---

## 5. Database and Data

DB tables, columns, constraints, and persistent data identifiers should use `snake_case`. 

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


* **Foreign Keys:** Name foreign keys explicitly as <singular_target_table>_id (e.g., recording_id).
* **Indexes:** Prefix indexes with idx_ followed by the table and column names (e.g., idx_recordings_created_at).
* **Database File:** A local DB file should be clean and environment-agnostic, such as oden.db or oden.sqlite3.


Database names should describe the **domain concept**, not the implementation that currently stores it.

---

## 6. API

API routes should use lowercase, plural resource names where appropriate.

```text
/api/recordings
/api/transcripts
/api/datasets
```

JSON fields should use `snake_case` unless a documented API convention requires otherwise.

---

## 7. Tests

Test files must mirror the structure of the source code or sit right alongside the implementation. Test names must clearly describe the behavior being verified rather than just the function name.

Python:

```python
test_process_audio_returns_transcript()
test_invalid_audio_is_rejected()
```

Python test functions should follow a predictable behavioral pattern: 
`test_<unit>_<scenario>_<expected_result>()`

```text
# Patterns
def test_audio_processor_with_invalid_file_raises_value_error():
    ...

def test_transcriber_returns_valid_transcript_on_success():
    ...
``` 

TypeScript:

TypeScript test files must mirror their corresponding source file name, appending .test.ts or .test.tsx.

```text
processAudio.test.ts
AudioPlayer.test.tsx
```

```text
# Patterns

// Inside AudioPlayer.test.tsx
it('should render the audio controls when a recording is loaded', () => { ... });

// Inside audioUtils.test.ts
it('should reject invalid audio formats', () => { ... });

```

**Tests should use the same terminology as the functionality they validate.** Avoid lazy or generic names like test_data() or test_works().

---

## 8. Files and Directories

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

## 9. Documentation

Documentation headings should use descriptive names and consistent terminology.

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

## 10. Abbreviations

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

## 11. Naming Priority

When conventions conflict, use the following priority:

1. ODEN-specific conventions
2. Framework or ecosystem conventions
3. Language conventions
4. General readability and consistency

Conventions should be updated when the technology stack or architecture changes.
