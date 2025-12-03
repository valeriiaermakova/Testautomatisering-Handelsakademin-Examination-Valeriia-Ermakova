from behave import when, then
from playwright.sync_api import expect
from pages.catalog_page import CatalogPage


def context_go_to_catalog_page(context):
    web_page = CatalogPage(context.page)
    web_page.navigate()
    context.web_page = web_page


# Scenario:  Titta igenom böcker i Katalog
@when("jag är på Katalog sida")
def go_to_katalog(context):
    context_go_to_catalog_page(context)
    locator = context.web_page.get_test_id_for_catalog()
    expect(locator).to_be_disabled()


@then("lista med alla böcker finns där")
def books_catalog_is_shown(context):
    book_list = context.page.locator("div.catalog > div.book")
    for book in book_list.all():
        expect(book).to_be_visible()
        expect(book).not_to_be_empty()
