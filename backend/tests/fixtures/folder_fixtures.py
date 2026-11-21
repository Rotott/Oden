from unittest.mock import Mock

import pytest

from src.journal.domain.folder import Folder
from src.journal.domain.journal_entry import JournalEntry


@pytest.fixture
def folder() -> Folder:
    """A fresh, empty folder."""
    return Folder(name="My Folder")


@pytest.fixture
def folder_with_entries() -> Folder:
    """Folder containing two journal entries."""
    first_entry = Mock(spec=JournalEntry)
    second_entry = Mock(spec=JournalEntry)

    return Folder(
        name="My Folder",
        entries=[first_entry, second_entry],
    )
