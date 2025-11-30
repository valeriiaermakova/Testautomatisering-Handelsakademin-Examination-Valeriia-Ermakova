from behave import given, when, then
from playwright.sync_api import expect
from pages.add_new_book_page import AddNewBookPage


def new_page_context(context):
    web_page = AddNewBookPage(context.page)
    web_page.navigate()
    context.web_page = web_page


@when('jag tryck på "Lägg till bok" knappen i navigering menu')
def step_given_start_page(context):
    new_page_context(context)


@then("jar ser tom titel form")
def title_is_empty(context):
    locator = context.web_page.get_title_input()
    expect(locator).to_be_empty()


@then("jag ser tom författare form")
def author_is_empty(context):
    locator = context.web_page.get_author_input()
    expect(locator).to_be_empty()


@then("jag ser gråtonad knappen")
def button_to_add_book_disabled(context):
    locator = context.web_page.get_submit_button()
    expect(locator).to_be_disabled()


@when("jag skriver titel")
def add_value_to_user_field(context):
    new_page_context(context)
    context.web_page.set_title("En man som heter Ove")


@when("jag skriver författare")
def add_value_to_author_field(context):
    context.web_page.set_author("F. Backmann")


@then('"Lägg till ny bok" knappen låser upp')
def button_to_add_book_enabled(context):
    locator = context.web_page.get_submit_button()
    expect(locator).to_be_enabled()


@then('jag tryck på knappen "Lägg till ny bok"')
def press_submit_button(context):
    context.web_page.press_button_to_submit()


@then("Titelfältet är tomt")
def title_reset(context):
    title_is_empty(context)


@then("Författarefältet är tomt")
def author_reset(context):
    author_is_empty(context)


@then('"Lägg till ny bok" knappen är gråtonad')
def button_disabled_after_submit(context):
    button_to_add_book_disabled(context)
