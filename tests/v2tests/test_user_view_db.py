from . import BaseTestCase
import json


class UserEndpointsTestCase(BaseTestCase):
    def test_user_sign_up_success(self):
        """
        Tests User Signed Up Successfully
        """
        response = self.client.post('api/v2/auth/signup', data=json.dumps({
            "firstname": "Davied",
            "lastname": "Odari",
            "othername": "Kiribwa",
            "email": "odari@amail.com",
            "phoneNumber": "0717455945",
            "passportUrl": "www.googledrive.com/pics?v=jejfek",
            "password": "1wwjdje3qr",
            "isAdmin": 0
        }))
        self.assertEqual(response.status_code, 201, "Sign Up Successful")
        self.assertTrue(len(response.json['token']) > 60)

    def test_user_sign_up_user_exists(self):
        """
        Tests User Signed Up Duplicate and failed
        """
        user = {
            "firstname": "Davied",
            "lastname": "Odari",
            "othername": "Kiribwa",
            "email": "odari@amail.com",
            "phoneNumber": "0717455945",
            "passportUrl": "www.googledrive.com/pics?v=jejfek",
            "password": "1wwjdje3qr",
            "isAdmin": 0
        }
        self.client.post('api/v2/auth/signup', data=json.dumps(user))
        response = self.client.post('api/v2/auth/signup', data=json.dumps(user))
        self.assertEqual(response.status_code, 409, "User Exists in db conflict 409")
        self.assertIn('User Already Exists', response.json['error'])

    def test_user_sign_up_with_invalid_data(self):
        """
        Tests User Signed Up with invalid data
        """
        user = {
            "firstname": "Davied",
            "lastname": "Odari",
            "othername": "Kiribwa",
            "email": "odamail.com",
            "phoneNumber": "0717455945",
            "passportUrl": "www.googledrive.com/pics?v=jejfek",
            "password": "1wwjdje3qr",
            "isAdmin": 0
        }
        self.client.post('api/v2/auth/signup', data=json.dumps(user))
        response = self.client.post('api/v2/auth/signup', data=json.dumps(user))
        self.assertEqual(response.status_code, 400, "Input fields should be empty'")
        self.assertIn('Please Check All Input Fields Are Valid', response.json['error'])

    def test_user_sign_up_with_missing_data(self):
        """
        Tests User Signed Up with missing
        """
        user = {
            "firstname": "Davied",
            "lastname": "Odari",
            "passportUrl": "www.googledrive.com/pics?v=jejfek",
            "password": "1wwjdje3qr"
        }
        self.client.post('api/v2/auth/signup', data=json.dumps(user))
        response = self.client.post('api/v2/auth/signup', data=json.dumps(user))
        self.assertEqual(response.status_code, 400, "Should contain insufficient keys  for request")
        self.assertIn('Please Check All Input Fields Are Filled', response.json['error'])

    def test_user_sign_in_success(self):
        """
        Tests User Signed in Successfully
        """
        self.client.post('api/v2/auth/signup', data=json.dumps({
            "firstname": "Davied",
            "lastname": "Odari",
            "othername": "Kiribwa",
            "email": "odari@amail.com",
            "phoneNumber": "0717455945",
            "passportUrl": "www.googledrive.com/pics?v=jejfek",
            "password": "1wwjdje3qr",
            "isAdmin": 0
        }))
        response = self.client.post('api/v2/auth/login', data=json.dumps({
            "email": "odari@amail.com",
            "password": "1wwjdje3qr"
        }))
        self.assertEqual(response.status_code, 201, "Login Should be Successful")
        self.assertTrue(len(response.json['token']) > 50)

    def test_user_sign_in_unsuccessful(self):
        """
        Tests User Sign In was unsuccessful
        """
        self.client.post('api/v2/auth/signup', data=json.dumps({
            "firstname": "Davied",
            "lastname": "Odari",
            "othername": "Kiribwa",
            "email": "odari@amail.com",
            "phoneNumber": "0717455945",
            "passportUrl": "www.googledrive.com/pics?v=jejfek",
            "password": "1wwjdje3qr",
            "isAdmin": 0
        }))
        response = self.client.post('api/v2/auth/login', data=json.dumps({
            "email": "odari@amail.com",
            "password": "1ww1dqe3qr"
        }))
        self.assertEqual(response.status_code, 400, "Login Should be unsuccessful")
        self.assertIn('Please Check All Input Fields Are Valid', response.json['error'])

    def test_user_sign_in_unsuccessful_missing_data(self):
        """
        Tests User Sign In was unsuccessful
        """
        response = self.client.post('api/v2/auth/login', data=json.dumps({
            "email": "odari@amail.com",
        }))
        self.assertEqual(response.status_code, 400, "Login Should be unsuccessful")
        self.assertIn('Please Check All Input Fields Are Filled', response.json['error'])
