import re

import base_url


class MyBooksPage:
    def __init__(self, page):
        self.page = page
        self.expected_text_for_empty_list = re.compile(
            r"\s*När du valt, kommer dina favoritböcker att visas här.\s*"
        )

    def navigate(self):
        base_url.get_to_base_url(self.page)
        self.page.get_by_test_id("favorites").click()
