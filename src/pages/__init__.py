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
        return self

    def scroll_down(self, pixels=100):
        self.browser.actions.scroll_by_amount(-pixels).perform()
        return self

    def switch_to_frame(self, frame_element):
        self.browser.driver.switch_to.frame(frame_element)
        return self

    def switch_to_default(self):
        self.browser.driver.switch_to.default_content()
        return self

    def switch_to_alert(self):
        alert = self.browser.driver.switch_to.alert
        alert.send_keys()
        return self

    def sleep(self, seconds):
        self.browser.driver.implicitly_wait(seconds)
