from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from src.journal.domain.contribution import VoiceContribution
from src.journal.domain.utils import utc_now


@dataclass
class JournalEntry:
    """Represents one logical journal entry."""

    id: UUID = field(default_factory=uuid4)
    title: str | None = None
    folder_id: UUID | None = None

    voice_contributions: list[VoiceContribution] = field(default_factory=list)

    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    def add_voice_contribution(
        self,
        contribution: VoiceContribution,
    ) -> None:
        self.voice_contributions.append(contribution)
        self.updated_at = utc_now()
