from datetime import datetime

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


class CalendarElement(Element):
    date_picker = '//*[@class="react-datepicker"]'
    month_pick_input = '//*[@class="react-datepicker__month-select"]'
    year_pick_input = '//*[@class="react-datepicker__year-select"]'
    needed_day = ('//*[contains(@class,"datepicker__day") and not(contains(@class, "outside-month"))'
                  ' and not(contains(@class, "name")) and .="%s"]')
    needed_month = '//*[@class="react-datepicker__month-select"]//option[text()="%s"]'
    month_picker_list = '//*[@class="react-datepicker__month-select"]'
    year_picker_list = '//*[@class="react-datepicker__year-select"]'
    needed_year = '//*[@class="react-datepicker__year-select"]//option[text()="%s"]'

    def set_value(self, value):
        date_obj = datetime.strptime(value, "%m/%d/%Y")
        day = date_obj.day
        self.browser.click(self.locator)
        self.browser.wait_for_visible(self.date_picker)
        self.set_month(value)
        self.set_year(value)
        self.browser.click(self.needed_day % day)
        self.browser.wait_for_invisible(self.date_picker)

    def set_month(self, date):
        date_obj = datetime.strptime(date, "%m/%d/%Y")
        month_name = date_obj.strftime("%B")
        self.browser.click(self.month_pick_input)
        self.browser.wait_for_visible(self.month_picker_list)
        self.browser.click(self.needed_month % month_name)

    def set_year(self, date):
        date_obj = datetime.strptime(date, "%m/%d/%Y")
        year = date_obj.year
        self.browser.click(self.month_pick_input)
        self.browser.wait_for_visible(self.month_picker_list)
        self.browser.click(self.needed_year % year)
