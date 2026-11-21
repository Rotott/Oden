from uuid import UUID

from src.journal.domain.transcription import (
    Transcription,
    TranscriptionStatus,
)

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Initialization and default values
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_transcription_has_default_values(transcription):
    assert isinstance(transcription.id, UUID)
    assert transcription.status == TranscriptionStatus.PENDING

    assert transcription.transcription_language is None
    assert transcription.transcribed_text is None
    assert transcription.user_corrected_text is None

    assert transcription.model_name is None
    assert transcription.model_version is None

    assert transcription.created_at is not None
    assert transcription.updated_at is not None
    assert transcription.reviewed_at is None

    assert transcription.failure_reason is None


def test_transcription_gets_unique_id():
    first = Transcription()
    second = Transcription()

    assert first.id != second.id


def test_transcription_gets_independent_timestamps():
    first = Transcription()
    second = Transcription()

    assert first.created_at is not second.created_at
    assert first.updated_at is not second.updated_at


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# TranscriptionStatus enum
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_transcription_status_has_expected_values():
    assert TranscriptionStatus.PENDING.value == "pending"
    assert TranscriptionStatus.PROCESSING.value == "processing"
    assert TranscriptionStatus.COMPLETED.value == "completed"
    assert TranscriptionStatus.FAILED.value == "failed"


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# active_text property
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_active_text_returns_none_when_no_text_exists(transcription):
    assert transcription.active_text is None


def test_active_text_returns_generated_text_when_no_correction(
    completed_transcription,
):
    assert completed_transcription.active_text == "Today was a good day."


def test_active_text_returns_corrected_text_when_available(
    corrected_transcription,
):
    assert corrected_transcription.active_text == ("Today was an excellent day.")


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# is_corrected property
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_is_corrected_returns_false_by_default(transcription):
    assert transcription.is_corrected is False


def test_is_corrected_returns_true_after_correction(
    corrected_transcription,
):
    assert corrected_transcription.is_corrected is True


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# mark_processing()
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_mark_processing_updates_status(transcription):
    transcription.mark_processing()

    assert transcription.status == TranscriptionStatus.PROCESSING


def test_mark_processing_updates_timestamp(transcription):
    previous_updated_at = transcription.updated_at

    transcription.mark_processing()

    assert transcription.updated_at >= previous_updated_at


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# complete()
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_complete_updates_transcription_data(transcription):
    transcription.complete(
        generated_text="Hello world",
        model_name="whisper",
        model_version="1.0",
    )

    assert transcription.transcribed_text == "Hello world"
    assert transcription.model_name == "whisper"
    assert transcription.model_version == "1.0"
    assert transcription.status == TranscriptionStatus.COMPLETED
    assert transcription.failure_reason is None


def test_complete_accepts_missing_model_version(transcription):
    transcription.complete(
        generated_text="Hello world",
        model_name="whisper",
    )

    assert transcription.model_version is None


def test_complete_clears_previous_failure_reason(failed_transcription):
    failed_transcription.complete(
        generated_text="Successfully transcribed",
        model_name="whisper",
    )

    assert failed_transcription.status == TranscriptionStatus.COMPLETED
    assert failed_transcription.failure_reason is None


def test_complete_updates_timestamp(transcription):
    previous_updated_at = transcription.updated_at

    transcription.complete(
        generated_text="Hello world",
        model_name="whisper",
    )

    assert transcription.updated_at >= previous_updated_at


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# mark_failed()
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_mark_failed_updates_status_and_reason(transcription):
    transcription.mark_failed("Something went wrong")

    assert transcription.status == TranscriptionStatus.FAILED
    assert transcription.failure_reason == "Something went wrong"


def test_mark_failed_updates_timestamp(transcription):
    previous_updated_at = transcription.updated_at

    transcription.mark_failed("Something went wrong")

    assert transcription.updated_at >= previous_updated_at


def test_failed_transcription_has_expected_state(failed_transcription):
    assert failed_transcription.status == TranscriptionStatus.FAILED
    assert failed_transcription.failure_reason == ("Transcription service unavailable")


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# apply_correction()
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_apply_correction_stores_corrected_text(
    completed_transcription,
):
    completed_transcription.apply_correction("Corrected text")

    assert completed_transcription.user_corrected_text == "Corrected text"


def test_apply_correction_updates_active_text(
    completed_transcription,
):
    completed_transcription.apply_correction("Corrected text")

    assert completed_transcription.active_text == "Corrected text"


def test_apply_correction_marks_transcription_as_corrected(
    completed_transcription,
):
    completed_transcription.apply_correction("Corrected text")

    assert completed_transcription.is_corrected is True


def test_apply_correction_updates_timestamp(transcription):
    previous_updated_at = transcription.updated_at

    transcription.apply_correction("Corrected text")

    assert transcription.updated_at >= previous_updated_at


def test_apply_correction_does_not_change_status(
    completed_transcription,
):
    previous_status = completed_transcription.status

    completed_transcription.apply_correction("Corrected text")

    assert completed_transcription.status == previous_status


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# mark_reviewed()
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_mark_reviewed_sets_reviewed_at(transcription):
    transcription.mark_reviewed()

    assert transcription.reviewed_at is not None


def test_mark_reviewed_updates_updated_at(transcription):
    previous_updated_at = transcription.updated_at

    transcription.mark_reviewed()

    assert transcription.updated_at >= previous_updated_at


def test_mark_reviewed_sets_both_reviewed_at_and_updated_at_timestamps(transcription):
    transcription.mark_reviewed()

    assert transcription.reviewed_at is not None
    assert transcription.updated_at >= transcription.reviewed_at


def test_mark_reviewed_does_not_change_status(
    completed_transcription,
):
    previous_status = completed_transcription.status

    completed_transcription.mark_reviewed()

    assert completed_transcription.status == previous_status
