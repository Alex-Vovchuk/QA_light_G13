import os

from PIL import Image

from src.browser import Browser


class TestFrames:

    def test_get_text_from_frame(self, frames_page):
        frames_page.open()
        frames_page.first_sample_text.click_element()

        frames_page.switch_to_first_frame()
        answer = frames_page.first_sample_text.get_text()
        frames_page.switch_to_default()

        assert 'expanded' in frames_page.first_sample_text.get_attribute('class')

    def test_get_new_tab(self, browser_windows_page):
        browser_windows_page.open()
        browser_windows_page.new_tab_button.click_element()
        all_tabs = browser_windows_page.browser.get_all_windows()
        browser_windows_page.browser.switch_to_tab(all_tabs[-1])
        browser_windows_page.browser.switch_to_tab(all_tabs[0])

    def test_get_attribute(self, forms_page):
        forms_page.open()
        forms_page.picture_input.upload_file(generate_image())

    # def test_example(self, forms_page):
    #     forms_page.open()
    #     forms_page.state_select.click_element()
    #     forms_page.ncr_option.click_element()


def generate_image():
    image = Image.new('RGB', (100, 100), color='red')
    image_path = os.getcwd() + "test_image.png"
    image.save(image_path)
    return image_path

