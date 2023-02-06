import pytest
from playwright.sync_api import Page

from pages.create_new_batch import CreateNewBatch
from pages.home import HomePage
from pages.login import LoginPage
from pages.parabank.para_login_page import ParaLoginPage


def pytest_addoption(parser):
    parser.addoption('--settings', action='store')

@pytest.fixture()
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture()
def home_page(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture()
def create_new_batch_page(page: Page) -> CreateNewBatch:
    return CreateNewBatch(page)

@pytest.fixture()
def para_login_page(page: Page) -> ParaLoginPage:
    return ParaLoginPage(page)
