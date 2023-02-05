import time
import allure
from Web.Data.data import *
from Web.PageObject.page_object import PageObject


class Test_ContactUs(PageObject, Colors, Inputs):
    @allure.description("Check the page title is correct")
    def test_contactus_page_title(self):
        self.open()
        self._click(self.contact_link)
        time.sleep(2)
        assert self.read_the_text(self.contact_page_title) == "New message"

    @allure.description("Check that comment submission works using all valid data.")
    def test_with_all_valid_data(self):
        self.open()
        self._click(self.contact_link)
        self._entry(self.email_path, self.email)
        self._entry(self.comment_name, self.name)
        self._entry(self.message_path,self.comment)
        self._click(self.send_message_button)
        time.sleep(2)
        assert self.read_alert() == "Thanks for the message!!"

    @allure.description("Check that comment submission works using all invalid data.")
    def test_with_all_invalid_data(self):
        self.open()
        self._click(self.contact_link)
        self._entry(self.email_path, self.invalid_email)
        self._entry(self.comment_name, self.invalid_name)
        self._entry(self.message_path,self.invalid_comment)
        self._click(self.send_message_button)
        time.sleep(2)
        assert self.read_alert() == "You entered invalid data"

    @allure.description("Check that comment submission does’t work without entering any data.")
    def test_without_data(self):
        self.open()
        self._click(self.contact_link)
        self._click(self.send_message_button)
        time.sleep(2)
        assert self.read_alert() == "Please fill out the fields"

    @allure.description("Check that comment submission works using invalid email.")
    def test_with_invalid_email(self):
        self.open()
        self._click(self.contact_link)
        self._entry(self.email_path, self.invalid_email)
        self._entry(self.comment_name, self.name)
        self._entry(self.message_path,self.comment)
        self._click(self.send_message_button)
        time.sleep(2)
        assert self.read_alert() == "Please use valid email"

    @allure.description("Check that comment submission works by entering the correct name and email but without "
                        "entering a comment.")
    def test_with_no_comment(self):
        self.open()
        self._click(self.contact_link)
        self._entry(self.email_path, self.email)
        self._entry(self.comment_name, self.name)
        self._click(self.send_message_button)
        time.sleep(2)
        assert self.read_alert() == "Please fill out the comment field"

    @allure.description("Check that comment submission works by entering comment but without entering name and email.")
    def test_without_name_and_email(self):
        self.open()
        self._click(self.contact_link)
        self._entry(self.message_path,self.comment)
        self._click(self.send_message_button)
        time.sleep(2)
        assert self.read_alert() == "Please enter your email"

    @allure.description("Check if the close button works")
    def test_contact_close_button(self):
        self.open()
        self._click(self.contact_link)
        self._click(self.contact_close_button)
        time.sleep(2)
        assert self.read_the_text(self.brand_name) == " PRODUCT STORE"

    @allure.description("Check that comment submission works without name.")
    def test_without_comment_name(self):
        self.open()
        self._click(self.contact_link)
        self._entry(self.email_path, self.email)
        self._entry(self.message_path, self.comment)
        self._click(self.send_message_button)
        time.sleep(2)
        assert self.read_alert() == "Please fill out comment name field"


