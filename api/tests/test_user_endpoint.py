from . import BaseTestCase
from run import app
import json


class UserEndpointsTestCase(BaseTestCase):
    def setUp(self):
        self.user = {
            "firstname": "David",
            "lastname": "Odari",
            "othername": "Kiribwa",
            "email": "odari@mail.com",
            "phoneNumber": "0717455945",
            "passportUrl": "www.googledrive.com/pics?v=jejfek",
            "password": "12we3e4r"
        }
        self.user_invalid = {
            "firstname": "David",
            "lastname": "Odari",
            "othername": "Kiribwa",
            "email": "od",
            "phoneNumber": "0717455945",
            "passportUrl": "www.googledrive.com/pics?v=jejfek",
            "password": "12we4r"
        }
        self.client = app.test_client()

    def test_user_sign_up_success(self):
        response = self.client.post('api/v1/users', data=json.dumps(self.user))
        assert 201 == response.status_code
        assert 'Signed Up Successfully' in response.json['data']

    def test_user_sign_up_fail(self):
        response = self.client.post('api/v1/users', data=json.dumps(self.user_invalid))
        assert 400 == response.status_code
        assert 'Invalid Data' in response.json['error']

    def test_user_sign_up_invalid_keys(self):
        response = self.client.post('api/v1/users', data=json.dumps({"firstname": "David"}))
        assert 403 == response.status_code
        assert 'Invalid Request' in response.json['error']

    def test_user_sign_up_user_exists(self):
        self.client.post('api/v1/users', data=json.dumps(self.user))
        self.client.post('api/v1/users', data=json.dumps(self.user))
        response = self.client.post('api/v1/users', data=json.dumps(self.user))
        assert 409 == response.status_code
        assert 'User Already Exists' in response.json['error']
