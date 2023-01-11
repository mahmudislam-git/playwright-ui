from playwright.sync_api import Page
from helper.utils import get_current_date_time


class CreateNewBatch:
    def __init__(self, page: Page) -> None:
        self.page = page
        # self.job_list_box = page.locator("#joblist")
        self.job_list_box = "select#joblist"
        self.name_input = page.locator("#name")
        self.description_input = page.locator("#description")
        self.priority = page.locator("#priority")
        # self.status_list_box = page.locator("#status_list_box")
        self.status_list_box = "#status_list_box"
        self.job_description_input = page.locator("#job_description")
        self.job_create_button = page.locator("#createbutton")

    def create_new_batch(self, job_item: str, job_name: str, desc: str, priority: str, status: str, job_desc: str):
        self.page.select_option(self.job_list_box, label=job_item)
        job_name = job_name + get_current_date_time()
        self.name_input.fill(job_name)
        self.description_input.fill(desc)
        self.priority.fill(priority)
        self.page.select_option(self.status_list_box, label=status)
        self.job_description_input.fill(job_desc)
        self.job_create_button.click()
