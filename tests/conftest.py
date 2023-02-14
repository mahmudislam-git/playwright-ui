import pytest
from playwright.sync_api import Page

from pages.cti_toolbar_pages.cti_login_page import CtiLoginPage
from pages.cti_toolbar_pages.cti_toolbar_page import CtiToolbarPage

def pytest_addoption(parser):
    parser.addoption('--settings', action='store')

@pytest.fixture()
def cit_login_page(page: Page) -> CtiLoginPage:
    return CtiLoginPage(page)

@pytest.fixture()
def cit_login_page(page: Page) -> CtiToolbarPage:
    return CtiToolbarPage(page)