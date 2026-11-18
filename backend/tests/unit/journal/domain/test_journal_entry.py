from datetime import UTC, datetime
from unittest.mock import Mock
from uuid import UUID, uuid4

from src.journal.domain.journal_entry import JournalEntry
from src.journal.domain.contribution import VoiceContribution


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Initialization and default values
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_journal_entry_has_default_values(journal_entry):
    assert isinstance(journal_entry.id, UUID)

    assert journal_entry.title is None
    assert journal_entry.folder_id is None

    assert journal_entry.voice_contributions == []

    assert isinstance(journal_entry.created_at, datetime)
    assert isinstance(journal_entry.updated_at, datetime)


def test_journal_entry_accepts_custom_title():
    entry = JournalEntry(title="My first entry")

    assert entry.title == "My first entry"


def test_journal_entry_accepts_custom_folder_id():
    folder_id = uuid4()

    entry = JournalEntry(folder_id=folder_id)

    assert entry.folder_id == folder_id


def test_journal_entry_accepts_custom_id():
    custom_id = uuid4()

    entry = JournalEntry(id=custom_id)

    assert entry.id == custom_id


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# UUID generation
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_each_journal_entry_gets_unique_id():
    first = JournalEntry()
    second = JournalEntry()

    assert first.id != second.id


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Voice contribution collection
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_journal_entry_starts_with_empty_contributions(journal_entry):
    assert journal_entry.voice_contributions == []


def test_journal_entries_have_independent_contribution_collections():
    first = JournalEntry()
    second = JournalEntry()

    assert first.voice_contributions is not second.voice_contributions


def test_add_voice_contribution_adds_contribution(
    journal_entry,
    sample_voice_contribution,
):
    journal_entry.add_voice_contribution(sample_voice_contribution)

    assert sample_voice_contribution in journal_entry.voice_contributions


def test_add_voice_contribution_increases_collection_count(
    journal_entry,
    sample_voice_contribution,
):
    pre = journal_entry.voice_contributions.size()

    journal_entry.add_voice_contribution(sample_voice_contribution)

    assert len(journal_entry.voice_contributions) == pre + 1


def test_add_multiple_voice_contributions(journal_entry):
    first_contribution = Mock(spec=VoiceContribution)
    second_contribution = Mock(spec=VoiceContribution)

    journal_entry.add_voice_contribution(first_contribution)
    journal_entry.add_voice_contribution(second_contribution)

    assert len(journal_entry.voice_contributions) == 2

    assert journal_entry.voice_contributions == [
        first_contribution,
        second_contribution,
    ]


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# add_voice_contribution() - timestamp updates
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_add_voice_contribution_updates_timestamp(
    journal_entry,
    sample_voice_contribution,
):
    previous_updated_at = journal_entry.updated_at

    journal_entry.add_voice_contribution(sample_voice_contribution)

    assert journal_entry.updated_at >= previous_updated_at


def test_add_multiple_contributions_updates_timestamp(
    journal_entry,
):
    first_contribution = Mock(spec=VoiceContribution)
    second_contribution = Mock(spec=VoiceContribution)

    journal_entry.add_voice_contribution(first_contribution)
    first_updated_at = journal_entry.updated_at

    journal_entry.add_voice_contribution(second_contribution)

    assert journal_entry.updated_at >= first_updated_at


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Existing journal entry state
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_journal_entry_with_contribution_has_expected_state(
    journal_entry_with_contribution,
    sample_voice_contribution,
):
    assert len(journal_entry_with_contribution.voice_contributions) == 1

    assert journal_entry_with_contribution.voice_contributions[0] is sample_voice_contribution


def test_adding_contribution_does_not_change_title(
    journal_entry,
    sample_voice_contribution,
):
    journal_entry.title = "My journal entry"

    journal_entry.add_voice_contribution(sample_voice_contribution)

    assert journal_entry.title == "My journal entry"


def test_adding_contribution_does_not_change_folder_id(
    journal_entry,
    sample_voice_contribution,
):
    folder_id = uuid4()
    journal_entry.folder_id = folder_id

    journal_entry.add_voice_contribution(sample_voice_contribution)

    assert journal_entry.folder_id == folder_id
