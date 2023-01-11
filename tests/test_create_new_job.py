from playwright.sync_api import Page

from pages.create_new_batch import CreateNewBatch
from pages.home import HomePage
from pages.login import LoginPage


def test_create_new_batch(page: Page, login_page: LoginPage,
                          home_page: HomePage, create_new_batch_page: CreateNewBatch) -> None:

    login_page.login()
    home_page.click_create_new_batch()
    create_new_batch_page.create_new_batch()