import pytest

from src.journal.domain.recording import Recording


@pytest.fixture
def recording() -> Recording:
    """A standard ~2min audio recording."""
    return Recording(
        storage_key="recordings/test-recording.wav",
        duration_seconds=120.5,
        sample_rate=44100,
        audio_format="wav",
    )


@pytest.fixture
def short_recording() -> Recording:
    """A short 5sek audio recording."""
    return Recording(
        storage_key="recordings/short-recording.mp3",
        duration_seconds=5.0,
        sample_rate=22050,
        audio_format="mp3",
    )
