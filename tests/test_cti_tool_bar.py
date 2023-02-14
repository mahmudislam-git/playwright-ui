from playwright.sync_api import Page
from pages.cti_toolbar_pages.cti_login_page import CtiLoginPage
from pages.cti_toolbar_pages.cti_toolbar_page import CtiToolbarPage

def test_cti_toolbar_resource_usage(page: Page, cit_login_page: CtiLoginPage, citi_toolbar_page: CtiToolbarPage) -> None:

    cit_login_page.login_into_application()
    citi_toolbar_page.access_cti_toolbar()

