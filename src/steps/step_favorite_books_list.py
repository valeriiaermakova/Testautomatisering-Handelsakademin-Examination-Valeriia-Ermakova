from behave import given, when, then
from playwright.sync_api import expect
from pages.catalog_page import CatalogPage


def context_go_to_catalog_page(context):
    web_page = CatalogPage(context.page)
    web_page.navigate()
    context.web_page = web_page


@when("jag tryck på en favorit ikon nära en marklös bok {book1}")
def mark_book(context, book1):
    context_go_to_catalog_page(context)
    locator = context.web_page.get_book_by_test_id(book1)
    expect(locator).to_be_visible()
    expect(locator).not_to_have_class("selected")
    context.web_page.click_on_favorite_icon(book1)


@then("bok {book1} blir märkt")
def check_book_is_marked(context, book1):
    locator = context.web_page.get_book_by_test_id(book1)
    expect(locator).to_be_visible()
    expect(locator).to_contain_class("selected")


@then("jag tryck på favorit ikon nära andra marklös bok {book2}")
def mark_another_book(context, book2):
    locator = context.web_page.get_book_by_test_id(book2)
    expect(locator).not_to_have_class("selected")
    context.web_page.click_on_favorite_icon(book2)


@then("tidigare boken {book1} stannar som märkt")
def previous_book_is_marked(context, book1):
    check_book_is_marked(context, book1)


@then("andra bok {book2} blir märkt")
def another_book_is_marked(context, book2):
    check_book_is_marked(context, book2)


@when("jag tryck på favorit ikon nära en märkt bok")
def unmark_book(context):
    context_go_to_catalog_page(context)
    locator = context.web_page.get_book_by_test_id(
        "star-Hur man tappar bort sin TV-fjärr 10 gånger om dagen"
    )
    context.web_page.click_on_favorite_icon(
        "star-Hur man tappar bort sin TV-fjärr 10 gånger om dagen"
    )
    expect(locator).to_contain_class("selected")
    expect(locator).to_be_visible()
    context.web_page.click_on_favorite_icon(
        "star-Hur man tappar bort sin TV-fjärr 10 gånger om dagen"
    )


@then("bok blir märktlös")
def book_is_unmarked(context):
    locator = context.web_page.get_book_by_test_id(
        "star-Hur man tappar bort sin TV-fjärr 10 gånger om dagen"
    )
    expect(locator).not_to_have_class("selected")
    expect(locator).to_be_visible()
