from . import BaseTestCase


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
