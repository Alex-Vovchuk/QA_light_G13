from src.pages import Page


class TextBoxPage(Page):
    page_url = '/text-box'

    full_name_field = '//*[@id="userName"]'
    submit_button = '//*[@id="submit"]'
