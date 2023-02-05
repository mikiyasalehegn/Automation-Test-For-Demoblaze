import time
import allure
from Web.Data.data import *
from Web.PageObject.page_object import PageObject


class Test_SignUp(PageObject, Colors, Inputs):

    @allure.description("Check that signup works with existing user data.")
    def test_signup_with_existing_user_data(self):
        self.open()
        self._click(self.signup_link)
        self._entry(self.signup_name, self.name)
        self._entry(self.signup_pass, self.password)
        self._click(self.signup_button)
        assert self.read_alert() == "This user already exist."

    @allure.description("Check that signup works without entering data.")
    def test_signup_without_user_data(self):
        self.open()
        self._click(self.signup_link)
        self._click(self.signup_button)
        time.sleep(3)
        assert self.read_alert() == "Please fill out Username and Password."

    @allure.description("Verify signup with less password")
    def test_less_password(self):
        self.open()
        self._click(self.signup_link)
        self._entry(self.signup_name, self.invalid_name)
        self._entry(self.signup_pass, self.less_pass)
        self._click(self.signup_button)
        time.sleep(3)
        assert self.read_alert() == "The password needs to be more than 4 digits."

    @allure.description("check the if close button works.")
    def test_signup_close_button(self):
        self.open()
        self._click(self.signup_link)
        self._click(self.signup_close_button)
        time.sleep(3)
        assert self.read_the_text(self.brand_name) == "PRODUCT STORE"

    @allure.description("Check the page title")
    def test_signup_page_title(self):
        self.open()
        self._click(self.signup_link)
        time.sleep(3)
        assert self.read_the_text(self.signup_header) == "Sign up"

    @allure.description("")
    def test_signup_with_not_existing_user_data(self):
        self.open()
        self._click(self.signup_link)
        self._entry(self.signup_name, "jfk,")
        self._entry(self.signup_pass, "32145:")
        self._click(self.signup_button)
        self.alert_ok()
        self._click(self.login_link)
        time.sleep(2)
        self._entry(self.login_name, "jfk,")
        self._entry(self.login_pass, "32145:")
        self._click(self.login_button)
        self._is_displayed(self.name_of_user)





