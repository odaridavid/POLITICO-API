from flask import Blueprint, request, jsonify, make_response
from . import generate_response, Methods
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
    return method_requests(party_id, None, updated_party_data)


@party_api.route("/parties/<party_id>", methods=['GET', 'DELETE'])
def api_specific_party(party_id):
    return method_requests(party_id, 1, party=None)


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


def party_id_conversions(party_id):
    try:
        # conversion of id
        pid = int(party_id)
        return pid
    except ValueError:
        # Use of Letters as ids edge case
        return make_response(jsonify({"status": 400, "error": "Invalid Party Id"}), 400)


def method_requests(party_id, option, party):
    pid = party_id_conversions(party_id)
    if isinstance(pid, int):
        if option == 1 and party is None:
            # Option 1 for delete and get
            return delete_and_get(pid)
        # Update Party
        return Methods(PartiesModel, pid, party, 'party').patch()
    return pid


def delete_and_get(pid):
    if not request.method == 'DELETE':
        # Pass Through Model to get specific item
        model_result = PartiesModel(party_id=int(pid)).get_specific_item()
        #  Check keys
        if {'id', 'name', 'hqAddress', 'logoUrl'} <= set(model_result):
            return make_response(jsonify({"status": 200, "data": [model_result]}), 200)
        return generate_response(model_result)
    # Delete
    model_result = PartiesModel(party_id=pid).remove_item()
    if model_result is None:
        return make_response(
            jsonify({"status": 200, "message": "Deleted Successfully"}), 200)
    return generate_response(model_result)
