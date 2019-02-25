import re


class UserValidator:
    def __init__(self, user):
        self.user = user
        self.email = self.user['email']

    def check_phone_number_value(self):
        if 10 <= len(self.user['phoneNumber']) <= 13:
            return self.user['phoneNumber']
        return 'Invalid'

    def check_passport_url_value(self):
        if len(self.user['passportUrl']) > 0:
            if re.match(r"[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)",
                        self.user['passportUrl']):
                return self.user['passportUrl']
        return 'Invalid'

    def check_password(self):
        if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', self.user['password']):
            return self.user['password']
        return 'Invalid'

    def check_email(self):
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$)", self.user['email']):
            return self.user['email']
        return 'Invalid'

    def all_checks(self):
        validated_f_name = CheckStrings(self.user['firstname']).check_strings()
        validated_l_name = CheckStrings(self.user['lastname']).check_strings()
        validated_o_name = CheckStrings(self.user['othername']).check_strings()
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


class CheckStrings:
    def __init__(self, item):
        self.item = item

    def check_strings(self):
        """Validated Strings and prevents entry of any other type"""
        if isinstance(self.item, str):
            if len(self.item.strip()) >= 3:
                return self.item
        return 'Invalid'


class OfficeValidator:
    def __init__(self, office):
        self.office = office

    def all_checks(self):
        validated_office_type = CheckStrings(self.office['type']).check_strings()
        validated_office_name = CheckStrings(self.office['name']).check_strings()
        if 'Invalid' not in [validated_office_type, validated_office_name]:
            return {
                "type": validated_office_type,
                "name": validated_office_name
            }
        return 'Invalid'


class PartyValidator:
    def __init__(self, party):
        self.party = party

    def all_checks(self):
        validated_party_name = CheckStrings(self.party['name']).check_strings()
        validated_party_address = CheckStrings(self.party['hqAddress']).check_strings()
        validated_party_url = CheckStrings(self.party['logoUrl']).check_strings()
        if 'Invalid' not in [validated_party_name, validated_party_address, validated_party_url]:
            return {
                "name": validated_party_name,
                "hqAddress": validated_party_address,
                "logoUrl": validated_party_url
            }
        return 'Invalid'


class PetitionValidator:
    def __init__(self, petition):
        self.petition = petition

    def checks(self, key_name):
        """Checks id is valid"""
        if not self.petition[key_name] > 0:
            return 'Invalid'
        return self.petition[key_name]

    def check_body(self):
        """Checks body of petition"""
        if not len(self.petition['body']) >= 100:
            return 'Invalid'
        return self.petition['body']

    def all_checks(self):
        validate_user_response = self.checks('createdBy')
        validate_office_response = self.checks('office')
        validate_body_response = self.check_body()
        if 'Invalid' not in [validate_user_response, validate_office_response, validate_body_response]:
            return {
                "createdBy": validate_user_response,
                "office": validate_office_response,
                "body": validate_body_response
            }
        return 'Invalid'
