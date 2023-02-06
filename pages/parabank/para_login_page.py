from playwright.sync_api import Page
from simple_settings import settings


class ParaLoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.URL = settings.URL
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[type="password"]')
        self.login_button = page.get_by_role("button", name="Log In")
        self.logout_button = page.get_by_role("link", name="Log Out")

    def load_url(self) -> None:
        print(self.URL)
        self.page.goto(self.URL)

    def para_login(self, para_username, para_password) -> None:
        self.username_input.click()
        self.username_input.fill(para_username)

        self.password_input.click()
        self.password_input.fill(para_password)

        self.login_button.click()
        self.logout_button.click()