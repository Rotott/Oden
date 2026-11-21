from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from src.journal.domain.recording import Recording
from src.journal.domain.transcription import Transcription
from src.journal.domain.utils import utc_now


@dataclass
class VoiceContribution:
    """Represents one voice contribution to a journal entry."""

    recording: Recording
    transcription: Transcription | None = None

    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=utc_now)
