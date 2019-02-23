from flask import Blueprint, request, jsonify, make_response
from api.v2.models.office import OfficesModelDb
from flask_jwt_extended import jwt_required
from . import check_user, id_conversion

office_api_v2 = Blueprint('office_v2', __name__, url_prefix="/api/v2")


@office_api_v2.route("/offices", methods=['POST'])
@jwt_required
def api_create_office():
    if 'Requires Admin Privilege' not in check_user():
        office = request.get_json(force=True)
        # Checks keys exist in given dict as sets
        if {'type', 'name'} <= set(office):
            office_name = OfficesModelDb(office).create_office()
            if 'Office Exists' in office_name:
                return make_response(jsonify({"status": 409, "error": "Office Already Exists"}), 409)
            elif 'Invalid Data' in office_name:
                return make_response(jsonify({"status": 400, "error": "Check Input Values"}), 400)
            response_body = {
                "status": 201,
                "data": [{
                    "name": office_name
                }]
            }
            return make_response(jsonify(response_body), 201)
        return make_response(jsonify({"status": 400, "error": "Please Check All Input Fields Are Filled"}), 400)
    return make_response(jsonify({"status": 401, "error": "Unauthorized Access,Requires Admin Rights"}), 401)


@office_api_v2.route("/offices", methods=['GET'])
@jwt_required
def api_get_offices():
    offices = OfficesModelDb().get_all_offices()
    return make_response(jsonify({"status": 200, "data": offices}), 200)


@office_api_v2.route("/offices/<offices_id>/name", methods=['PATCH'])
@jwt_required
def api_edit_office(offices_id):
    if 'Requires Admin Privilege' not in check_user():
        oid = id_conversion(offices_id)
        updated_office_data = request.get_json(force=True)
        if {'name'} <= set(updated_office_data):
            model_result = OfficesModelDb(office_id=oid).edit_office(updated_office_data['name'])
            if 'Invalid Id' in model_result or 'Invalid Data' in model_result:
                return make_response(jsonify({"status": 400, "error": "Invalid Data ,Check id or data being updated"}),
                                     400)
            elif 'Office Exists' in model_result:
                return make_response(jsonify({"status": 409, "error": "Office with similar name exists"}), 409)
            return make_response(jsonify({"status": 200, "message": "Updated successfully"}), 200)
        return make_response(jsonify({"status": 400, "error": "Please Check All Input Fields Are Filled"}), 400)
    return make_response(jsonify({"status": 401, "error": "Unauthorized Access,Requires Admin Rights"}), 401)


@office_api_v2.route("/offices/<office_id>", methods=['GET'])
@jwt_required
def api_specific_office_get(office_id):
    oid = id_conversion(office_id)
    office = OfficesModelDb(office_id=oid).get_specific_office()
    if isinstance(office, list) and len(office) >= 1:
        response_body = {
            "id": office[0][0],
            "office_type": office[0][1],
            "office_name": office[0][2]
        }
        return make_response(jsonify({"status": 200, "data": [response_body]}), 200)
    return make_response(jsonify({"status": 404, "error": "Office Not Found"}), 404)


@office_api_v2.route("/offices/<office_id>", methods=['DELETE'])
@jwt_required
def api_specific_office_delete(office_id):
    if 'Requires Admin Privilege' not in check_user():
        oid = id_conversion(office_id)
        office = OfficesModelDb(office_id=oid).delete_office()
        if isinstance(office, list):
            return make_response(jsonify({"status": 200, "message": "{} Deleted".format(office[0][0])}), 200)
        return make_response(jsonify({"status": 404, "error": "Office Not Found"}), 404)
    return make_response(jsonify({"status": 401, "error": "Unauthorized Access,Requires Admin Rights"}), 401)
