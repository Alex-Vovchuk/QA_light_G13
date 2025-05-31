from datetime import datetime

import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

submit_button = '//*[@id="submit"]'
picture_input = '//*[@id="uploadPicture"]'
# state_select = '//*[@id="state"]'


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


def test_practice_form_playwright(page):
    needed_date = '02/13/2024'
    page.goto('https://demoqa.com/date-picker')
    # page.locator('xpath=//*[@id="firstName"]').fill('Martin')
    # page.locator('xpath=//*[@id="lastName"]').fill('Luther')
    # page.locator('xpath=//*[@for="hobbies-checkbox-1"]').check()

    date_obj = datetime.strptime(needed_date, "%m/%d/%Y")
    day = date_obj.day
    page.click('xpath=//*[@id="datePickerMonthYearInput"]')
    month_name = date_obj.strftime("%B")
    year = date_obj.year
    page.locator('xpath=//*[@class="react-datepicker__month-select"]').select_option(month_name)
    page.locator('xpath=//*[@class="react-datepicker__year-select"]').select_option(f'{year}')
    page.click('xpath=//*[contains(@class,"datepicker__day") and not(contains(@class, "outside-month"))'
               ' and not(contains(@class, "name")) and .="%s"]' % day)
    expect(page.locator('xpath=//*[@id="datePickerMonthYearInput"]')).to_have_value(needed_date)

# def wait_for_text(text):
#     for timer in range(30):
#         if page.locator('xpath=//*[@for="hobbies-checkbox-1"]').text_content() == text:
#             break
#         time.sleep(1)
#     else:
#         raise TimeoutError("Timeout waiting for text content")
