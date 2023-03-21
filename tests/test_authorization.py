import requests
import endpoints


class TestAuthorization:

    def test_successful_authorization(self):
        authorization_headers = {'API-KEY': 'V1stul4!@2021'}
        response = requests.post(endpoints.authorized_url, headers=authorization_headers)
        assert response.status_code == 200

    def test_missing_header(self):
        response = requests.post(endpoints.authorized_url)
        assert response.status_code == 401

    def test_incorrect_header(self):
        authorization_headers = {'API-KEY': 'meowmeow'}
        response = requests.post(endpoints.authorized_url, headers=authorization_headers)
        assert response.status_code == 403

