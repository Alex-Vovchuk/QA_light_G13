from src.browser import Browser
from config import BASE_BROWSER, BASE_URL


class Page(object):
    locator = ''
    page_url = ''
    header_logo = '//a[@href="https://demoqa.com"]'

    def __init__(self):
        self.browser = Browser()

    def open(self):
        self.browser.driver.get(BASE_URL + self.page_url)
        return self

    def scroll_up(self, pixels=100):
        self.browser.actions.scroll_by_amount(pixels).perform()

    def scroll_down(self, pixels=100):
        self.browser.actions.scroll_by_amount(-pixels).perform()

