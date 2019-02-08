from . import BaseTestCase
from api.v1.validator import UserValidator, CheckStrings


class UserValidatorTest(BaseTestCase):
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
            "firstname": "Da",
            "lastname": "Od",
            "othername": "Ka",
            "email": "odarmail",
            "phoneNumber": "07145",
            "passportUrl": "",
            "password": "12w"
        }

        self.validator_invalid = UserValidator(self.user_invalid)

    def test_check_name(self):
        validator = CheckStrings(self.user['firstname'])
        assert validator.check_string() == "David"

    def test_check_phone_number(self):
        validator = UserValidator(self.user)
        assert validator.check_phone_number_value() == "0717455945"

    def test_check_passport_url(self):
        validator = UserValidator(self.user)
        assert validator.check_passport_url_value() == "www.googledrive.com/pics?v=jejfek"

    def test_check_password(self):
        validator = UserValidator(self.user)
        assert validator.check_password() == "12we3e4r"

    def test_check_email(self):
        validator = UserValidator(self.user)
        assert validator.check_email() == "odari@mail.com"

    def test_check_name_invalid(self):
        validator = CheckStrings(self.user_invalid['firstname'])
        assert validator.check_string() == "Invalid"

    def test_check_phone_number_invalid(self):
        validator = UserValidator(self.user_invalid)
        assert validator.check_phone_number_value() == "Invalid"

    def test_check_passport_url_invalid(self):
        validator = UserValidator(self.user_invalid)
        assert validator.check_passport_url_value() == "Invalid"

    def test_check_password_invalid(self):
        validator = UserValidator(self.user_invalid)
        assert validator.check_password() == "Invalid"

    def test_check_email_invalid(self):
        validator = UserValidator(self.user_invalid)
        assert validator.check_email() == "Invalid"
