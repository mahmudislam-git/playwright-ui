from playwright.sync_api import Page

class CreateNewBatch:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.job_select_button = page.locator("#JobSelect")
        self.job_items = page.locator("#JobSelect_window div")
        self.name_input = page.locator("#name")
        self.description_input = page.locator("#Description")
        self.priority = page.locator("#JobPriority")
        # self.status_list_box = page.locator("#status_list_box")
        # self.status_list_box = "#status_list_box"
        # self.job_description_input = page.locator("#job_description")
        self.job_create_button = page.get_by_role("button", name="Create")

    def create_new_batch(self, job_item: str, desc: str, priority: str):

        self.job_select_button.click()
        self.job_items.filter(has_text=job_item).nth(1).click()

        self.description_input.click()
        self.description_input.fill(desc)

        self.priority.click()
        self.priority.fill(priority)

        self.job_create_button.nth(1).click()

