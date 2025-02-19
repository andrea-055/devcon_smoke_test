import typing

from playwright.sync_api import Page

class Notes(Page):
    URL = 'notes'

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.new_note_button = page.locator('.notes-page__button-text', has_text="New note")
        self.note_input = page.locator(".full-note-page__input textarea")
        self.save_button = page.get_by_role("button", name="Save")
        self.note_list = page.locator('.notes-page__note-items')  # Teljes jegyzetlista
        self.note_items = page.locator('.note-item')  # Összes jegyzet
        self.note_texts = page.locator('.note-item__extract')  # A jegyzetek tartalmának előnézete

    def open(self):
        self.page.goto(self.URL)

    def click_new_note(self):
        self.new_note_button.click()

    def write_note(self, text: str):
        self.note.input.click()
        self.note.input.fill(text)

    def save_note(self):
        self.save.button.click()

    def note_is_saved(self, expected_text: str) -> bool:
        preview_text = expected_text[:10]
        return self.note_texts.locator(f"text={preview_text}").is_visible()