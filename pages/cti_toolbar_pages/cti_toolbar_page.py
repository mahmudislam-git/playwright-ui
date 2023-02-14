from playwright.sync_api import Page
class CtiToolbarPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.cti_tool_bar = page.get_by_role("menuitem", name="CTI Toolbar")

    def access_cti_toolbar(self) -> None:
        self.cti_tool_bar.click()
        self.cti_tool_bar.click()
        self.cti_tool_bar.click()
