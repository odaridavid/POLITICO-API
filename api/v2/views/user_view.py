from flask import Blueprint, request, jsonify, make_response
from api.v2.models.user_model import UserModelDb

user_api_v2 = Blueprint('user_v2', __name__, url_prefix="/api/v2")


@user_api_v2.route("/auth/signup", methods=['POST'])
def api_user_sign_up():
    user = request.get_json(force=True)
    # Make Sure Keys Exist
    if {"firstname", "lastname", "othername", "email", "phoneNumber", "passportUrl", "password","isAdmin"} <= set(user):
        validated_user_msg = UserModelDb(user).user_sign_up()
        if 'Invalid Data' in validated_user_msg:
            # Invalidated data
            return make_response(jsonify({"status": 400, "error": "Parsing Invalid Data ,Bad Request"}), 400)
        elif 'User Exists' in validated_user_msg:
            # Duplicate User not allowed
            return make_response(jsonify({"status": 409, "error": "User Already Exists"}), 409)
        else:
            return make_response(
                jsonify({"status": 201, "data": "{} Signed Up Successfully".format(validated_user_msg)}), 201)
    #     Missing data
    return make_response(jsonify({"status": 400, "error": "Invalid Request ,Missing Data"}), 400)
