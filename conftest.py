import pytest

from src.browser import Browser
from src.pages.alert_frames_windows.browser_windows_page import BrowserWindowsPage
from src.pages.alert_frames_windows.frames_page import FramesPage
from src.pages.elements_pages.text_box_page import TextBoxPage
from src.pages.forms_page import FormsPage


@pytest.fixture(scope="session")
def browser():
    return Browser()


@pytest.fixture(scope="session", autouse=True)
def close_browser(browser):
    yield
    browser.driver.quit()


@pytest.fixture(scope="class")
def text_box_page():
    return TextBoxPage()


@pytest.fixture(scope="class")
def frames_page():
    return FramesPage()


@pytest.fixture(scope="class")
def browser_windows_page():
    return BrowserWindowsPage()


@pytest.fixture(scope="class")
def forms_page():
    return FormsPage()
