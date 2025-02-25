import pytest
from datetime import datetime
from pages.notes import Notes

@pytest.mark.registered
def test_create_and_save_note(notes: Notes):
    notes.open()
    notes.click_new_note()

    now = datetime.now()
    test_text = f"this is a test note {now.hour}:{now.minute}:{now.second}"

    notes.write_note(test_text)
    notes.save_note()

    assert notes.note_is_saved(test_text), "There is no new note in the list!"