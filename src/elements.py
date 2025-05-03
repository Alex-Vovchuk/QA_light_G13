from src.browser import Browser


class Element(object):

    def __init__(self, locator):
        self.locator = locator
        self.browser = Browser()

    def set_value(self, value):
        elem = self.browser.get_element(self.locator)
        self.browser.wait_for_clickable(self.locator)
        elem.send_keys(value)
        return self

    def click_element(self):
        self.browser.click(self.locator)

    def is_visible(self):
        return self.browser.get_element(self.locator).is_displayed()


