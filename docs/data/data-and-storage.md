# Data and storage

[← Back to  ODEN Architecture](../architecture/architecture.md)


This document defines how ODEN separates source code, public project
resources, and private user data.

## Storage categories

| Category | Storage | Repository |
|---|---|---|
| Source code | Project repository | Included |
| Public resources | Project repository | Included |
| Audio recordings | Local private storage | Excluded |
| Transcripts | Local private storage | Excluded |
| Datasets | Local private storage | Excluded |
| Models/checkpoints | Local model storage | Excluded |
| Private configuration | Local configuration storage | Excluded |

## Private data

Private user data shall be stored outside the version-controlled
repository.

### Audio

User-recorded audio is stored in:

`<defined path>` **TBD**

### Transcripts

User transcripts are stored in:

`<defined path>` **TBD**

### Datasets

Private datasets are stored in:

`<defined path>` **TBD**

## Models and checkpoints

Model files and training checkpoints are treated as local resources
rather than repository content. They shall be stored outside the source tree unless a specific model artifact is intentionally designated as a public project resource.

## Configuration

Private configuration, including credentials, local paths, and other
machine- or user-specific settings, shall not be committed to the
repository. Public configuration templates may be included in the repository.

## Repository exclusions

Private data and machine-local resources shall be excluded using the
repository's ignore rules.

Examples include:

- Audio recordings
- Private transcripts
- Private datasets
- Model/checkpoint files
- Local configuration
- Runtime-generated data

## Data ownership

User-generated audio, transcripts, datasets, and other private data
remain user-owned data. ODEN's source repository contains the software and intentionally public project resources, not users' private data.


[← Back to  ODEN Architecture](architecture.md)
