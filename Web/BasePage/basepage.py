import allure
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class BasePage:
    _driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def _find(self, locate) -> WebElement:
        self._wait_until_element_is_visible(locate)
        return self._driver.find_element(*locate)

    def _entry(self, locate, content):
        self._wait_until_element_is_visible(locate)
        self._find(locate).send_keys(content)

    def _wait_until_element_is_visible(self, locate, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        try:
            wait.until(ec.visibility_of_element_located(locate))
        except TimeoutError:
            print("The element is not present on the page")

    def scroll(self, locate, upto):
        self._wait_until_element_is_visible(locate)
        self._driver.execute_script(upto)

    @allure.step("Clicking the element")
    def _click(self, locate):
        self._wait_until_element_is_visible(locate)
        self._find(locate).click()

    def _is_displayed(self, locate) -> bool:
        return self._find(locate).is_displayed()

    def _find_elements(self, locator):
        self._wait_until_element_is_visible(locator)
        return self._driver.find_elements(*locator)