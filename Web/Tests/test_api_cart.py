import allure
import requests
import jsonpath

from Web.API_Constants.cart import Cart


class Test_API(Cart):

    @allure.description("Check Api for cart without add product")
    def test_api_for_empty_cart(self):
        url = self.cart_url
        data = self.empty_data
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert res_data == self.message_no_item

    @allure.description("Check Api for cart by adding 1 products")
    def test_api_for_cart_2products(self):
        url = self.cart_url
        data = self.data_with_product
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert len(res_data['Items']) == 2





