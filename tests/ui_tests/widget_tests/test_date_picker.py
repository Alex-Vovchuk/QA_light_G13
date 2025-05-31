import datetime
import allure


class TestDatePicker:

    def test_get_text_from_frame(self, browser, date_picker_page):
        with allure.step("Setting date"):
            needed_date = '05/13/2025'
            failed_date = '05/15/2025'
            date_picker_page.open()
            date_picker_page.select_date_input.set_value(needed_date)
        with allure.step("Assert date from input"):
            assert date_picker_page.select_date_input.get_attribute('value') == failed_date



