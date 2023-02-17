from playwright.sync_api import Page
from pages.cti_toolbar_pages.cti_login_page import CtiLoginPage
from pages.cti_toolbar_pages.cti_toolbar_page import CtiToolbarPage

def test_cti_toolbar_resource_usage(page: Page, cti_login_page: CtiLoginPage, cti_tool_bar_page: CtiToolbarPage) -> None:

    cti_login_page.login_into_application()
    cti_tool_bar_page.access_cti_toolbar()

