class TestTextBox:

    def test_fill_in_form_valid_data(self, text_box_page):
        text_box_page.open()
        text_box_page.browser.wait_for_clickable(text_box_page.full_name_field)
        text_box_page.browser.get_element(text_box_page.full_name_field).send_keys('First Name')
        text_box_page.browser.click(text_box_page.submit_button)
