from src.elements import Element, SelectElement
from src.pages import Page


class FormsPage(Page):
    page_url = '/automation-practice-form'

    first_name_input = Element('//*[@id="firstName"]')
    submit_button = Element('//*[@id="submit"]')
    picture_input = Element('//*[@id="uploadPicture"]')
    state_select = SelectElement('//*[@id="state"]')
    ncr_option = Element('//div[contains(text(),"NCR")]')
