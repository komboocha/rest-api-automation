import requests
import random

base_url = 'https://g07547egsi.execute-api.eu-west-1.amazonaws.com/dev/'

valid_status_codes = (200, 201, 2020, 300, 301, 302, 400, 401, 403, 404, 500, 503)


class TestEndpoints:

    def send_and_assert_echo_status(self, request_status, response_status):
        url = f'{base_url}/echostatus/{request_status}'
        response = requests.get(url)
        assert response.status_code == response_status

    def test_get_status_code(self):
        url = f'{base_url}/alwaysok'
        get_status_response = requests.get(url)

        assert get_status_response.status_code == 200

    def test_echo_status_proper_code(self):
        request_status = random.choice(valid_status_codes)
        self.send_and_assert_echo_status(request_status, request_status)

    def test_echo_status_improper_numeric_code(self):
        request_status = 1
        self.send_and_assert_echo_status(request_status, 400)

    def test_echo_status_improper_non_numeric_code(self):
        self.send_and_assert_echo_status('burak345', 400)







