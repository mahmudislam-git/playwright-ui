
from playwright.sync_api import Playwright, Page, Browser, BrowserContext


def test_browser_memory_cpu_usage(playwright: Playwright):
    browser_type = playwright.chromium
    browser = browser_type.launch()
    context = browser.new_context()

    with context:
        page = context.new_page()
        client = page.context.new_cdp_session(page)
        client.send('Performance.enable')
        #client.send('Profiler.enable')
        page.goto("https://www.saucedemo.com/")
        page.locator("[data-test=\"username\"]").click()
        page.locator("[data-test=\"username\"]").fill("standar_user")
        page.locator("[data-test=\"password\"]").click()
        page.locator("[data-test=\"password\"]").fill("secret_sauce")
        page.locator("[data-test=\"login-button\"]").click()
        page.locator("[data-test=\"username\"]").click()
        page.locator("[data-test=\"username\"]").fill("standar_user")
        page.locator("[data-test=\"username\"]").click()
        page.locator("[data-test=\"username\"]").press("ArrowLeft")
        page.locator("[data-test=\"username\"]").press("ArrowLeft")
        page.locator("[data-test=\"username\"]").press("ArrowLeft")
        page.locator("[data-test=\"username\"]").press("ArrowLeft")
        page.locator("[data-test=\"username\"]").press("ArrowLeft")
        page.locator("[data-test=\"username\"]").press("ArrowLeft")
        page.locator("[data-test=\"username\"]").press("ArrowRight")
        page.locator("[data-test=\"username\"]").fill("standard_user")
        page.locator("[data-test=\"login-button\"]").click()
        page.locator("[data-test=\"product_sort_container\"]").select_option("za")
        page.locator("[data-test=\"product_sort_container\"]").select_option("lohi")
        page.locator("[data-test=\"product_sort_container\"]").select_option("hilo")
        page.locator("#shopping_cart_container a").click()
        page.locator("[data-test=\"continue-shopping\"]").click()
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
    browser.close()

