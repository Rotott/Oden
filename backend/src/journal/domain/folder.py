from dataclasses import dataclass, field
from uuid import UUID, uuid4

from src.journal.domain.journal_entry import JournalEntry


@dataclass
class Folder:
    """Represents an organizational folder within a journal."""

    name: str
    id: UUID = field(default_factory=uuid4)
    entries: list[JournalEntry] = field(default_factory=list)
