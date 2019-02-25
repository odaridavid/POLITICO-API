from flask import Blueprint, request, jsonify, make_response
from api.v2.models.user import UserModelDb

user_api_v2 = Blueprint('user_v2', __name__, url_prefix="/api/v2")


@user_api_v2.route("/auth/signup", methods=['POST'])
def api_user_sign_up():
    user = request.get_json(force=True)
    if {"firstname", "lastname", "othername", "email", "phoneNumber", "passportUrl", "password"} <= set(user):
        validated_user = UserModelDb().user_sign_up(user)
        if 'Invalid Data' in validated_user:
            return make_response(jsonify({"status": 400, "error": "Please Check All Input Fields Are Valid"}), 400)
        elif 'User Exists' in validated_user:
            return make_response(jsonify({"status": 409, "error": "User Already Exists"}), 409)
        else:
            return make_response(
                jsonify({"status": 201, "token": validated_user}), 201)
    return make_response(jsonify({"status": 400, "error": "Please Check All Input Fields Are Filled"}), 400)


@user_api_v2.route("/auth/login", methods=['POST'])
def api_user_sign_in():
    user = request.get_json(force=True)
    if {"email", "password"} <= set(user):
        validated_user = UserModelDb().user_sign_in(user)
        if 'Invalid' in validated_user:
            return make_response(jsonify({"status": 400, "error": "Please Check All Input Fields Are Valid"}), 400)
        elif 'Non Existent User' in validated_user:
            return make_response(jsonify({"status": 400, "error": "Check Email or Password"}), 400)
        else:
            return make_response(jsonify({"status": 201, "token": validated_user}), 201)
    return make_response(jsonify({"status": 400, "error": "Please Check All Input Fields Are Filled"}), 400)
