class UserValidator:
    def __init__(self, user):
        self.user = user

    def check_first_name_value(self):
        if len(self.user['firstname']) >= 3 and type(self.user['firstname']) == str:
            return self.user['firstname']
        return 'Invalid'

    def check_last_name_value(self):
        if len(self.user['lastname']) >= 3 and type(self.user['firstname']) == str:
            return self.user['lastname']
        return 'Invalid'

    def check_other_name_value(self):
        if len(self.user['othername']) >= 3 and type(self.user['firstname']) == str:
            return self.user['othername']
        return 'Invalid'

    def check_phone_number_value(self):
        if 10 <= len(self.user['phoneNumber']) <= 13:
            return self.user['phoneNumber']
        return 'Invalid'

    def check_passport_url_value(self):
        if len(self.user['passportUrl']) > 0:
            return self.user['passportUrl']
        return 'Invalid'

    def check_password(self):
        if not len(self.user['password']) >= 8:
            return 'Invalid'
        return self.user['password']

    def check_email(self):
        if any(val == "@" for val in self.user['email']):
            if any(val == "." for val in self.user['email']):
                return self.user['email']
            return 'Invalid'
        return 'Invalid'

    def all_checks(self):
        validated_f_name = self.check_first_name_value()
        validated_l_name = self.check_last_name_value()
        validated_o_name = self.check_other_name_value()
        validated_pass_url = self.check_passport_url_value()
        validated_phone_no = self.check_phone_number_value()
        validated_email = self.check_email()
        validated_password = self.check_password()
        if 'Invalid' not in [validated_f_name, validated_l_name, validated_o_name,
                             validated_pass_url, validated_email, validated_phone_no,
                             validated_password]:
            return {
                "firstname": validated_f_name,
                "lastname": validated_l_name,
                "othername": validated_o_name,
                "email": validated_email,
                "phoneNumber": validated_phone_no,
                "passportUrl": validated_pass_url,
                "password": validated_password
            }
        return 'Invalid'


class OfficeValidator:
    pass


class PartyValidator:
    pass
