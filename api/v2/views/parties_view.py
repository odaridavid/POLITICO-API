from flask import Blueprint, request, jsonify, make_response
from api.v2.models.parties_model import PartiesModelDb

parties_api_v2 = Blueprint('parties_v2', __name__, url_prefix="/api/v2")


@parties_api_v2.route("/parties", methods=['POST'])
def api_create_parties():
    party = request.get_json(force=True)
    if {'name', 'hqAddress', 'logoUrl'} <= set(party):
        party_name = PartiesModelDb(party).create_party()
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
    return make_response(jsonify({"status": 400, "error": "Missing Key value"}), 400)


@parties_api_v2.route("/parties", methods=['GET'])
def api_get_parties():
    parties = PartiesModelDb().get_all_parties()
    return make_response(jsonify({"status": 200, "data": parties}), 200)


@parties_api_v2.route("/parties/<party_id>/name", methods=['PATCH'])
def api_edit_party(party_id):
    oid = id_conversion(party_id)
    updated_party_data = request.get_json(force=True)
    if {'name'} <= set(updated_party_data):
        model_result = PartiesModelDb(party_id=oid).edit_party(updated_party_data['name'])
        if 'Invalid Id' in model_result or 'Invalid Data' in model_result:
            return make_response(jsonify({"status": 400, "error": "Invalid Data ,Check id or data being updated"}), 400)
        elif 'Party Exists' in model_result:
            return make_response(jsonify({"status": 409, "error": "Party with similar name exists"}), 409)
        return make_response(jsonify({"status": 200, "message": "{} Updated successfully".format(model_result[0][1])}),
                             200)
    return make_response(jsonify({"status": 400, "error": "Missing Key value"}), 400)


@parties_api_v2.route("/parties/<party_id>", methods=['GET'])
def api_specific_office_get(party_id):
    oid = id_conversion(party_id)
    party = PartiesModelDb(party_id=oid).get_specific_party()
    if isinstance(party, list) and len(party) >= 1:
        response_body = {
            "id": party[0][0],
            "name": party[0][1],
            "hqAddress": party[0][2],
            "logoUrl": party[0][3],
        }
        return make_response(jsonify({"status": 200, "data": [response_body]}), 200)
    return make_response(jsonify({"status": 404, "error": "Data Not Found"}), 404)


@parties_api_v2.route("/parties/<party_id>", methods=['DELETE'])
def api_specific_office_delete(party_id):
    oid = id_conversion(party_id)
    party = PartiesModelDb(party_id=oid).delete_party()
    if isinstance(party, list):
        return make_response(jsonify({"status": 200, "message": "{} Deleted".format(party[0][0])}), 200)
    return make_response(jsonify({"status": 404, "error": "Data Not Found"}), 404)


def id_conversion(item_id):
    try:
        oid = int(item_id)
        return oid
    except ValueError:
        return 'Invalid'
