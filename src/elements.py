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
        return self

    def is_visible(self):
        return self.browser.get_element(self.locator).is_displayed()

    def get_text(self):
        self.browser.wait_for_visible(self.locator)
        return self.browser.get_element(self.locator).text

    def get_css_property(self, property_name):
        self.browser.wait_for_present(self.locator)
        element = self.browser.get_element(self.locator)
        return element.value_of_css_property(property_name)

    def get_attribute(self, element_attribute):
        self.browser.wait_for_present(self.locator)
        element = self.browser.get_element(self.locator)
        return element.get_attribute(element_attribute)

    def upload_file(self, file_path):
        self.browser.wait_for_present(self.locator)
        element = self.browser.get_element(self.locator)
        element.send_keys(file_path)
        return self


class SelectElement(Element):

    def set_value(self, value):
        elem = self.browser.get_element(self.locator)
        self.browser.wait_for_clickable(self.locator)
        # needs to write
        return self
