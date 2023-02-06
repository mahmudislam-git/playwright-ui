import pytest
from playwright.sync_api import Page

from helper.cpu_memory_monitor import start_monitor
from monitoring.monitoring_thread import SystemResourceMonitoring
from pages.create_new_batch import CreateNewBatch
from pages.home import HomePage
from pages.login import LoginPage
from pages.parabank.para_login_page import ParaLoginPage


# def test_create_new_batch(page: Page, login_page: LoginPage,
#                           home_page: HomePage, create_new_batch_page: CreateNewBatch) -> None:
#
#     login_page.load()
#     login_page.login()
#     home_page.click_create_new_batch()
#     create_new_batch_page.create_new_batch("NYSOH_INT_RETURNED_MAIL", "Automated Testing", " 4")
# @pytest.fixture(scope='function')
# def setup_monitor():
#     start_monitor()
def test_monitor_cpu_memory(page: Page, para_login_page: ParaLoginPage) -> None:
    #setup_monitor()

    monitoring = SystemResourceMonitoring()
    monitoring.start()
    monitoring.join()
    pytest.main()
    para_login_page.load_url()
    para_login_page.para_login("test", "test@123")
