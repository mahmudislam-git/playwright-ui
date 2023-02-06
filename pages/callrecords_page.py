from playwright.sync_api import Page
class CallRecordsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.call_records_link = page.get_by_role("link", name="@ Call Records")
        self.documents_link = page.get_by_role("link", name="@ Documents")
        self.referral_contacts_link = page.get_by_role("link", name="@ Referral Contacts")
        self.settings_menuitem = page.get_by_role("menuitem", name="Settings")
        self.logout_button = page.get_by_role("button", name="Logout")

    def access_call_records (self) -> None:

        self.call_records_link.click()
        self.documents_link.click()
        self.referral_contacts_link.click()
        self.settings_menuitem.click()

    def log_out_application(self) -> None:
        self.logout_button()