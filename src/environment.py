from playwright.sync_api import sync_playwright


def before_all(context):
    print("Start Test Suite")
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.chromium
    context.browser = context.browser_type.launch(headless=False)


def before_scenario(context, scenario):
    print("Start scenario: " + str(scenario))
    context.page = context.browser.new_page()
    context.page.set_default_timeout(2000)
    context.base_url = "https://tap-vt25-testverktyg.github.io/exam--reading-list/"


def after_scenario(context, scenario):
    print("End scenario: " + str(scenario))
    if context.page:
        context.page.close()


def after_all(context):
    print("End Test Suite")
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()
