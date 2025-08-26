from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def wait_for(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        try:
            wait = WebDriverWait(self.driver, 5, poll_frequency=2)
            element = wait.until(EC.visibility_of_element_located(locator))
            element.click()
        except (ElementNotVisibleException, TimeoutException):
            print(f"Element {locator} not visible after 10 seconds")

    def type(self, locator, text):
        elem = self.wait_for(locator)
        elem.clear()
        elem.send_keys(text)

    def is_visible(self, locator, wait_time=5):
        try:
            wait = WebDriverWait(self.driver, wait_time, poll_frequency=2)
            return wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except (ElementNotVisibleException, TimeoutException):
            raise
