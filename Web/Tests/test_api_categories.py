import json
import allure
import jsonpath
import requests

from Web.API_Constants.Category_const import Cat


class Test_Categories(Cat):

    @allure.description("Check Api for phones categories")
    def test_api_for_phones(self):
        url = self.cat_url
        data = self.phone_data
        res = requests.post(url, json=data)
        products = len(res.json()["Items"])
        first_pro_name = jsonpath.jsonpath(json.loads(res.text), 'Items[0].title')[0]
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert products == 7
        assert first_pro_name == 'Samsung galaxy s6'

    @allure.description("Check Api for laptops categories")
    def test_api_for_laptops(self):
        url = self.cat_url
        data = self.laptop_data
        res = requests.post(url, json=data)
        products = len(res.json()["Items"])
        first_pro_name = jsonpath.jsonpath(json.loads(res.text), 'Items[0].title')[0]
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert products == 6
        assert first_pro_name == "Sony vaio i5"

    @allure.description("Check Api for monitors categories")
    def test_api_for_monitors(self):
        url = self.cat_url
        data = self.monitor_data
        res = requests.post(url, json=data)
        products = len(res.json()["Items"])
        first_pro_name = jsonpath.jsonpath(json.loads(res.text), 'Items[0].title')[0]
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert products == 2
        assert first_pro_name == 'Apple monitor 24'

    @allure.description("Check Api for all products")
    def test_api_for_all_products(self):
        url = self.all_products
        res = requests.get(url)
        products = len(res.json()["Items"])
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert products == 15


