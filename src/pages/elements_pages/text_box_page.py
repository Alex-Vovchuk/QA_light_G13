from src.elements import Element
from src.pages import Page


class TextBoxPage(Page):
    page_url = '/text-box'

    full_name_input = Element('//*[@id="userName"]')
    user_email_input = Element('//*[@id="userEmail"]')
    current_address_input = Element('//*[@id="currentAddress"]')
    permanent_address_input = Element('//*[@id="permanentAddress"]')

    submit_button = Element('//*[@id="submit"]')

    success_name = Element('//*[@id="name"]')
    success_email = Element('//*[@id="email"]')
    success_current_address = Element('//p[@id="currentAddress"]')
    success_permanent_address = Element('//p[@id="permanentAddress"]')
