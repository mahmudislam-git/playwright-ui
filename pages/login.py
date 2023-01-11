from playwright.sync_api import Page


class LoginPage:

    URL = 'website link'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.locator('#username')
        self.password_input = page.locator('#password')
        self.login_button = page.locator("#login")

    def load(self) -> None:
        self.page.goto(self.URL)

    def login(self) -> None:
        self.username_input.fill("username")
        self.password_input.fill("password")
        self.login_button.click()