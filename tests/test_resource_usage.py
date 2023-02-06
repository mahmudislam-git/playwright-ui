
from playwright.sync_api import Page

from pages.callrecords_page import CallRecordsPage
from pages.login_page import LoginPage


def test_monitor_cpu_memory(page: Page, login_page: LoginPage,call_records_page: CallRecordsPage) -> None:

    login_page.launch_application()
    call_records_page.access_call_records()
    call_records_page.log_out_application()
