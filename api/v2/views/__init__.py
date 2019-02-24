from flask_jwt_extended import get_jwt_identity
from api.v2.models.user import UserModelDb


def check_user():
    current_user = get_jwt_identity()
    return UserModelDb().get_user_by_id(current_user)


def id_conversion(item_id):
    try:
        oid = int(item_id)
        return oid
    except ValueError:
        return 'Invalid'
