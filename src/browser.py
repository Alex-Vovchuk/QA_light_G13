from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from config import BASE_URL, BASE_TIMEOUT, BASE_BROWSER


class Browser:
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = None
    actions = None

    @classmethod
    def __init__(cls, browser_name=BASE_BROWSER, headless=False):
        if not cls.driver:
            cls.browser_name = browser_name
            cls.headless = headless
            if headless:
                cls.options.add_argument("--headless")
            if cls.browser_name == 'chrome':
                cls.driver = webdriver.Chrome(options=cls.options)
            elif cls.browser_name == 'firefox':
                cls.driver = webdriver.Firefox(options=cls.options)
            if cls.driver:
                cls.actions = ActionChains(cls.driver)

    def go_to_main_page(self):
        if self.driver.current_url != BASE_URL:
            self.driver.get(BASE_URL)

    def get_element(self, locator, by_=By.XPATH):
        return self.driver.find_element(by_, locator)

    def scroll_to_element(self, locator):
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0, arguments[1]);", element, 100)

    def click(self, locator):
        element = self.get_element(locator)
        self.scroll_to_element(locator)
        self.wait_for_clickable(locator)
        element.click()

    def wait_for_clickable(self, locator, by_=By.XPATH, timeout=BASE_TIMEOUT):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.element_to_be_clickable((by_,  locator)))

    def wait_for_visible(self, locator, by_=By.XPATH, timeout=BASE_TIMEOUT):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located((by_,  locator)))

    def wait_for_present(self, locator, by_=By.XPATH, timeout=BASE_TIMEOUT):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((by_,  locator)))

    def refresh(self):
        self.driver.refresh()

    def go_back(self):
        self.driver.back()

    def get_all_windows(self):
        return self.driver.window_handles

    def switch_to_tab(self, tab_id):
        self.driver.switch_to.window(tab_id)

    def get_cookies(self):
        return self.driver.get_cookies()

    def delete_cookie(self):
        return self.driver.delete_all_cookies()

