from behave import given, when, then
from playwright.sync_api import expect
from pages.add_new_book_page import AddNewBookPage


def context_go_to_add_book_page(context):
    web_page = AddNewBookPage(context.page)
    web_page.navigate()
    context.web_page = web_page


@when('jag tryck på "Lägg till bok" knappen i navigering menu')
def step_given_start_page(context):
    context_go_to_add_book_page(context)


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
def add_value_to_title_field(context):
    context_go_to_add_book_page(context)
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


@when("jag har lagt en ny bok")
def add_new_book(context):
    # raise ValueError("hug!")
    context_go_to_add_book_page(context)
    context.web_page.set_title("En man som heter Ove")
    context.web_page.set_author("F. Backmann")
    context.web_page.press_button_to_submit()


@when("jag går till Katalog sidan")
def go_to_catalog(context):
    context.page.get_by_test_id("catalog").click()


@then("jag kan se boken som jag har lagt till")
def find_added_book(context):
    frame = context.page.locator("div.catalog > div.book")
    books = frame.all_text_contents()
    expect_s = '"{title}", {author}'.format(
        title="En man som heter Ove", author="F. Backmann"
    )
    book_found = False
    for book in books:
        if expect_s in book:
            book_found = True
            break
    assert book_found


@when("jag läggar eller skippar titel: {title}")
def add_title(context, title):
    context_go_to_add_book_page(context)
    title = title.strip('"')
    context.web_page.set_title(title)


@when("jag läggar eller skippar författare: {author}")
def add_author(context, author):
    author = author.strip('"')
    context.web_page.set_author(author)


@then('"Lägg till ny bok" knappen är inaktiverad')
def submit_button_is_locked(context):
    button_to_add_book_disabled(context)
