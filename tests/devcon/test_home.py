from playwright.sync_api import expect
from tests.devcon.conftest import *


@pytest.mark.registered
def test_agenda_is_accessible(home, agenda):
    home.open()
    home.nav_agenda.click()
    expect(agenda.agenda_item_lobby).to_be_visible(timeout=20000)

@pytest.mark.registered
def test_spaces_is_accessible(home, spaces):
    home.open()
    home.nav_spaces.click()
    expect(spaces.space_items).to_have_count(12)
    