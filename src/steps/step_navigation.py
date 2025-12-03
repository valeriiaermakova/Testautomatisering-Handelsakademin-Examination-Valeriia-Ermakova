from behave import when, then
from playwright.sync_api import expect
from pages.catalog_page import CatalogPage
from pages.my_books_page import MyBooksPage
from pages.add_new_book_page import AddNewBookPage


def context_go_to_catalog_page(context):
    web_page = CatalogPage(context.page)
    web_page.navigate()
    context.web_page = web_page


@when("jag öppnar Läslista webbsida")
def go_to_main_page(context):
    context_go_to_catalog_page(context)


@then("jag är på Katalog vy")
def check_catalog_view(context):
    locator = context.web_page.get_test_id_for_catalog()
    expect(locator).to_be_visible()
    expect(locator).to_be_disabled()
    expect(context.page.locator("div.app > main > div.catalog")).to_be_visible()


@when('jag trick på "Lägg till bok"')
def go_to_add_books_page(context):
    context_go_to_catalog_page(context)
    context.page.get_by_test_id("add-book").click()


@then('jag är på "Lägg till bok" vy')
def check_add_book_view(context):
    locator = context.page.get_by_test_id("add-book")
    expect(locator).to_be_visible()
    expect(locator).to_be_disabled()
    expect(context.page.locator("div.app > main > div.form")).to_be_visible()


@when('jag trick på "Mina böcker"')
def go_to_my_books_page(context):
    context_go_to_catalog_page(context)
    context.page.get_by_test_id("favorites").click()


@then('jag är på "Mina böcker" vy')
def check_my_books_view(context):
    locator = context.page.get_by_test_id("favorites")
    expect(locator).to_be_visible()
    expect(locator).to_be_disabled()
    expect(context.page.locator("div.app > main > div.favorites")).to_be_visible()


@when('jag är på "Mina böcker" vy')
def go_to_my_books_page(context):
    context_go_to_catalog_page(context)
    context.page.get_by_test_id("favorites").click()


@when('jag trick på "Katalog"')
def go_to_catalog_from_another_view(context):
    context.page.get_by_test_id("catalog").click()


@then('jag är på "Katalog" vy')
def back_to_catalog_view(context):
    locator = context.web_page.get_test_id_for_catalog()
    expect(locator).to_be_visible()
    expect(locator).to_be_disabled()
    expect(context.page.locator("div.app > main > div.catalog")).to_be_visible()
