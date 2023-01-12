import os

from playwright.sync_api import Page
from simple_settings import settings


class LoginPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.URL = settings.URL
        self.username = os.environ.get('BATCH_UI_USERNAME')
        self.password = os.environ.get('BATCH_UI_PASSOWORD')
        self.username_input = page.locator('#username')
        self.password_input = page.locator('#password')
        self.login_button = page.locator("#login")

    def load(self) -> None:
        print(self.URL)
        self.page.goto(self.URL)

    def login(self) -> None:
        self.username_input.fill(self.username)
        self.password_input.fill(self.password)
        self.login_button.click()