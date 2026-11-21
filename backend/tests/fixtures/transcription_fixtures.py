import pytest

from src.journal.domain.transcription import Transcription


@pytest.fixture
def transcription() -> Transcription:
    """A fresh, unprocessed transcription."""
    return Transcription()


@pytest.fixture
def completed_transcription(
    transcription: Transcription,
) -> Transcription:
    """A transcription that has completed processing."""
    transcription.complete(
        generated_text="Today was a good day.",
        model_name="whisper",
        model_version="1.0",
    )
    return transcription


@pytest.fixture
def corrected_transcription(
    completed_transcription: Transcription,
) -> Transcription:
    """A completed transcription with user corrections."""
    completed_transcription.apply_correction("Today was an excellent day.")
    return completed_transcription


@pytest.fixture
def failed_transcription(
    transcription: Transcription,
) -> Transcription:
    """Create a transcription that has failed processing."""
    transcription.mark_failed("Transcription service unavailable")
    return transcription
