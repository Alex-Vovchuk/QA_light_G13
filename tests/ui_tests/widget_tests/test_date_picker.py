import datetime


class TestDatePicker:

    def test_get_text_from_frame(self, date_picker_page):
        needed_date = '05/13/2025'
        date_picker_page.open()
        date_picker_page.select_date_input.set_value(needed_date)


