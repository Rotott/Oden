from unittest.mock import Mock
from uuid import UUID

from src.journal.domain.folder import Folder
from src.journal.domain.journal import Journal

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Initialization and default values
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_journal_has_default_values(journal):
    assert isinstance(journal.id, UUID)
    assert journal.name == "My Journal"
    assert journal.folders == []
    assert journal.entries == []


def test_journal_accepts_custom_name():
    journal = Journal(name="Personal Journal")

    assert journal.name == "Personal Journal"


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# UUID generation
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_each_journal_gets_unique_id():
    first = Journal()
    second = Journal()

    assert first.id != second.id


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Collection initialization
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_journal_starts_with_empty_folders(journal):
    assert journal.folders == []


def test_journal_starts_with_empty_entries(journal):
    assert journal.entries == []


def test_journals_have_independent_folder_collections():
    first = Journal()
    second = Journal()

    assert first.folders is not second.folders


def test_journals_have_independent_entry_collections():
    first = Journal()
    second = Journal()

    assert first.entries is not second.entries


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# add_folder()
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_add_folder_adds_folder_to_journal(
    journal,
    sample_folder,
):
    journal.add_folder(sample_folder)

    assert sample_folder in journal.folders


def test_add_folder_increases_folder_count(
    journal,
    sample_folder,
):
    pre = len(journal.folders)
    journal.add_folder(sample_folder)

    assert len(journal.folders) == pre + 1


def test_add_multiple_folders(journal):

    first_folder = Mock(spec=Folder)
    second_folder = Mock(spec=Folder)
    pre = len(journal.folders)

    journal.add_folder(first_folder)
    journal.add_folder(second_folder)

    assert len(journal.folders) == pre + 2
    assert first_folder in journal.folders
    assert second_folder in journal.folders


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# add_entry()
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_add_entry_adds_entry_to_journal(
    journal,
    sample_journal_entry,
):
    journal.add_entry(sample_journal_entry)

    assert sample_journal_entry in journal.entries


def test_add_entry_increases_entry_count(
    journal,
    sample_journal_entry,
):

    pre = len(journal.entries)
    journal.add_entry(sample_journal_entry)

    assert len(journal.entries) == pre + 1


def test_add_multiple_entries(journal):
    from unittest.mock import Mock

    from src.journal.domain.journal_entry import JournalEntry

    first_entry = Mock(spec=JournalEntry)
    second_entry = Mock(spec=JournalEntry)

    pre = len(journal.entries)
    journal.add_entry(first_entry)
    journal.add_entry(second_entry)

    assert len(journal.entries) == pre + 2
    assert first_entry in journal.entries
    assert second_entry in journal.entries


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Folder and entry independence
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_adding_folder_does_not_affect_entries(
    journal,
    sample_folder,
):
    journal.add_folder(sample_folder)

    assert journal.folders == [sample_folder]
    assert journal.entries == []


def test_adding_entry_does_not_affect_folders(
    journal,
    sample_journal_entry,
):
    journal.add_entry(sample_journal_entry)

    assert journal.entries == [sample_journal_entry]
    assert journal.folders == []
