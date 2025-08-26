import pytest
import os
from pages.login_page import LoginPage
from pages.landing_page import LandingPage
from selenium.common.exceptions import TimeoutException


email = os.getenv("HUDL_EMAIL")
password = os.getenv("HUDL_PASSWORD")
incorrect_password = os.getenv("HUDL_INCORRECT_PASSWORD")
incorrect_email = "blahblah"


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_001_login_with_valid_credentials(self):
        landing_page = LandingPage(self.driver)
        login_page = LoginPage(self.driver)
        assert landing_page.load_login_page()
        assert login_page.login(email, password)

    def test_002_login_with_invalid_password(self):
        landing_page = LandingPage(self.driver)
        login_page = LoginPage(self.driver)
        assert landing_page.load_login_page()
        with pytest.raises(TimeoutException):
            assert not login_page.login(email, incorrect_password)
        assert login_page.get_password_error_message() == "Your email or password is incorrect. Try again."

    def test_003_login_with_blank_field(self):
        landing_page = LandingPage(self.driver)
        login_page = LoginPage(self.driver)
        assert landing_page.load_login_page()
        with pytest.raises(TimeoutException):
            assert not login_page.login_with_out_filling()
        assert login_page.get_username_error_message() == "Enter an email address"

    def test_004_login_with_invalid_email(self):
        landing_page = LandingPage(self.driver)
        login_page = LoginPage(self.driver)
        assert landing_page.load_login_page()
        assert not login_page.try_login_with_invalid_username(incorrect_email)
        assert login_page.get_username_invalid_error_message() == "Enter a valid email."

    def test_005_login_with_case_sensitivity_password(self):
        landing_page = LandingPage(self.driver)
        login_page = LoginPage(self.driver)
        assert landing_page.load_login_page()
        with pytest.raises(TimeoutException):
            assert not login_page.login(email, password.lower())
        assert login_page.get_password_error_message() == "Your email or password is incorrect. Try again."

    def test_006_login_with_white_spaces_password(self):
        landing_page = LandingPage(self.driver)
        login_page = LoginPage(self.driver)
        assert landing_page.load_login_page()
        with pytest.raises(TimeoutException):
            assert not login_page.login(email, password + ' ')
        assert login_page.get_password_error_message() == "Your email or password is incorrect. Try again."

# More scenarios can be covered for locked account or password expired account similarly
