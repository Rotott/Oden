# Data

This directory contains intentionally versioned, non-private data that belongs to the Oden project.

It may include example data, public reference resources, and other curated files used for development, demonstration, or evaluation.

Private user data, runtime-generated files, large datasets, and model artifacts shall be stored outside the repository unless explicitly designated as public project resources.

## Examples

Example data used to demonstrate Oden's functionality, such as sample audio recordings and corresponding transcripts.

## Reference data

Public reference resources intentionally included in the repository for development, evaluation, or reproducibility.

## Data storage

Automated test fixtures should generally be stored alongside the relevant tests under `tests/fixtures/`.

Runtime data, including user recordings, transcripts, private datasets, models, and checkpoints, shall be stored outside the repository.

The organization, storage locations, and handling of project and runtime data are defined in the [Data and Storage](../docs/data/data-and-storage.md) documentation.