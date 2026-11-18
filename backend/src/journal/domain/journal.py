from dataclasses import dataclass, field
from uuid import UUID, uuid4

from src.journal.domain.folder import Folder
from src.journal.domain.journal_entry import JournalEntry


@dataclass
class Journal:
    """Represents the user's journal and its organizational structure."""

    id: UUID = field(default_factory=uuid4)  # TODO placeholder for db impl.
    name: str = "My Journal"  # Default value

    folders: list[Folder] = field(default_factory=list)  # TODO placeholder for db impl.
    entries: list[JournalEntry] = field(default_factory=list)  # TODO placeholder for db impl. |
    # TODO TBD if entries should be replaced with a default/unasigned folder
    # TODO --> can add one default folder (eg. folders[0]) and remove entries and sub func.

    def add_folder(self, folder: Folder) -> None:
        self.folders.append(folder)

    def add_entry(self, entry: JournalEntry) -> None:
        self.entries.append(entry)
