from unittest.mock import Mock

import pytest

from src.journal.domain.contribution import VoiceContribution
from src.journal.domain.journal_entry import JournalEntry


@pytest.fixture
def journal_entry() -> JournalEntry:
    """A fresh, empty journal entry."""
    return JournalEntry()


@pytest.fixture
def sample_voice_contribution() -> VoiceContribution:
    """Mock voice contribution for testing."""
    return Mock(spec=VoiceContribution)


@pytest.fixture
def journal_entry_with_contribution(
    journal_entry: JournalEntry,
    sample_voice_contribution: VoiceContribution,
) -> JournalEntry:
    """A journal entry containing a voice contribution."""
    journal_entry.add_voice_contribution(sample_voice_contribution)
    return journal_entry
