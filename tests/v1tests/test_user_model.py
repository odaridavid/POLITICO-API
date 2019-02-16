from tests.v1tests import BaseTestCase
from api.v1.models.user_model import UserModel


class UserModelTest(BaseTestCase):
    def setUp(self):
        self.user = UserModel(
            user={
                "firstname": "David",
                "lastname": "Odari",
                "othername": "Kiribwa",
                "email": "odari@mail.com",
                "phoneNumber": "0717455945",
                "passportUrl": "www.googledrive.com/pics?v=jejfek",
                "password": "12we3e4r"
            })
        self.user_invalid = UserModel(
            user={
                "firstname": "David",
                "lastname": "Od",
                "othername": "Kiribwa",
                "email": "odari@mail.com",
                "phoneNumber": "0717455945",
                "passportUrl": "www.googledrive.com/pics?v=jejfek",
                "password": "12we3e4r"
            })

    def test_user_sign_up(self):
        """
        Test User Model Creates New User
        """
        user_name = self.user.user_sign_up()
        self.assertEqual(user_name, "David")

    def test_user_sign_up_exists(self):
        """
        Test User Model Rejects Duplicate User Sign Up with email
        """
        self.user.user_sign_up()
        user_name = self.user.user_sign_up()
        self.assertEqual(user_name, "User Exists")

    def test_user_sign_up_incorrect_value(self):
        """
        Test User Sign Up fails with insufficient fields
        """
        user_name = self.user_invalid.user_sign_up()
        self.assertEqual(user_name, "Invalid Data Check The Fields")

    def test_user_is_admin(self):
        self.user_admin = UserModel(user=self.user, is_admin=1)
        resp_admin_user = self.user_admin.user_is_admin()
        self.assertTrue(resp_admin_user, "User should be admin")

    def test_user_is_not_admin(self):
        self.user_not_admin = UserModel(user=self.user, is_admin=0)
        resp_normal_user = self.user_not_admin.user_is_admin()
        self.assertFalse(resp_normal_user, "User should not be admin")
