import re

from behave import when, then
from playwright.sync_api import expect
from pages.catalog_page import CatalogPage


def context_go_to_catalog_page(context):
    web_page = CatalogPage(context.page)
    web_page.navigate()
    context.web_page = web_page


@when("jag är på Läslistan webbsida")
def go_to_main_page(context):
    context_go_to_catalog_page(context)


@then('jag ser text "Läslistan"')
def header_is_visible(context):
    locator = context.page.locator("div.app > header > h1")
    expect(locator).to_contain_text(re.compile(r"\s*Läslistan\s*"))
    expect(locator).to_be_visible()


@then("jag ser en kontextuell bild")
def image_is_visible(context):
    locator = context.page.locator("div.app > header > div.hero > img")
    expect(locator).to_be_visible()
    expect(locator).to_have_accessible_name("Bokklubb på café")


@when("jag är på Läslista webbsida")
def go_to_main_page2(context):
    context_go_to_catalog_page(context)


@then("jag ser text Läslistan son sidas titel")
def page_title_visible(context):
    expect(context.page).to_have_title(re.compile(r"\s*Läslistan\s*"))
