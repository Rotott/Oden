from datetime import UTC, datetime
from uuid import UUID

from src.journal.domain.recording import Recording


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Initialization and required attributes
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_recording_has_expected_attributes(recording):
    assert recording.storage_key == "recordings/test-recording.wav"
    assert recording.duration_seconds == 120.5
    assert recording.sample_rate == 44100
    assert recording.audio_format == "wav"


def test_recording_has_default_values(recording):
    assert isinstance(recording.id, UUID)
    assert isinstance(recording.created_at, datetime)
    assert recording.created_at is not None


def test_recording_gets_unique_id():
    first = Recording(
        storage_key="recordings/first.wav",
        duration_seconds=10.0,
        sample_rate=44100,
        audio_format="wav",
    )

    second = Recording(
        storage_key="recordings/second.wav",
        duration_seconds=10.0,
        sample_rate=44100,
        audio_format="wav",
    )

    assert first.id != second.id


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Timestamp generation
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_recordings_get_independent_timestamps():
    first = Recording(
        storage_key="recordings/first.wav",
        duration_seconds=10.0,
        sample_rate=44100,
        audio_format="wav",
    )

    second = Recording(
        storage_key="recordings/second.wav",
        duration_seconds=10.0,
        sample_rate=44100,
        audio_format="wav",
    )

    assert first.created_at is not second.created_at
