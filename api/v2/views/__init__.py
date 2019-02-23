from flask_jwt_extended import get_jwt_identity
from api.v2.models.user_model import UserModelDb


def check_user():
    current_user = get_jwt_identity()
    return UserModelDb().get_user_by_id(current_user)
