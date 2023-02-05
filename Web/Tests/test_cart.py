import time
import allure
import pytest

from Web.Data.data import *
from Web.PageObject.page_object import PageObject


class Test_Cart(PageObject, Colors, Inputs):
    @allure.description("Test adding the random product to the cart.")
    def test_add_to_cart(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        assert self._is_displayed(self.added_product) == True

    @allure.description("Test the price will be doubled when we add the same product.")
    def test_price_increment(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.home_link)
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        assert self._find(self.product_on_cart) == 2*float(self._find(self.random_price).text)

    @allure.description("Check if the product is disappeared from the cart after deleted")
    def test_delete_product_from_cart(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        self._click(self.delete)
        assert self.is_not_displayed(self.product_on_cart) == False

    @allure.description("Verify the title of cart page")
    def test_title_of_cart_page(self):
        self.open()
        self._click(self.cart_link)
        assert self.read_the_text(self.cart_title) == "Cart"

    @allure.description("Verify  if the price of the product is correct after adding it to the cart")
    def test_price_after_add_to_cart(self):
        self.open()
        self._click(self.random_product)
        self._click(self.add_to_cart)
        self.alert_ok()
        self._click(self.cart_link)
        assert self.read_the_text(self.price_on_cart) == "360"









