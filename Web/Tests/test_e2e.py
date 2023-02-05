import time
from Web.Data.data import *
from Web.PageObject.page_object import PageObject


class Test_Home(PageObject, Colors, Inputs):

    def test_end_to_end(self):
        self.open()
        self._click(self.signup_link)
        self._entry(self.signup_name, "Alehegn")
        self._entry(self.signup_pass, "m01236548")
        self._click(self.signup_button)
        time.sleep(3)
        assert self.read_alert() == "Sign up successful."
        self.alert_ok()
        self._click(self.login_link)
        self._entry(self.login_name, "Alehegn")
        self._entry(self.login_pass, "m01236548")
        self._click(self.login_button)
        self._is_displayed(self.name_of_user)
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        assert self._is_displayed(self.added_product) == True
        self._click(self.place_order_button)
        self._entry(self.name_path, self.name)
        self._entry(self.country_path, self.country)
        self._entry(self.city_path, self.city)
        self._entry(self.card_path, self.card_num)
        self._entry(self.month_path, self.month)
        self._entry(self.year_path, self.year)
        self._click(self.purchase_button)
        time.sleep(3)
        assert self.read_the_text(self.order_successfully) == "Thank you for your purchase!"
        self._click(self.confirm)
        self._click(self.contact_link)
        self._entry(self.email_path, self.email)
        self._entry(self.comment_name, self.name)
        self._entry(self.message_path, self.comment)
        self._click(self.send_message_button)
        time.sleep(2)
        assert self.read_alert() == "Thanks for the message!!"





