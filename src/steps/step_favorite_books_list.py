from behave import when, then
from playwright.sync_api import expect
from pages.catalog_page import CatalogPage
from pages.my_books_page import MyBooksPage


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


@when("jag tryck på favorit ikon nära en märkt bok {bookToUnmark}")
def unmark_book(context, bookToUnmark):
    context_go_to_catalog_page(context)
    locator = context.web_page.get_book_by_test_id(bookToUnmark)
    context.web_page.click_on_favorite_icon(bookToUnmark)
    expect(locator).to_contain_class("selected")
    expect(locator).to_be_visible()
    context.web_page.click_on_favorite_icon(bookToUnmark)


@then("bok blir märktlös {bookToUnmark}")
def book_is_unmarked(context, bookToUnmark):
    locator = context.web_page.get_book_by_test_id(bookToUnmark)
    expect(locator).not_to_have_class("selected")
    expect(locator).to_be_visible()


@when("jag tryck på en favorit ikon nära en märkt bok {bookToReMark}")
def unmark_book2(context, bookToReMark):
    context_go_to_catalog_page(context)
    context.web_page.click_on_favorite_icon(bookToReMark)
    context.web_page.click_on_favorite_icon(bookToReMark)


@then("boken blir märktlös {bookToReMark}")
def book_is_unmarked_2(context, bookToReMark):
    locator = context.web_page.get_book_by_test_id(bookToReMark)
    expect(locator).not_to_have_class("selected")


@then("jag tryck på favorit ikon nära avmarkerade boken {bookToReMark}")
def mark_book_again_after_unmarking(context, bookToReMark):
    context.web_page.click_on_favorite_icon(bookToReMark)


@then("boken blir märkt {bookToReMark}")
def book_is_marked_repeatedly(context, bookToReMark):
    check_book_is_marked(context, bookToReMark)


@when('jag kollar upp "Mina böcker" sida innan jag lägger till böcker i lista')
def go_to_my_books(context):
    context_go_to_catalog_page(context)
    context.page.get_by_test_id("favorites").click()


@then('jar ser text "När du valt, kommer dina favoritböcker att visas här."')
def check_empty_my_books_list(context):
    my_books_page = MyBooksPage(context.page)
    expect(
        context.page.get_by_text(my_books_page.expected_text_for_empty_list)
    ).to_be_visible()


@when("jag tryck på favorit ikon nära en marklös bok {book}")
def mark_favorite_book(context, book):
    mark_book(context, book)


@when('jag går till "Mina böcker"')
def go_to_my_books_list(context):
    context.page.get_by_test_id("favorites").click()


@then("märkta boken {book} är i mina böcker lista")
def check_marked_book_in_my_list(context, book):
    frame = context.page.get_by_test_id("book-list")
    books = frame.all_text_contents()
    book_found = False
    for element in books:
        if element in book:
            book_found = True
            break
    assert book_found
