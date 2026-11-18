import pytest

from src.journal.domain.contribution import VoiceContribution
from src.journal.domain.recording import Recording
from src.journal.domain.transcription import Transcription


@pytest.fixture
def voice_contribution(
    recording: Recording,
) -> VoiceContribution:
    """voice contribution without a transcription."""
    return VoiceContribution(
        recording=recording,
    )


@pytest.fixture
def voice_contribution_with_transcription(
    recording: Recording,
    completed_transcription: Transcription,
) -> VoiceContribution:
    """A voice contribution with a completed transcription ."""
    return VoiceContribution(
        recording=recording,
        transcription=completed_transcription,
    )
