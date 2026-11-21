from unittest.mock import Mock

import pytest

from src.journal.domain.folder import Folder
from src.journal.domain.journal import Journal
from src.journal.domain.journal_entry import JournalEntry


@pytest.fixture
def journal() -> Journal:
    """A fresh, empty journal."""
    return Journal()


@pytest.fixture
def sample_folder() -> Folder:
    """Mock folder for testing."""
    return Mock(spec=Folder)


@pytest.fixture
def sample_journal_entry() -> JournalEntry:
    """A mock journal entry for testing."""
    return Mock(spec=JournalEntry)
