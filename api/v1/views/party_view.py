from flask import Blueprint, request, jsonify, make_response
from . import generate_response
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
    party = request.get_json(force=True)
    try:
        pid = int(party_id)
        # Get Current Party Name
        model_result = PartiesModel(party_id=pid).get_specific_political_party_name()
        if 'Invalid Id' in model_result:
            # id == 0 or negatives edge case
            return make_response(jsonify({"status": 404, "error": "Invalid Political Party ,Id Not Found"}), 404)
        elif 'Doesnt Exist' in model_result:
            # Id greater than 0 but not found
            return make_response(jsonify({"status": 404, "error": "Political Party Not Found"}), 404)
        # Check key in request and string has value
        if {'name'} <= set(party) and len(party['name']) >= 3:
            model_result = party['name']
            # Success
            return make_response(jsonify({"status": 200, "data": [{"id": pid, "name": model_result}]}, 200))
        return make_response(jsonify({"status": 400, "error": "Incorrect Data Received,Bad request"}), 400)
    except ValueError:
        # Letters as ids edge case
        return make_response(jsonify({"status": 400, "error": "Invalid Party Id"}), 400)


@party_api.route("/parties/<party_id>", methods=['GET', 'DELETE'])
def api_specific_party(party_id):
    try:
        pid = int(party_id)
        if not request.method == 'DELETE':
            return req_worker_get(pid)
        model_result = PartiesModel(party_id=pid).remove_item()
        if model_result is None:
            return make_response(
                jsonify({"status": 200, "message": "Deleted Successfully"}), 200)
        return generate_response(model_result)
    except ValueError:
        return make_response(jsonify({"status": 400, "error": "Invalid Party Id"}), 400)


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


def req_worker_get(party_id):
    # Pass Through Model to get specific item
    model_result = PartiesModel(party_id=int(party_id)).get_specific_item()
    #  Check keys
    if {'id', 'name', 'hqAddress', 'logoUrl'} <= set(model_result):
        return make_response(jsonify({"status": 200, "data": [model_result]}), 200)
    return generate_response(model_result)
