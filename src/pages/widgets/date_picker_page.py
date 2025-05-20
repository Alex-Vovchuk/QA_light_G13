from src.elements import Element, CalendarElement
from src.pages import Page


class DatePickerPage(Page):
    page_url = '/date-picker'
    select_date_input = CalendarElement('//*[@id="datePickerMonthYearInput"]')

