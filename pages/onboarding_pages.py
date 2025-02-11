from playwright.sync_api import Page


class Onboard_Page(Page):
    URL = ''
    HEADTEXT = ''

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.header_text = page.locator('.welcome-page__header')
        self.next_button = page.get_by_role('button', name='Next')
        self.previous_button = page.get_by_role('button', name='Back')

    def open(self):
        self.page.goto(self.URL)

    def click_next_button(self):
        self.next_button.click()
   
    def click_back_button(self):
        self.previous_button.click()
 

class Onboard_Join(Onboard_Page):
    URL = 'welcome1'
    HEADTEXT = 'Privacy first communication platform'

    def __init__(self, page: Page) -> None:
        super().__init__(page)


class Onboard_Discuss(Onboard_Page):
    URL = 'welcome2'
    HEADTEXT = 'Share your thoughts'

    def __init__(self, page: Page) -> None:
        super().__init__(page)


class Onboard_Swarm(Onboard_Page):
    URL = 'welcome3'
    HEADTEXT = 'Experience the power of true decentalization'

    def __init__(self, page: Page) -> None:
        super().__init__(page)


class Onboard_Stay(Onboard_Page):
    URL = 'welcome4'
    HEADTEXT = 'Stay with Swarm'

    def __init__(self, page: Page) -> None:
        super().__init__(page)