import base_url


class AddNewBookPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        base_url.get_to_base_url(self.page)
        self.page.get_by_test_id("add-book").click()

    def get_title_input(self):
        return self.page.get_by_test_id("add-input-title")

    def get_author_input(self):
        return self.page.get_by_test_id("add-input-author")

    def get_submit_button(self):
        return self.page.get_by_test_id("add-submit")

    def set_title(self, title):
        self.get_title_input().fill(title)

    def set_author(self, author):
        self.get_author_input().fill(author)

    def press_button_to_submit(self):
        self.get_submit_button().click()
