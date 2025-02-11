from playwright.sync_api import Page

from pages.nav import Nav


class Agenda(Nav):
    URL = 'agenda'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.agenda_items = page.locator('.agenda-item')
        self.agenda_titles = page.locator('.agenda-item__main__content__title')
        self.agenda_item_lobby = self.agenda_titles.filter(has=page.get_by_text("Lobby"))
    
    def open(self):
        self.page.goto(self.URL)