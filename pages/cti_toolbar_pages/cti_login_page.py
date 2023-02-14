import os
from playwright.sync_api import Page
from simple_settings import settings
class CtiLoginPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.URL = settings.URL
        self.username = os.environ.get('BATCH_UI_USERNAME')
        self.password = os.environ.get('BATCH_UI_PASSOWORD')
        self.username_input = page.get_by_role("textbox",name="User ID")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role( "link", name="Login")

    def login_into_application(self) -> None:
        print(self.URL)
        self.page.goto(self.URL)

        self.launch_application()
        self.username_input.wait_for()
        self.username_input.click()
        self.username_input.fill(self.username)

        self.password_input.click()
        self.password_input.fill(self.password)

        self.login_button.click()