import os

import pytest
from playwright.sync_api import Page

from pages.cti_toolbar_pages.cti_login_page import CtiLoginPage
from pages.cti_toolbar_pages.cti_toolbar_page import CtiToolbarPage
from utils.twilio.make_call import MakeCall
from utils.twilio.twilio_make_call import CTI


def pytest_addoption(parser):
    parser.addoption('--settings', action='store')

@pytest.fixture()
def cti_login_page(page: Page) -> CtiLoginPage:
    return CtiLoginPage(page)

@pytest.fixture()
def cti_tool_bar_page(page: Page) -> CtiToolbarPage:
    return CtiToolbarPage(page)

@pytest.fixture()
def make_call() -> MakeCall:
    return MakeCall()

@pytest.fixture()
def twilio_make_call() -> CTI:
    return CTI(os.environ.get('TWILIO_ACCOUNT_SID'), os.environ.get('TWILIO_AUTH_TOKEN'),os.environ.get('FROM_TWILIO_PHONE_NUMBER'))