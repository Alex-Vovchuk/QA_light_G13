from src.elements import Element
from src.pages import Page


class FramesPage(Page):
    page_url = '/frames'

    first_sample_text = Element('//*[@id="sampleHeading"]')
    first_iframe = '//iframe[@id="frame1"]'

    def switch_to_first_frame(self):
        first_frame_element = self.browser.get_element(self.first_iframe)
        self.switch_to_frame(first_frame_element)
