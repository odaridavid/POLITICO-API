from . import Model
from api.v1.validator import UserValidator

users = []


class UserModel(Model):
    def __init__(self, user=None, is_admin=0):
        super(UserModel, self).__init__(item=user, list_of_items=users)
        # Remains 0 for default user
        self.isAdmin = is_admin

    def user_is_admin(self):
        if not self.isAdmin == 0:
            return True
        return False

    def user_sign_up(self):
        admin_status = self.user_is_admin()
        # Generate Unique Id
        user_id = super(UserModel,self).generate_id()
        # Returns Validated User Dict
        validated_user = UserValidator(self.item).all_checks()
        if not validated_user == 'Invalid':
            # Checks If User is in list
            # TODO List Comprehension
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
                "isAdmin": admin_status
            }
            # Add User To List
            users.append(created_user)
            return created_user['firstname']
        return 'Invalid Data Check The Fields'
