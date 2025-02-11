from playwright.sync_api import Page


class Nav(Page):
    
    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.footer_navigation = page.locator('.navigation-footer')
        self.nav_home = self.footer_navigation.get_by_text('Home')
        self.nav_agenda = self.footer_navigation.get_by_text('Agenda')
        self.nav_spaces = self.footer_navigation.get_by_text('Spaces')
        self.nav_notes = self.footer_navigation.get_by_text('Notes')