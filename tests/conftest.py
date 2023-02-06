import pytest
from playwright.sync_api import Page

from pages.callrecords_page import CallRecordsPage
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption('--settings', action='store')

@pytest.fixture()
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture()
def call_records_page(page: Page) -> CallRecordsPage:
    return CallRecordsPage(page)

