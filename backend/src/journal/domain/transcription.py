from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

from src.journal.domain.utils import utc_now


class TranscriptionStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Transcription:
    """Represents the transcription of a recording."""

    id: UUID = field(default_factory=uuid4)
    status: TranscriptionStatus = TranscriptionStatus.PENDING
    transcription_language: str | None = None
    transcribed_text: str | None = None
    user_corrected_text: str | None = None

    model_name: str | None = None
    model_version: str | None = None

    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)
    reviewed_at: datetime | None = None

    failure_reason: str | None = None

    @property
    def active_text(self) -> str | None:
        """Return corrected text when available, otherwise generated text."""
        return self.user_corrected_text or self.transcribed_text

    @property
    def is_corrected(self) -> bool:
        return self.user_corrected_text is not None

    def mark_processing(self) -> None:
        self.status = TranscriptionStatus.PROCESSING
        self.updated_at = utc_now()

    def complete(
        self,
        generated_text: str,
        model_name: str,
        model_version: str | None = None,
    ) -> None:
        self.transcribed_text = generated_text
        self.model_name = model_name
        self.model_version = model_version
        self.status = TranscriptionStatus.COMPLETED
        self.failure_reason = None
        self.updated_at = utc_now()

    def mark_failed(self, reason: str) -> None:
        self.status = TranscriptionStatus.FAILED
        self.failure_reason = reason
        self.updated_at = utc_now()

    def apply_correction(self, corrected_text: str) -> None:
        self.user_corrected_text = corrected_text
        self.updated_at = utc_now()

    def mark_reviewed(self) -> None:
        self.reviewed_at = utc_now()
        self.updated_at = utc_now()
