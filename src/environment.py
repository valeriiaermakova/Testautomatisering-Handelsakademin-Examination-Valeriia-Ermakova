from playwright.sync_api import sync_playwright


def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.chromium
    context.browser = context.browser_type.launch(headless=False)


def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.page.set_default_timeout(1000)
    context.base_url = "https://tap-vt25-testverktyg.github.io/exam--reading-list/"


def after_scenario(context, scenario):
    if context.page:
        context.page.close()


def after_all(context):
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()
