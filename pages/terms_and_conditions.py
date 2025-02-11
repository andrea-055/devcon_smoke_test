from playwright.sync_api import Page


class Terms_And_Conditions(Page):
    URL = 'terms-and-conditions-onboarding'
    HEADTEXT = 'Terms and Conditions'

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.header_text = page.locator('.terms-and-conditions-onboarding-page__header')
        self.checkboxes = page.get_by_role('img')
        self.usvsc_checkbox = page.get_by_text('USCVS enabled').locator(self.checkboxes)
        self.tc_checkbox = page.get_by_text('Agree with Terms and Conditions').locator(self.checkboxes)
        self.next_button = page.get_by_role('button', name="Let’s go")
        self.previous_button = page.get_by_role('button', name='Back')

    def open(self):
        self.page.goto(self.URL)

    def click_next_button(self):
        self.next_button.click()

    def click_back_button(self):
        self.previous_button.click()

    def switch_tc(self):
        self.tc_checkbox.click()