import base_url


class CatalogPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        base_url.get_to_base_url(self.page)

    def click_on_favorite_icon(self, bookTestId):
        self.page.get_by_test_id(bookTestId).click()

    def get_book_by_test_id(self, bookTestId):
        return self.page.get_by_test_id(bookTestId)
