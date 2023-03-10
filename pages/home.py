from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.create_new_batch_button = page.locator('g > g > path')

    def click_create_new_batch(self):
        self.create_new_batch_button.first.click()