# Processing metadata and traceability

[← Back to ODEN Architecture](../architecture.md)

## 1. Purpose and principles

This document defines the metadata required to identify ODEN artifacts and trace significant processing operations.

- Each artifact has a unique, stable identifier
- Artifacts are immutable during normal processing. Corrections and regenerated outputs create new artifacts and are connected through explicit references.
- Timestamps use ISO 8601 date-time format with UTC, e.g. `2026-10-21T12:12:05Z`.

## 2. Identifiers and processing metadata

ODEN uses the following identifiers:

- `recording_id`: identifies an unique audio recording.
- `transcript_id`: identifies a unique transcript artifact.
- `model_id` and `model_version`: identify the model and the specific version used.
- `dataset_id` and `dataset_version`: identify a dataset and its specific version.
- `processing_run_id`: identifies a significant processing execution.

Processing metadata should record, where applicable, the operation type, start and completion timestamps, execution status, input and output artifact IDs, model/version, configuration version, and relevant error information.

Dataset versions and training/evaluation experiments should reference their source data and relevant model, dataset, and configuration versions where practical.

## 3. Artifact content and provenance

Artifact content and metadata are conceptually distinct. Their physical storage may be combined or separate, depending on implementation.

- A transcript references its source recording.
- A revised transcript receives a new ID and references the transcript from which it was derived.
- A processing run references its inputs and outputs.
- A dataset version references its source artifacts and generation configuration where practical.

Original artifacts must not be silently overwritten. Provenance must be preserved through structured metadata or persistent references, not filenames alone.

## 4. Conceptual artifact examples

The following JSON examples illustrate the intended information, not a finalized schema or storage format.

### 4.1 Audio recording

**Conceptual filename:** `recording_20261021_121200.wav`

*The filename is descriptive and may change independently of the recording's identifier.*

**Metadata:**

```json
{
  "recording_id": "rec-UUID",
  "created_at": "2026-10-21T12:12:00Z",
  "device_id": "microphone-01",
  "file_name": "recording_20261021_121200.wav",
  "media_type": "audio/wav"
}
```

### 4.2 Raw transcript

**Conceptual filename:** `transcript_20261021_121205_<transcript_id>.json`

**Metadata and content:**

```json
{
  "metadata": {
    "transcript_id": "trans-UUID-1",
    "source_recording_id": "rec-UUID",
    "created_at": "2026-10-21T12:12:05Z",
    "transcript_type": "machine_generated",
    "review_status": "unreviewed",
    "model_id": "stt-model-x",
    "model_version": "1.2",
    "processing_run_id": "run-UUID"
  },
  "content": {
    "text": "Example transcribed text."
  }
}
```

### 4.3 Revised transcript

**Conceptual filename:** `transcript_20261021_122000_<transcript_id>.json`

**Metadata and content:**

```json
{
  "metadata": {
    "transcript_id": "trans-UUID-2",
    "source_recording_id": "rec-UUID",
    "derived_from_transcript_id": "trans-UUID-1",
    "created_at": "2026-10-21T12:20:00Z",
    "transcript_type": "user_corrected",
    "review_status": "reviewed"
  },
  "content": {
    "text": "Example corrected text."
  }
}
```

The revised transcript retains its own identity and links to both the source recording and the raw transcript. Model provenance can be traced through the raw transcript unless new model processing was performed.

## 5. Conceptual processing and dataset metadata

### 5.1 Processing run

```json
{
  "processing_run_id": "run-UUID",
  "operation_type": "transcription",
  "started_at": "2026-10-21T12:12:01Z",
  "completed_at": "2026-10-21T12:12:05Z",
  "status": "completed",
  "input_ids": ["rec-UUID"],
  "output_ids": ["trans-UUID"],
  "model_id": "stt-model-x",
  "model_version": "1.2",
  "configuration_version": "stt-config-1"
}
```

### 5.2 Dataset version

```json
{
  "dataset_id": "dataset-a",
  "dataset_version": "1",
  "created_at": "2026-10-21T13:00:00Z",
  "source_artifact_ids": ["rec-UUID", "trans-UUID"],
  "generation_configuration_version": "dataset-config-1"
}
```


## 6. Scope and implementation

This document defines conceptual traceability rules, not database structures, programming classes, or file formats. Implementation details may be specified in relevant technical documentation.

[← Back to ODEN Architecture](../architecture.md)