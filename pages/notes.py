import typing

from playwright.sync_api import Page

class Notes(Page):
    URL = 'notes'

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.new_note_button = page.locator('.action-button')
        self.note_input = page.locator(".full-note-page__input textarea")
        self.save_button = page.get_by_role("button", name="Save")
        self.notes_button = page.locator('.navigation-header__text')
        self.note_list = page.locator('.notes-page__note-items')
        self.note_items = page.locator('.note-item')  #
        self.note_texts = page.locator('.note-item__extract')

    def open(self):
        self.page.goto(self.URL)

    def click_new_note(self):
        self.new_note_button.click()

    def write_note(self, text: str):
        self.note_input.click()
        self.note_input.fill(text)

    def save_note(self):
        self.save_button.click()
        # self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(3000)
        self.notes_button.click()
        self.page.wait_for_selector('.notes-page__note-items', timeout=15000)
        self.page.wait_for_selector('.note-item',timeout=15000)

    def note_is_saved(self, expected_text: str) -> bool:
        preview_text = expected_text[:10]
        self.page.wait_for_selector('.note-item', timeout=5000)
        return self.note_texts.locator(f"text={preview_text}").is_visible()