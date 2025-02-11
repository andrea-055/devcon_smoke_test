from playwright.sync_api import Page

from pages.nav import Nav


class Spaces(Nav):
    URL = 'spaces'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.space_items = page.locator('.recent-rooms-item')
    
    def open(self):
        self.page.goto(self.URL)