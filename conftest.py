import pytest

from src import Browser
from src.pages.elements_pages.text_box_page import TextBoxPage


@pytest.fixture(scope="session")
def browser():
    return Browser('chrome')


@pytest.fixture(scope="session", autouse=True)
def close_browser(browser):
    yield
    browser.driver.quit()


@pytest.fixture(scope="class")
def text_box_page():
    return TextBoxPage()
