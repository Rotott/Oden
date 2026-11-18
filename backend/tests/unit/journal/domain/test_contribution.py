from datetime import datetime
from uuid import UUID, uuid4

from src.journal.domain.contribution import VoiceContribution
from src.journal.domain.recording import Recording
from src.journal.domain.transcription import Transcription


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Initialization and default values
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_voice_contribution_has_default_values(voice_contribution):
    assert isinstance(voice_contribution.id, UUID)
    assert isinstance(voice_contribution.recording, Recording)

    assert voice_contribution.transcription is None
    assert isinstance(voice_contribution.created_at, datetime)


def test_voice_contribution_accepts_recording(recording):
    contribution = VoiceContribution(recording=recording)

    assert contribution.recording is recording


def test_voice_contribution_accepts_transcription(
    recording,
    completed_transcription,
):
    contribution = VoiceContribution(
        recording=recording,
        transcription=completed_transcription,
    )

    assert contribution.transcription is completed_transcription


def test_voice_contribution_accepts_custom_id(recording):
    custom_id = uuid4()

    contribution = VoiceContribution(
        id=custom_id,
        recording=recording,
    )

    assert contribution.id == custom_id


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# UUID generation
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_each_voice_contribution_gets_unique_id(recording):
    first = VoiceContribution(recording=recording)
    second = VoiceContribution(recording=recording)

    assert first.id != second.id


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Transcription relationship
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_voice_contribution_can_exist_without_transcription(
    voice_contribution,
):
    assert voice_contribution.transcription is None


def test_voice_contribution_can_exist_with_transcription(
    voice_contribution_with_transcription,
):
    assert isinstance(
        voice_contribution_with_transcription.transcription,
        Transcription,
    )


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Timestamp generation
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_voice_contribution_created_at_is_datetime(
    voice_contribution,
):
    assert isinstance(voice_contribution.created_at, datetime)


def test_voice_contributions_have_independent_timestamps(recording):
    first = VoiceContribution(recording=recording)
    second = VoiceContribution(recording=recording)

    assert first.created_at is not second.created_at
