from playwright.sync_api import Page


class Profile(Page):
    URL = 'profile'

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.username = page.locator('.profile__username')
    
    def open(self):
        self.page.goto(self.URL)