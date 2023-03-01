from playwright.sync_api import Playwright, Page, Browser, BrowserContext


def test_cti(playwright: Playwright):
    browser_type = playwright.chromium
    browser = browser_type.launch(headless=False)
    context = browser.new_context()

    with context:
        page = context.new_page()
        client = page.context.new_cdp_session(page)
        client.send('Performance.enable')
        # client.send('Profiler.enable')
        page.goto("<enter your url here>")
        page.get_by_role("textbox", name="User ID").click()
        page.get_by_role("textbox", name="User ID").fill("<enter user id>")
        page.get_by_label("Password").click()
        page.get_by_label("Password").fill("<enter password>")
        page.get_by_role("link", name="Login").click()

        with page.expect_popup() as page1_info:
            page.get_by_role("menuitem", name="CTI Toolbar").click()
        page1 = page1_info.value
        page1.close()

        page.frame_locator("iframe").get_by_role("heading", name="Available").get_by_text("Available").click()
        page.frame_locator("iframe").get_by_role("link", name="On Queue").click()

        # Customer call via twilio
        for x in range(10):
            ## Add here step to call twilio
            if page.frame_locator("iframe").locator("gef-pickup-control").get_by_role("button").is_enabled():
                page.frame_locator("iframe").locator("gef-pickup-control").get_by_role("button").click()
            ## Check twilio call is in-progress and wait

        page.locator("#s_1_1_78_0_icon").click()
        page.locator("#ui-id-448").click()
        page.locator("#s_1_1_80_0_icon").click()
        page.locator("#ui-id-540").click()
        page.locator("#s_1_1_12_0_icon").click()
        page.locator("#ui-id-652").click()
        page.get_by_role("button", name="Service Request:<b>GO</b>").click()
        page.get_by_role("button", name="Text Referral").click()
        page.frame_locator("iframe >> nth=1").locator("gef-disconnect-control").get_by_role("button").click()
        page.get_by_role("button", name="OK").click()
        page.get_by_role("button", name="Service Request:Call Wrap Up").click()
        page.locator("#ui-id-2098").click()
        page.get_by_role("cell", name="No: How else may I assist you today?Select Cancel").locator("div").click()
        page.get_by_role("button", name="Hide").click()
        page.get_by_role("button", name="Call Wrap Up:OK").click()
        page.get_by_role("button", name="Show").click()

        # ---------------------

        performanceMetrics = client.send('Performance.getMetrics')
        print("print performance metrics from chrome developer tool")
        print(performanceMetrics)
        metrics = page.evaluate("window.performance.timing")
        print('metrics', metrics)
        cpu_usage = (metrics['domInteractive'] - metrics['navigationStart']) / 1000
        print('cpu usage', cpu_usage)

        # Retrieve Memory Usage
        res = None
        for sub in performanceMetrics['metrics']:
            if sub['name'] == "JSHeapUsedSize":
                res = sub
        print('memory_usage', res['value'])

    # Close the browser
    context.close()
    browser.close()
