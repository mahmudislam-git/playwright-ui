import os
import time

from playwright.sync_api import Playwright, Page, Browser, BrowserContext

from utils.twilio.twilio_make_call import CTI


def test_browser_memory_cpu_usage(playwright: Playwright, twilio_make_call: CTI):
    twiml = "https://handler.twilio.com/twiml/EHc80d560fe35c83e0ac79286d3052c7af"
    to_phone_number = os.environ.get('TO_PHONE_NUMBER')

    browser_type = playwright.chromium
    browser = browser_type.launch(headless=False)
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

        # Customer call via twilio
        for x in range(3):
            # Make CTI call using twilio
            call_sid = twilio_make_call.make_the_call(to_phone_number, twiml)
            print("call_sid print "
                  "#", x, call_sid)

            time.sleep(20)
            # END CTI twilio call
            twilio_make_call.end_the_call(call_sid, twiml)
            time.sleep(5)


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

