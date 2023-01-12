import os

from playwright.sync_api import Page
from simple_settings import settings


class LoginPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.URL = settings.URL
        self.username = os.environ.get('BATCH_UI_USERNAME')
        self.password = os.environ.get('BATCH_UI_PASSOWORD')
        self.username_input = page.locator('input[type="text"]')
        self.password_input = page.locator('input[type="password"]')
        self.login_button = page.get_by_role(self, "button", name="Login")

    def load(self) -> None:
        print(self.URL)
        self.page.goto(self.URL)

    def login(self) -> None:
        self.username_input.click()
        self.username_input.fill(self.username)

        self.password_input.click()
        self.password_input.fill(self.password)

        self.login_button.click()
