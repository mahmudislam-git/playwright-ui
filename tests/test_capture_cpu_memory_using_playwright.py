
import psutil
import pytest
from playwright.sync_api import Playwright, Page, Browser, BrowserContext


# @pytest.fixture(scope="module")
# def playwright():
#     with Playwright() as playwright:
#         yield playwright


def test_browser_memory_cpu_usage(playwright: Playwright):
    browser_type = playwright.chromium
    browser = browser_type.launch()
    context = browser.new_context()

    with context:
        page = context.new_page()
        client = page.context.new_cdp_session(page)
        #client.send('Performance.enable')
        client.send('Profiler.enable')
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
        #context.close()
        #browser.close()
        # Run some actions on the page
        #performanceMetrics = client.send('Performance.getMetrics')
        #print("print performance metrics")
        #print(performanceMetrics)

        profilerData = client.send('Profiler.getBestEffortCoverage')
        print("print performance metrics")
        print(profilerData)
    # Get the browser process ID and create a process object
    # pid = browser.process.pid
    # process = psutil.Process(pid)

    # Get CPU and memory usage of the browser process
    # cpu_percent = process.cpu_percent()
    # memory_info = process.memory_info()
    # memory_mb = memory_info.rss / (1024 * 1024)
    #
    # # Print the CPU and memory usage
    # print(f"Browser CPU usage: {cpu_percent}%")
    # print(f"Browser memory usage: {memory_mb} MB")

    # Close the browser
    browser.close()
