from playwright.sync_api import Page


class Profile_Creation(Page):
    URL = 'profilecreation'
    HEADTEXT = 'Create Your profile'

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.header_text = page.locator('.welcome-page__header')
        self.input_name = page.locator('.profile-creation__user-input__input')
        self.register_button = page.get_by_role('button', name='Start Building Your Community')
        self.edit_name_button = page.locator('.edit-icon')
        self.username = ''
    
    def open(self):
        self.page.goto(self.URL)
        self.page.wait_for_function('() => localStorage.username != ""')

    def edit_name(self, username: str):
        if self.input_name.is_disabled():
            self.edit_name_button.click()
            self.input_name.type(username)
            self.edit_name_button.click()

    def register_as(self, username = ''):
        if username != '':
            self.edit_name(username)
        self.username = self.input_name.input_value()
        self.register_button.click()