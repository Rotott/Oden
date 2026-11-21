from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from src.journal.domain.utils import utc_now


@dataclass
class Recording:
    """Represents an original audio recording."""

    storage_key: str  # TODO placeholder attribute -> TBD
    duration_seconds: float  # TODO placeholder attribute -> TBD
    sample_rate: int  # TODO placeholder attribute -> TBD
    audio_format: str  # TODO placeholder attribute -> TBD

    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=utc_now)
