from . import Model
from api.v1.validator import UserValidator

users = []


class UserModel(Model):
    def __init__(self, user=None, is_admin=0):
        super().__init__(item=user, list_of_items=users)
        self.isAdmin = is_admin
        self.validated_user = UserValidator(self.item)

    def user_sign_up(self):
        # 0 for user 1 for admin
        if self.isAdmin is not 0:
            self.isAdmin = True
        else:
            self.isAdmin = False
        user_id = Model(list_of_items=users).generate_id()
        validated_user = self.validated_user.all_checks()
        if type(validated_user) == dict:
            # Extracts data from passed dict
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

            users.append(created_user)
            return created_user['firstname']
        return 'Invalid Data Check The Fields'

