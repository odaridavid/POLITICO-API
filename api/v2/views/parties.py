from flask import Blueprint, request, jsonify, make_response
from api.v2.models.parties import PartiesModelDb
from flask_jwt_extended import jwt_required
from . import check_user, id_conversion

parties_api_v2 = Blueprint('parties_v2', __name__, url_prefix="/api/v2")


@parties_api_v2.route("/parties", methods=['POST'])
@jwt_required
def api_create_parties():
    if 'Requires Admin Privilege' not in check_user():
        party = request.get_json(force=True)
        if {'name', 'hqAddress', 'logoUrl'} <= set(party):
            party_name = PartiesModelDb().create_party(party)
            if 'Party Exists' in party_name:
                return make_response(jsonify({"status": 409, "error": "Party Already Exists"}), 409)
            elif 'Invalid Data' in party_name:
                return make_response(jsonify({"status": 400, "error": "Check Input Values"}), 400)

            response_body = {
                "status": 201,
                "data": [{
                    "name": party_name
                }]
            }
            return make_response(jsonify(response_body), 201)
        return make_response(jsonify({"status": 400, "error": "Please Check All Input Fields Are Filled"}), 400)
    return make_response(jsonify({"status": 401, "error": "Unauthorized Access,Requires Admin Rights"}), 401)


@parties_api_v2.route("/parties", methods=['GET'])
@jwt_required
def api_get_parties():
    parties = PartiesModelDb().get_all_parties()
    return make_response(jsonify({"status": 200, "data": parties}), 200)


@parties_api_v2.route("/parties/<party_id>/name", methods=['PATCH'])
@jwt_required
def api_edit_party(party_id):
    if 'Requires Admin Privilege' not in check_user():
        oid = id_conversion(party_id)
        updated_party_data = request.get_json(force=True)
        if {'name'} <= set(updated_party_data):
            model_result = PartiesModelDb().edit_party(updated_party_data['name'], party_id=oid)
            if 'Invalid Id' in model_result or 'Invalid Data' in model_result:
                return make_response(jsonify({"status": 400, "error": "Invalid Data ,Check id or data being updated"}),
                                     400)
            elif 'Party Exists' in model_result:
                return make_response(jsonify({"status": 409, "error": "Party with similar name exists"}), 409)
            return make_response(
                jsonify({"status": 200, "message": "{} Updated Successfully".format(model_result[0][1])}),
                200)
        return make_response(jsonify({"status": 400, "error": "Please Check All Input Fields Are Filled"}), 400)
    return make_response(jsonify({"status": 401, "error": "Unauthorized Access,Requires Admin Rights"}), 401)


@parties_api_v2.route("/parties/<party_id>", methods=['GET'])
@jwt_required
def api_specific_party_get(party_id):
    oid = id_conversion(party_id)
    party = PartiesModelDb().get_specific_party(party_id=oid)
    if isinstance(party, list) and len(party) >= 1:
        print(party)
        response_body = {
            "id": party[0][0],
            "name": party[0][1],
            "hqAddress": party[0][2],
            "logoUrl": party[0][3]
        }
        return make_response(jsonify({"status": 200, "data": [response_body]}), 200)
    return make_response(jsonify({"status": 404, "error": "Party Not Found"}), 404)


@parties_api_v2.route("/parties/<party_id>", methods=['DELETE'])
@jwt_required
def api_specific_party_delete(party_id):
    if 'Requires Admin Privilege' not in check_user():
        oid = id_conversion(party_id)
        party = PartiesModelDb().delete_party(party_id=oid)
        if isinstance(party, list):
            return make_response(jsonify({"status": 200, "message": "{} Deleted".format(party[0][0])}), 200)
        return make_response(jsonify({"status": 404, "error": "Party Not Found"}), 404)
    return make_response(jsonify({"status": 401, "error": "Unauthorized Access,Requires Admin Rights"}), 401)
