from unittest.mock import Mock
from uuid import UUID, uuid4

from src.journal.domain.folder import Folder
from src.journal.domain.journal_entry import JournalEntry

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Initialization and default values
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_folder_has_default_values(folder):
    assert folder.name == "My Folder"
    assert isinstance(folder.id, UUID)
    assert folder.entries == []


def test_folder_accepts_custom_name():
    folder = Folder(name="Work")

    assert folder.name == "Work"


def test_folder_accepts_custom_id():
    custom_id = uuid4()

    folder = Folder(
        name="Work",
        id=custom_id,
    )

    assert folder.id == custom_id


def test_folder_accepts_custom_entries():
    first_entry = Mock(spec=JournalEntry)
    second_entry = Mock(spec=JournalEntry)

    folder = Folder(
        name="Work",
        entries=[first_entry, second_entry],
    )

    assert folder.entries == [first_entry, second_entry]


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# UUID generation
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_each_folder_gets_unique_id():
    first = Folder(name="First Folder")
    second = Folder(name="Second Folder")

    assert first.id != second.id


def test_folder_id_is_valid_uuid(folder):
    assert isinstance(folder.id, UUID)


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Entries collection
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_folder_starts_with_empty_entries(folder):
    assert folder.entries == []


def test_folders_have_independent_entry_collections():
    first = Folder(name="First Folder")
    second = Folder(name="Second Folder")

    assert first.entries is not second.entries


def test_folder_with_entries_contains_expected_entries(
    folder_with_entries,
):
    assert len(folder_with_entries.entries) == 2


def test_folder_preserves_entry_order(folder_with_entries):
    first_entry, second_entry = folder_with_entries.entries

    assert first_entry is not second_entry


def test_adding_entry_to_folder_updates_entries_collection(
    folder,
):
    entry = Mock(spec=JournalEntry)

    folder.entries.append(entry)

    assert entry in folder.entries
    assert len(folder.entries) == 1


def test_adding_entries_does_not_affect_other_folders(folder):
    another_folder = Folder(name="Another Folder")
    entry = Mock(spec=JournalEntry)

    folder.entries.append(entry)

    assert folder.entries == [entry]
    assert another_folder.entries == []


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Folder independence
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


def test_folders_have_independent_names():
    first = Folder(name="Work")
    second = Folder(name="Personal")

    assert first.name != second.name


def test_changing_folder_name_does_not_affect_other_folder():
    first = Folder(name="Work")
    second = Folder(name="Personal")

    first.name = "Projects"

    assert first.name == "Projects"
    assert second.name == "Personal"
