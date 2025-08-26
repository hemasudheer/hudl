from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from dotenv import load_dotenv
import os


locators = {
    "email": (By.XPATH, "//input[@id='username']"),
    "password": (By.XPATH, "//input[@id='password']"),
    "continue_button": (By.XPATH, "//button[text()='Continue']"),
    "dashboard_profile": (By.XPATH, "//div[@class='hui-globaluseritem__avatar']"),
    "incorrect_creds_password": (By.XPATH, "//span[@id='error-element-password']"),
    "incorrect_creds_email": (By.XPATH, "//div[@id='error-cs-email-required']"),
    "incorrect_creds_email_invalid": (By.XPATH, "//div[@id='error-cs-email-invalid']")

}
load_dotenv()


class LoginPage(BasePage):
    email = os.getenv("HUDL_EMAIL")
    password = os.getenv("HUDL_PASSWORD")
    incorrect_password = os.getenv("HUDL_INCORRECT_PASSWORD")

    def login(self, email, password):
        self.type(locators["email"], email)
        self.click(locators["continue_button"])
        self.type(locators["password"], password)
        self.click(locators["continue_button"])
        return self.is_visible(locators["dashboard_profile"])

    def try_login_with_invalid_username(self, email):
        self.type(locators["email"], email)
        self.click(locators["continue_button"])

    def login_with_out_filling(self):
        self.click(locators["continue_button"])
        return self.is_visible(locators["dashboard_profile"])

    def get_password_error_message(self):
        return self.find(locators["incorrect_creds_password"]).text

    def get_username_error_message(self):
        return self.find(locators["incorrect_creds_email"]).text

    def get_username_invalid_error_message(self):
        return self.find(locators["incorrect_creds_email_invalid"]).text
