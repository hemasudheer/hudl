from selenium.webdriver.common.by import By

from pages.base_page import BasePage

locators = {
    "login_button": (By.XPATH, "//a[normalize-space()='Log in']"),
    "hudl_login": (By.XPATH, "//span[normalize-space()='Hudl']"),
    "login_screen": (By.XPATH, "//h1[text()='Log In']")
}


class LandingPage(BasePage):
    URL = "https://www.hudl.com"

    def load_login_page(self):
        self.open(self.URL)
        self.click(locators["login_button"])
        self.click(locators["hudl_login"])
        return self.is_visible(locators["login_screen"])