from . import BaseTestCase
from api.v2.models.user import UserModelDb


class UserModelDbTestCase(BaseTestCase):
    def test_user_sign_up_successful(self):
        """Tests User added successfully to database"""
        token = self.user.user_sign_up({"firstname": "David",
                                        "lastname": "Odari",
                                        "othername": "Kiribwa",
                                        "email": "odari@gmail.com",
                                        "phoneNumber": "0717455945",
                                        "passportUrl": "www.googledrive.com/pics?v=jejfek",
                                        "password": "12we3e4r",
                                        "isAdmin": 'f'
                                        })
        self.assertTrue(len(token) > 60)

    def test_user_sign_up_duplicate(self):
        """Tests User cant be added more than once"""
        user_info = {"firstname": "David",
                     "lastname": "Odari",
                     "othername": "Kiribwa",
                     "email": "odari@gmail.com",
                     "phoneNumber": "0717455945",
                     "passportUrl": "www.googledrive.com/pics?v=jejfek",
                     "password": "12we3e4r",
                     "isAdmin": 'f'
                     }
        self.user.user_sign_up(user_info)
        integrity_error = self.user.user_sign_up(user_info)
        self.assertEqual(integrity_error, 'User Exists')

    def test_user_sign_up_invalid_data(self):
        """Tests User cant sign up with invalid data"""
        invalid_data = self.user_invalid.user_sign_up(user={"firstname": "David",
                                                            "lastname": "Od",
                                                            "othername": "Kiribwa",
                                                            "email": "odari@mail.com",
                                                            "phoneNumber": "0717455945",
                                                            "passportUrl": "www.googledrive.com/pics?v=jejfek",
                                                            "password": "12we3e4r"
                                                            })
        self.assertEqual(invalid_data, 'Invalid Data')

    def test_user_sign_in_successful(self):
        """Tests user signed in successfully"""
        user_info = {"firstname": "David",
                     "lastname": "Odari",
                     "othername": "Kiribwa",
                     "email": "odari@gmail.com",
                     "phoneNumber": "0717455945",
                     "passportUrl": "www.googledrive.com/pics?v=jejfek",
                     "password": "12we3e4r",
                     "isAdmin": 'f'
                     }
        self.user.user_sign_up(user_info)
        user_sign_in = UserModelDb()
        sign_in_response = user_sign_in.user_sign_in({"email": "odari@gmail.com", "password": "12we3e4r"})
        self.assertTrue(len(sign_in_response) > 50)

    def test_user_sign_in_unsuccessful(self):
        """Tests user sign in unsuccessfully"""
        user_info = {"firstname": "David",
                     "lastname": "Odari",
                     "othername": "Kiribwa",
                     "email": "odari@gmail.com",
                     "phoneNumber": "0717455945",
                     "passportUrl": "www.googledrive.com/pics?v=jejfek",
                     "password": "12we3e4r",
                     "isAdmin": 'f'
                     }
        self.user.user_sign_up(user_info)
        user_sign_in = UserModelDb()
        sign_in_response = user_sign_in.user_sign_in({"email": "odari@gmail.com", "password": "12w2sas21e4r"})
        self.assertEqual(sign_in_response, 'Invalid')
