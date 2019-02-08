from . import BaseTestCase
from api.v1.validator import UserValidator


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

    def test_check_first_name(self):
        validator = UserValidator(self.user)
        assert validator.check_first_name_value() == "David"

    def test_check_last_name(self):
        validator = UserValidator(self.user)
        assert validator.check_last_name_value() == "Odari"

    def test_check_other_name(self):
        validator = UserValidator(self.user)
        assert validator.check_other_name_value() == "Kiribwa"

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

    def test_check_first_name_invalid(self):
        validator = UserValidator(self.user_invalid)
        assert validator.check_first_name_value() == "Invalid"

    def test_check_last_name_invalid(self):
        validator = UserValidator(self.user_invalid)
        assert validator.check_last_name_value() == "Invalid"

    def test_check_other_name_invalid(self):
        validator = UserValidator(self.user_invalid)
        assert validator.check_other_name_value() == "Invalid"

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
