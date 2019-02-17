from flask import Blueprint, request, jsonify, make_response
from api.v2.models.office_model import OfficesModelDb

office_api_v2 = Blueprint('office_v2', __name__, url_prefix="/api/v2")


@office_api_v2.route("/offices", methods=['POST'])
def api_create_office():
    # get the office as json
    office = request.get_json(force=True)
    # Checks keys exist in given dict as sets
    if {'type', 'name'} <= set(office):
        # add office to model which returns generated id
        office_name = OfficesModelDb(office).create_office()
        if 'Office Exists' in office_name:
            # Duplicate Office not allowed
            return make_response(jsonify({"status": 409, "error": "Office Already Exists"}), 409)
        elif 'Invalid Data' in office_name:
            # Invalid Data
            return make_response(jsonify({"status": 400, "error": "Check Input Values"}), 400)

        response_body = {
            "status": 201,
            "data": [{
                "name": office_name
            }]
        }
        # Successful
        return make_response(jsonify(response_body), 201)
    # Missing Keys
    return make_response(jsonify({"status": 400, "error": "Missing Key value"}), 400)


@office_api_v2.route("/offices", methods=['GET'])
def api_get_offices():
    offices = OfficesModelDb().get_all_offices()
    # If parties list has no items or does  Successful
    return make_response(jsonify({"status": 200, "data": offices}), 200)
