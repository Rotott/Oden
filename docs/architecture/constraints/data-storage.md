# Data storage
[← Go back](constraints.md)

## Purpose

This document defines the architectural requirements for storing and handling personal data in ODEN. ODEN is intended to give users local control over their personal data. Local storage is therefore the default.

## Local storage

Personal data generated or collected by ODEN shall be stored locally by default. This includes, where applicable:

* Audio recordings
* Transcripts
* Corrected transcripts
* Personal memory
* User-generated metadata
* Locally generated datasets
* Application state containing personal information

Core functionality shall not require cloud storage for access to personal data.

## External storage

External or cloud storage may be supported as an optional feature.

If supported:

* It shall be explicitly identified as optional.
* It shall not be required for core functionality.
* The user shall be able to continue using ODEN locally without it.
* The data transferred to the external service shall be clearly defined.
* Credentials and access information shall not be stored in the public repository.

## Data leaving the local system

Personal data shall not leave the local system implicitly. Any feature that transfers personal data to an external service shall:

* Be explicitly identifiable as using an external service.
* Document what data is transferred.
* Document the purpose of the transfer.
* Identify the external service involved.
* Be treated as optional functionality.

## Data ownership and portability

ODEN should avoid proprietary or unnecessarily restrictive storage formats for personal data. Users should be able to access and export their personal data without depending on an external service. Where practical, important user data should use documented or commonly readable formats.

## Data deletion

Users should be able to remove locally stored personal data without requiring access to an external service. Features that create derived or cached copies of personal data should document where those copies are stored and how they can be removed.

## Architectural implications

Components that access personal data should not assume that the data is stored remotely. Storage implementations should be replaceable where practical so that local storage remains the default while alternative storage mechanisms can be introduced as optional functionality.



[← Go back](constraints.md)
