import allure
import requests

from Web.API_Constants.login_constants import Login


class Test_API(Login):

    @allure.description("Check Api for login using valid password and username")
    def test_api_for_login_correctly(self):
        url = self.login_url
        data = self.valid_data
        res = requests.post(url, json=data)
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10

    @allure.description("Check Api for login using invalid password and username")
    def test_api_for_login_incorrectly(self):
        url = self.login_url
        data = self.invalid_data
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10

    @allure.description("Check Api for login using incorrect password")
    def test_api_for_login_incorrectly(self):
        url = self.login_url
        data = self.incorrect_pass
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert res_data == self.wrong_pass_error

    @allure.description("Check Api for signup with existing user data")
    def test_api_signup_existing(self):
        url = self.signup_url
        data = self.valid_data
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert res_data == self.signup_error
