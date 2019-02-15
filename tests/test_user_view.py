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
        """
        Tests User Signed Up Successfully
        """
        response = self.client.post('api/v1/users', data=json.dumps(self.user))
        self.assertEqual(response.status_code, 201, "Sign Up Successful")
        self.assertIn('Signed Up Successfully', response.json['data'])

    def test_user_sign_up_fail(self):
        """
        Tests User sign up failed
        """
        response = self.client.post('api/v1/users', data=json.dumps(self.user_invalid))
        self.assertEqual(response.status_code, 400, "Sign Up Failed")
        self.assertIn('Invalid Data', response.json['error'])

    def test_user_sign_up_invalid_keys(self):
        """
        Tests User cant sign up with insufficient info
        """
        response = self.client.post('api/v1/users', data=json.dumps({"firstname": "David"}))
        self.assertEqual(response.status_code, 400, "Insufficient Information Being Passed In")
        self.assertIn('Invalid Request', response.json['error'])

    def test_user_sign_up_user_exists(self):
        """
        Test User cant sign up with same email
        """
        self.client.post('api/v1/users', data=json.dumps(self.user))
        self.client.post('api/v1/users', data=json.dumps(self.user))
        response = self.client.post('api/v1/users', data=json.dumps(self.user))
        self.assertEqual(response.status_code, 409, "Conflict With Existing User")
        self.assertIn('User Already Exists', response.json['error'])
