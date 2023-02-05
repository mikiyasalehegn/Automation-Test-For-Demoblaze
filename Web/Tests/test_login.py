import time
import allure
from Web.Data.data import *
from Web.PageObject.page_object import PageObject


class Test_Login(PageObject, Colors, Inputs):

    @allure.description("Check the page title")
    def test_login_page_title(self):
        self.open()
        self._click(self.login_link)
        time.sleep(2)
        assert self.read_the_text(self.login_header) == "Log in"

    @allure.description("Verify login using the correct username and an incorrect password.")
    def test_with_correct_username_password(self):
        self.open()
        self._click(self.login_link)
        self._entry(self.login_name, self.username)
        self._entry(self.login_pass, self.password)
        self._click(self.login_button)
        self._is_displayed(self.name_of_user)

    @allure.description("Verify login with an incorrect username and correct password")
    def test_with_incorrect_username(self):
        self.open()
        self._click(self.login_link)
        self._entry(self.login_name, self.invalid_name)
        self._entry(self.login_pass, self.password)
        self._click(self.login_button)
        assert self.read_alert() == "User does not exist."

    @allure.description("Verify login using the correct username and an incorrect password.")
    def test_correct_username_incorrect_password(self):
        self.open()
        self._click(self.login_link)
        self._entry(self.login_name, self.username)
        self._entry(self.login_pass, self.invalid_pass)
        self._click(self.login_button)
        assert self.read_alert() == 'Wrong password.'

    @allure.description("Verify login using the wrong username and password.")
    def test_incorrect_username_and_password(self):
        self.open()
        self._click(self.login_link)
        self._entry(self.login_name, self.invalid_name)
        self._entry(self.login_pass, self.invalid_pass)
        self._click(self.login_button)
        assert self.read_alert() == 'User does not exist.'

    @allure.description("Check login without inserting username and password.")
    def test_without_user_data(self):
        self.open()
        self._click(self.login_link)
        self._click(self.login_button)
        time.sleep(3)
        assert self.read_alert() == 'Please fill out Username and Password.'

    @allure.description("Check if the password is written with the ‘*’ symbol.")
    def test_password_is_not_revealed(self):
        self.open()
        self._click(self.login_link)
        self._entry(self.login_name, self.invalid_name)
        self._entry(self.login_pass, self.invalid_pass)
        time.sleep(3)
        assert self.password_not_revealed(self.login_pass) == True

    @allure.description("Verify close button is working")
    def test_login_close_button(self):
        self.open()
        self._click(self.login_link)
        self._click(self.login_close_button)
        time.sleep(3)
        assert self.read_the_text(self.brand_name) == " PRODUCT STORE"

    @allure.description("Verify logout link works properly.")
    def test_logout(self):
        self.open()
        self._click(self.login_link)
        self._entry(self.login_name, self.username)
        self._entry(self.login_pass, self.password)
        self._click(self.login_button)
        self._is_displayed(self.name_of_user)
        self._click(self.logout_link)
        time.sleep(2)
        assert self._is_displayed(self.login_link) == True




