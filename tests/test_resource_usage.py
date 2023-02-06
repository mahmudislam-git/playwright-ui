
from playwright.sync_api import Page
from pages.parabank.para_login_page import ParaLoginPage
def test_monitor_cpu_memory(page: Page, para_login_page: ParaLoginPage) -> None:

    para_login_page.load_url()
    para_login_page.para_login("test", "test@123")
