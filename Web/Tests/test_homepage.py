import time
import allure
from Web.Data.data import *
from Web.PageObject.page_object import PageObject


class Test_Home(PageObject, Colors, Inputs):

    @allure.description("Verify the background color of the headers is blue-black.")
    def test_background_color_of_header(self):
        self.open()
        assert self.color_assertion(self.header) == self.dark_blue

    @allure.description("Verify the background color of the footer is blue-black.")
    def test_background_color_of_footer(self):
        self.open()
        self.scrolling_page(self.footer, "window.scrollBy(0,500)")
        assert self.color_assertion(self.footer) == self.dark_blue

    @allure.description("Verify the background color of the body is white.")
    def test_background_color_of_body(self):
        self.open()
        self.scrolling_page(self.footer, "window.scrollBy(0,250)")
        assert self.color_assertion(self.body) == self.white1

    @allure.description("Verify the text color of the page title is white.")
    def test_textcolor_of_brand_name(self):
        self.open()
        assert self.color_assertion(self.brand_name) == self.white2

    @allure.description("Verify that the category buttons are displayed on the home page.")
    def test_categories_are_displayed(self):
        self.open()
        self.scrolling_page(self.footer, "window.scrollBy(0,250)")
        self.checking_categories(self.categories)

    @allure.description("Verify whether the welcome text is displayed after login on the home page or not.")
    def test_welcome_text_after_login(self):
        self.open()
        self._click(self.login_link)
        self._clear_the_field(self.username_path)
        self._entry(self.username_path, self.username)
        self._clear_the_field(self.password_path)
        self._entry(self.password_path, self.password)
        self._click(self.login_button)
        self._is_displayed(self.name_of_user)
        time.sleep(2)

    @allure.description("Verify the total number of phones in phones category")
    def test_amount_of_phones(self):
        self.open()
        time.sleep(3)
        self.scrolling_page(self.next_button, "window.scrollBy(0,250)")
        self._click(self.phone_link)
        time.sleep(3)
        assert self.number_of_products_on_page(self.products_on_page) == 7

    @allure.description("Verify that the number of products in the laptops category are displayed on the home page.")
    def test_amount_of_laptops(self):
        self.open()
        time.sleep(3)
        self.scrolling_page(self.next_button, "window.scrollBy(0,250)")
        self._click(self.laptop_link)
        time.sleep(3)
        assert self.number_of_products_on_page(self.products_on_page) == 6

    @allure.description("Verify that the number of products in the monitors' category are displayed on the home page.")
    def test_amount_of_monitors(self):
        self.open()
        time.sleep(3)
        self.scrolling_page(self.next_button, "window.scrollBy(0,250)")
        self._click(self.monitors_link)
        time.sleep(3)
        assert self.number_of_products_on_page(self.products_on_page) == 2

    @allure.description("Check if there is duplicated product first page")
    def test_duplication_of_products_on_1st_page(self):
        self.open()
        time.sleep(3)
        assert self.there_is_no_duplicated_product(self.products_on_page) == True

    @allure.description("Check if there is duplicated product on the 2nd page")
    def test_duplication_of_products_on_2nd_page(self):
        self.open()
        self.scrolling_page(self.next_button, "window.scrollBy(0,500)")
        time.sleep(3)
        self._click(self.next_button)
        time.sleep(3)
        assert self.there_is_no_duplicated_product(self.products_on_page) == True
