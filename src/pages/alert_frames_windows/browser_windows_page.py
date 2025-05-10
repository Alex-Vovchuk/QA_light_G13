from src.elements import Element
from src.pages import Page


class BrowserWindowsPage(Page):
    page_url = '/browser-windows'

    new_tab_button = Element('//button[@id="tabButton"]')