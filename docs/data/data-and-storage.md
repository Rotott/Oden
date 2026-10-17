# Data and storage

[← Back to ODEN Architecture](../architecture/architecture.md)

## Purpose

This document defines the organization and default locations of ODEN's project resources, runtime data, models, and local configuration.

The architectural requirements governing personal data storage, external transfers, ownership, portability, and deletion should be defined in the [Data storage constraints - documentation](../../architecture/constraints/data-storage.md).


## Storage categories
| Category | Storage | Repository |
|---|---|---|
| Source code | Project repository | Included |
| Public resources | Project repository | Included |
| Audio recordings | Local private storage | Excluded |
| Transcripts | Local private storage | Excluded |
| Datasets | Local private storage | Excluded |
| Models/checkpoints | Local private storage | Excluded |
| Private configuration | Local private storage | Excluded |


## Repository data

The repository contains source code, documentation, public configuration templates, and intentionally versioned project resources.

The `data/` directory is reserved for non-private project resources, such as curated examples and public reference data, see  [`data/` directory README](../../data/README.md).

Test fixtures should generally be stored alongside the relevant test suite. Shared fixtures may be placed in a common test directory when needed. Test data containing private information shall not be committed to the repository.

Private user data, machine-specific configuration, runtime outputs, and large model artifacts shall not be committed to the repository by default.

## Runtime data location

ODEN uses a configurable runtime data root, referred to as `ODEN_DATA_DIR`.

### Development default

During development, the default location is a directory adjacent to the repository:

```text
Projects/
├── Oden/
└── Oden-data/
```

The `Oden-data/` directory is local development storage and is not part of the ODEN repository.

### Future application default

A platform-specific application data directory may replace the development default when ODEN's runtime and deployment requirements are established.

For example, on Windows:

```text
%LOCALAPPDATA%\ODEN\data\
```

The configured `ODEN_DATA_DIR` takes precedence over the default location.


## Runtime directory structure

The initial runtime directory structure is:

```text
Oden-data/
├── audio/
├── transcripts/
├── datasets/
├── models/
└── cache/
```

| Directory | Purpose |
|---|---|
| `audio/` | Audio recordings and related files |
| `transcripts/` | Transcripts and corrections |
| `datasets/` | Local datasets used for development, training, or evaluation |
| `models/` | Downloaded models and training checkpoints |
| `cache/` | Temporary or reproducible data |

Subdirectories shall be introduced as required by implemented functionality. This structure does not prescribe file formats, database schemas, or storage backends.

## Configuration

Machine-specific settings, private configuration, credentials, and local paths shall remain outside the repository.

Public configuration templates and non-sensitive examples may be included in the repository.


## Repository exclusions

Repository ignore rules shall cover private and machine-local resources, including:

- Audio recordings and private transcripts.
- Private datasets and runtime-generated files.
- Downloaded models and training checkpoints.
- Local configuration and credentials.
- Cache files and temporary processing outputs.



## Future storage changes

The current directory structure is an initial organizational convention, not a commitment to a particular storage implementation.

Future changes, including relocation to a platform-specific data directory or introduction of a database, should preserve the separation between project resources and runtime data.

[← Back to ODEN Architecture](../architecture/architecture.md)