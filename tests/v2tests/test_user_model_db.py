from . import BaseTestCase
from api.v2.models.user_model import UserModelDb


class UserModelDbTestCase(BaseTestCase):
    def test_user_sign_up_successful(self):
        """Tests User added successfully to database"""
        user_name = self.user.user_sign_up()
        self.assertEqual(user_name, 'David')

    def test_user_sign_up_duplicate(self):
        """Tests User cant be added more than once"""
        self.user.user_sign_up()
        integrity_error = self.user.user_sign_up()
        self.assertEqual(integrity_error, 'User Exists')

    def test_user_sign_up_invalid_data(self):
        """Tests User cant sign up with invalid data"""
        invalid_data = self.user_invalid.user_sign_up()
        self.assertEqual(invalid_data, 'Invalid Data')

    def test_user_sign_in_successful(self):
        """Tests user signed in successfully"""
        self.user.user_sign_up()
        user_sign_in = UserModelDb({"email": "odari@gmail.com", "password": "12we3e4r"})
        sign_in_response = user_sign_in.user_sign_in()
        self.assertTrue(len(sign_in_response) > 50)

    def test_user_sign_in_unsuccessful(self):
        """Tests user sign in unsuccessfully"""
        self.user.user_sign_up()
        user_sign_in = UserModelDb({"email": "odari@gmail.com", "password": "12w2sas21e4r"})
        sign_in_response = user_sign_in.user_sign_in()
        self.assertEqual(sign_in_response, 'Invalid')
