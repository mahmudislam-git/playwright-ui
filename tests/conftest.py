import os

import pytest
from playwright.sync_api import Page

from utils.twilio.twilio_make_call import CTI


def pytest_addoption(parser):
    parser.addoption('--settings', action='store')

@pytest.fixture()
def twilio_make_call() -> CTI:
    return CTI(os.environ.get('TWILIO_ACCOUNT_SID'), os.environ.get('TWILIO_AUTH_TOKEN'),os.environ.get('FROM_TWILIO_PHONE_NUMBER'))