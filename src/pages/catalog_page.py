import base_url


class CatalogPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        base_url.get_to_base_url()
        self.page.get_by_test_id("catalog").click()
