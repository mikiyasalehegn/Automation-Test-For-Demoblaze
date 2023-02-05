import time
import allure
from Web.Data.data import *
from Web.PageObject.page_object import PageObject


class Test_Order(PageObject, Colors, Inputs):

    @allure.description("Verify the page title is Place order.")
    def test_the_page_title(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        self._click(self.place_order_button)
        time.sleep(2)
        assert self.read_the_text(self.order_page_title) == "Place order"

    @allure.description("Check the place order using all valid data.")
    def test_place_order_with_correct_data(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
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

    @allure.description("Verify the place order using all invalid data.")
    def test_place_order_with_invalid_data(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        self._click(self.place_order_button)
        self._entry(self.name_path, self.invalid_name)
        self._entry(self.country_path, self.invalid_country)
        self._entry(self.city_path, self.invalid_city)
        self._entry(self.card_path, self.invalid_card)
        self._entry(self.month_path, self.invalid_month)
        self._entry(self.year_path, self.invali_year)
        self._click(self.purchase_button)
        time.sleep(3)
        assert self.read_the_text(self.order_successfully) == "You entered invalid data"

    @allure.description("Verify the place order using correct data and an invalid username.")
    def test_place_order_incorrect_name_valid_data(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        self._click(self.place_order_button)
        self._entry(self.name_path, self.invalid_name)
        self._entry(self.country_path, self.country)
        self._entry(self.city_path, self.city)
        self._entry(self.card_path, self.card_num)
        self._entry(self.month_path, self.month)
        self._entry(self.year_path, self.year)
        self._click(self.purchase_button)
        time.sleep(3)
        assert self.read_the_text(self.order_successfully) == "The name you entered doesn't match to other data"

    @allure.description("Verify place order without data")
    def test_place_order_without_data(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        self._click(self.place_order_button)
        self._click(self.purchase_button)
        time.sleep(3)
        assert self.read_alert() == "Please fill out Name and Creditcard."

    @allure.description("Verify the place order without entering the name.")
    def test_order_without_name(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        self._click(self.place_order_button)
        self._entry(self.country_path, self.country)
        self._entry(self.city_path, self.city)
        self._entry(self.card_path, self.card_num)
        self._entry(self.month_path, self.month)
        self._entry(self.year_path, self.year)
        self._click(self.purchase_button)
        time.sleep(3)
        assert self.read_alert() == "Please fill out Name."

    @allure.description("Verify that the place order works using an invalid country.")
    def test_order_with_invalid_country(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        self._click(self.place_order_button)
        self._entry(self.name_path, self.name)
        self._entry(self.country_path, self.invalid_country)
        self._entry(self.city_path, self.city)
        self._entry(self.card_path, self.card_num)
        self._entry(self.month_path, self.month)
        self._entry(self.year_path, self.year)
        self._click(self.purchase_button)
        time.sleep(3)
        assert self.read_the_text(self.order_successfully) == "Please fill out valid Country."

    @allure.description("Verify that the place order works using an invalid city.")
    def test_order_with_invalid_city(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        self._click(self.place_order_button)
        self._entry(self.name_path, self.name)
        self._entry(self.country_path, self.country)
        self._entry(self.city_path, self.invalid_city)
        self._entry(self.card_path, self.card_num)
        self._entry(self.month_path, self.month)
        self._entry(self.year_path, self.year)
        self._click(self.purchase_button)
        time.sleep(3)
        assert self.read_the_text(self.order_successfully) == "Please fill out valid City."

    @allure.description("Verify that the place order works using an invalid Credit Card number.")
    def test_order_with_invalid_cardnum(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        self._click(self.place_order_button)
        self._entry(self.name_path, self.name)
        self._entry(self.country_path, self.country)
        self._entry(self.city_path, self.city)
        self._entry(self.card_path, self.invalid_card)
        self._entry(self.month_path, self.month)
        self._entry(self.year_path, self.year)
        self._click(self.purchase_button)
        time.sleep(3)
        assert self.read_the_text(self.order_successfully) == "Please fill out valid Creditcard."

    @allure.description("Verify place orders that work using an invalid month.")
    def test_order_with_invalid_month(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        self._click(self.place_order_button)
        self._entry(self.name_path, self.name)
        self._entry(self.country_path, self.country)
        self._entry(self.city_path, self.city)
        self._entry(self.card_path, self.card_num)
        self._entry(self.month_path, self.invalid_month)
        self._entry(self.year_path, self.year)
        self._click(self.purchase_button)
        time.sleep(3)
        assert self.read_the_text(self.order_successfully) == "Please fill out valid Month."

    @allure.description("Verify place orders that work using an invalid year.")
    def test_order_with_invalid_year(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        self._click(self.place_order_button)
        self._entry(self.name_path, self.name)
        self._entry(self.country_path, self.country)
        self._entry(self.city_path, self.city)
        self._entry(self.card_path, self.card_num)
        self._entry(self.month_path, self.month)
        self._entry(self.year_path, self.invali_year)
        self._click(self.purchase_button)
        time.sleep(3)
        assert self.read_the_text(self.order_successfully) == "Please fill out valid Creditcard."

    @allure.description("Verify that purchase information we filled in on the place order is correctly displayed on "
                        "the confirmation page")
    def test_the_purchase_info_is_correctly_recorded(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        self._click(self.place_order_button)
        self._entry(self.name_path, self.name)
        self._entry(self.country_path, self.country)
        self._entry(self.city_path, self.city)
        self._entry(self.card_path, self.card_num)
        self._entry(self.month_path, self.month)
        self._entry(self.year_path, self.invali_year)
        self._click(self.purchase_button)
        time.sleep(3)
        assert self._is_displayed(self.record)

    @allure.description("Verify that the place order doesn’t work without adding a product to the cart.")
    def test_order_without_add_product(self):
        self.open()
        self._click(self.cart_link)
        assert self.is_not_enabled(self.place_order_button) == True

    @allure.description("Verify if the close button is working")
    def test_close_button(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        self._click(self.place_order_button)
        self._click(self.purchase_close_button)
        time.sleep(3)
        assert self.is_not_displayed(self.order_page_title) == "Place order"

    @allure.description("Verify if the confirmation page and place order page are overlapped")
    def test_disappearance_of_purchase_button(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        self._click(self.place_order_button)
        self._entry(self.name_path, self.name)
        self._entry(self.country_path, self.country)
        self._entry(self.city_path, self.city)
        self._entry(self.card_path, self.card_num)
        self._entry(self.month_path, self.month)
        self._entry(self.year_path, self.invali_year)
        self._click(self.purchase_button)
        time.sleep(3)
        assert self.is_not_displayed(self.purchase_button) == True

    @allure.description("Verify ok button is working")
    def test_ok_button(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        self._click(self.place_order_button)
        self._entry(self.name_path, self.name)
        self._entry(self.country_path, self.country)
        self._entry(self.city_path, self.city)
        self._entry(self.card_path, self.card_num)
        self._entry(self.month_path, self.month)
        self._entry(self.year_path, self.invali_year)
        self._click(self.purchase_button)
        time.sleep(3)
        assert self.read_the_text(self.brand_name) == " PRODUCT STORE"




