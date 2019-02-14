from flask import Blueprint, request, jsonify, make_response
from . import Methods
from api.v1.models.party_model import PartiesModel

party_api = Blueprint('party_v1', __name__, url_prefix="/api/v1")


@party_api.route("/parties", methods=['GET', 'POST'])
def api_parties():
    if not request.method == 'GET':
        return req_worker_post()
    # Get List Items from model
    parties = PartiesModel().get_all_items_in_list()
    # If parties list has no items or does should be  Successful
    return make_response(jsonify({"status": 200, "data": parties}), 200)


@party_api.route("/parties/<party_id>/name", methods=['PATCH'])
def api_edit_party(party_id):
    # Get Json Request Data
    updated_party_data = request.get_json(force=True)
    return Methods(party_id, updated_party_data, 'party').method_requests(0)


@party_api.route("/parties/<party_id>", methods=['GET'])
def api_specific_party_get(party_id):
    return Methods(party_id, None, 'party').method_requests(1)


@party_api.route("/parties/<party_id>", methods=['DELETE'])
def api_specific_party_delete(party_id):
    return Methods(party_id, None, 'party').method_requests(2)


def req_worker_post():
    party = request.get_json(force=True)
    # Checks keys exist in given dict
    if {'name', 'hqAddress', 'logoUrl'} <= set(party):
        # Create Party Model instance and add Party to list
        gen_id = PartiesModel(party).create_political_party()
        if not isinstance(gen_id, int):
            # Invalid Data
            return make_response(jsonify({"status": 403, "error": "Check Input Values"}), 403)
        response_body = {"status": 201, "data": [{"id": gen_id, "name": party['name']}]}
        # Successful
        return make_response(jsonify(response_body), 201)
    return make_response(jsonify({"status": 400, "error": "Bad Request: Missing Data Values"}), 400)
