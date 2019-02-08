from flask import Blueprint, request, jsonify, make_response
from . import generate_response
from api.v1.models.party_model import PartiesModel

party_api = Blueprint('party_v1', __name__, url_prefix="/api/v1")


@party_api.route("/parties", methods=['GET', 'POST'])
def api_parties():
    if request.method == 'POST':
        # get the party data as json
        party = request.get_json(force=True)
        # Checks keys exist in given dict
        if {'name', 'hqAddress', 'logoUrl'} <= set(party):
            # Create Party Model instance and add Party to list
            gen_id = PartiesModel(party).create_political_party()
            response_body = {"status": 201, "data": [{"id": gen_id, "name": party['name']}]}
            # Successful
            return make_response(jsonify(response_body), 201)
        return make_response(jsonify({"status": 400, "error": "Bad Request: Missing Data Values"}), 400)

    elif request.method == 'GET':
        # Get List Items from model
        parties = PartiesModel().get_all_items_in_list()
        if len(parties) >= 0:
            # If parties list has no items or does should be  Successful
            return make_response(jsonify({"status": 200, "data": parties}), 200)
        # Unsuccessful No Such data or not found
        return make_response(jsonify({"status": 404, "error": "Data Not Found"}), 404)


@party_api.route("/parties/<party_id>/name", methods=['PATCH'])
def api_edit_party(party_id):
    model_result = PartiesModel(party_id=int(party_id)).get_specific_political_party_name()
    if 'Doesnt Exist' in model_result:
        return make_response(jsonify({"status": 404, "error": "Political Party Not Found"}), 404)

    # Get Json Request Data
    party = request.get_json(force=True)
    # Change Name
    if {'name'} <= set(party):
        model_result = party['name']
        return make_response(jsonify({"status": 200, "data": [{"id": party_id, "name": model_result}]}, 200))
    return make_response(jsonify({"status": 400, "error": "Incorrect Data Received,Bad request"}), 400)


@party_api.route("/parties/<party_id>", methods=['GET', 'DELETE'])
def api_specific_party(party_id):
    if request.method == 'GET':
        model_result = PartiesModel(party_id=int(party_id)).get_specific_item()
        if {'id', 'name', 'hqAddress', 'logoUrl'} <= set(model_result):
            return make_response(jsonify({"status": 200, "data": [model_result]}), 200)
        return generate_response(model_result)
    elif request.method == 'DELETE':
        model_result = PartiesModel(party_id=int(party_id)).remove_item()
        if model_result is None:
            return make_response(
                jsonify({"status": 200, "message": "Deleted Successfully"}), 200)
        return generate_response(model_result)
