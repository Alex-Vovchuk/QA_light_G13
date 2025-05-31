import inspect

import allure
import pytest

from src.browser import Browser
from src.pages.alert_frames_windows.browser_windows_page import BrowserWindowsPage
from src.pages.alert_frames_windows.frames_page import FramesPage
from src.pages.elements_pages.text_box_page import TextBoxPage
from src.pages.forms_page import FormsPage
from src.pages.widgets.date_picker_page import DatePickerPage


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


@pytest.fixture(scope="class")
def date_picker_page():
    return DatePickerPage()


@pytest.fixture(autouse=True, scope='function')
def report_failure(browser, close_browser, request):
    yield
    if is_test_failed():
        my_png = browser.driver.get_screenshot_as_png()
        allure.attach(my_png, "file_name", attachment_type=allure.attachment_type.PNG)
        failed = getattr(request.node, "rep_call", None)
        if failed and failed.failed:
            my_png = browser.driver.get_screenshot_as_png()
            allure.attach(my_png, "file_name", attachment_type=allure.attachment_type.PNG)


def is_test_failed():
    return [fi.frame.f_locals['reports'][-1] for fi in inspect.stack() if 'reports' in fi.frame.f_locals][0].failed


