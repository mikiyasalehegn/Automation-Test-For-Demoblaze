import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Web.BasePage.basepage import BasePage
from Web.Data.data import *


class PageObject(BasePage, Locators):
    @allure.step("Opening the website")
    def open(self):
        self._driver.get(self.url)
        self._driver.maximize_window()

    @allure.step("Asserting color")
    def color_assertion(self, locate):
        return self._find(locate).value_of_css_property("background-color")

    @allure.step("Scrolling the page")
    def scrolling_page(self, location, amount):
        self.scroll(location, amount)

    @allure.step("Checking all the categories")
    def checking_categories(self, locator):
        for category in locator:
            self._is_displayed(category)

    @allure.step("Accepting alert")
    def alert_ok(self, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.alert_is_present())
        self._driver.switch_to.alert.accept()

    @allure.step("Read alert message")
    def read_alert(self, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.alert_is_present())
        return self._driver.switch_to.alert.text

    @allure.step("Read the text of the element")
    def read_the_text(self, locate):
        self._wait_until_element_is_visible(locate)
        return self._find(locate).accessible_name

    def _clear_the_field(self, locate):
        self._wait_until_element_is_visible(locate)
        self._find(locate).clear()

    @allure.step("Checking if the element is not enabled")
    def is_not_enabled(self, locate):
        if self._find(locate).is_enabled() is False:
            return True
        else:
            return False

    @allure.step("Checking if the password id not revealed")
    def password_not_revealed(self, locate):
        typee = self._find(locate).get_attribute("type")
        if typee == "password":
            return True
        else:
            return False

    @allure.step("Checking if the element is not displayed")
    def is_not_displayed(self, locate):
        if self._find(locate).is_displayed() is True:
            return False
        else:
            return True

    @allure.step("Verifying number of products on the page")
    def number_of_products_on_page(self, locate):
        self._wait_until_element_is_visible(locate)
        products = self._find_elements(locate)
        return len(products)

    def defining_the_element(self, locate):
        product = self._find(locate)
        return product

    def there_is_no_duplicated_product(self, locate):
        self._wait_until_element_is_visible(locate)
        products = self._find_elements(locate)
        exact_number_of_products = set(products)
        if len(products) == len(exact_number_of_products):
            return True
        else:
            return False












