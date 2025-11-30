url = "https://tap-vt25-testverktyg.github.io/exam--reading-list/"


def get_to_base_url(page):
    page.goto(url, timeout=5000)
