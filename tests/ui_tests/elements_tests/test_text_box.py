class TestTextBox:

    def test_only_mandatory_fields(self, text_box_page):
        text_box_page.open()
        text_box_page.full_name_input.set_value("First Name")
        text_box_page.user_email_input.set_value("paasdfj@gmasd.com")
        text_box_page.current_address_input.set_value("First Name")
        text_box_page.permanent_address_input.set_value("First Name")
        text_box_page.submit_button.click_element()

        assert text_box_page.success_name.is_visible()
        assert text_box_page.success_email.is_visible()
        assert text_box_page.success_current_address.is_visible()
        assert text_box_page.success_permanent_address.is_visible()
