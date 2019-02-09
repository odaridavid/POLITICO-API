from . import Model
from api.v1.validator import UserValidator

users = []


class UserModel(Model):
    def __init__(self, user=None, is_admin=0):
        super().__init__(item=user, list_of_items=users)
        # Remains 0 for default user
        self.isAdmin = is_admin
        # Pass in user to be validated
        self.user_validator = UserValidator(self.item)

    def user_sign_up(self):
        if not self.isAdmin == 0:
            self.isAdmin = True
        self.isAdmin = False
        # Generate Unique Id
        user_id = super().generate_id()
        # Returns Validated User Dict
        validated_user = self.user_validator.all_checks()
        if type(validated_user) == dict:
            # Checks If User is in list
            for user in users:
                if user['email'] == validated_user['email']:
                    return 'User Exists'
            created_user = {
                "id": user_id,
                "firstname": validated_user['firstname'],
                "lastname": validated_user['lastname'],
                "othername": validated_user['othername'],
                "email": validated_user['email'],
                "phoneNumber": validated_user['phoneNumber'],
                "passportUrl": validated_user['passportUrl'],
                "password": validated_user['password'],
                "isAdmin": self.isAdmin
            }
            # Add User To List
            users.append(created_user)
            return created_user['firstname']
        return 'Invalid Data Check The Fields'
