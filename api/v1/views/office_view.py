from flask import Blueprint, request, jsonify, make_response
from . import generate_response
from api.v1.models.office_model import OfficesModel

# flask blueprint is a way for you to organize your flask application into smaller and re-usable application
office_api = Blueprint('office_v1', __name__, url_prefix="/api/v1")


@office_api.route("/offices", methods=['GET', 'POST'])
def api_office():
    if not request.method == 'GET':
        # get the office as json
        office = request.get_json(force=True)
        # Checks keys exist in given dict as sets
        if {'type', 'name'} <= set(office):
            # add office to model which returns generated id
            gen_id = OfficesModel(office).create_government_office()
            if not type(gen_id) == int:
                # Invalid Data
                return make_response(jsonify({"status": 403, "error": "Check Input Values"}), 403)
            response_body = {
                "status": 201,
                "data": [{
                    "id": gen_id,
                    "type": office['type'],
                    "name": office['name']
                }]
            }
            # Successful
            return make_response(jsonify(response_body), 201)
        # Missing Keys
        return make_response(jsonify({"status": 400, "error": "Missing Key value"}), 400)

    offices = OfficesModel().get_all_items_in_list()
    if len(offices) >= 0:
        # If parties list has no items or does  Successful
        return make_response(jsonify({"status": 200, "data": offices}), 200)


@office_api.route("/offices/<office_id>", methods=['GET'])
def api_specific_office(office_id):
    try:
        oid = int(office_id)
        model_result = OfficesModel(office_id=oid).get_specific_item()
        # Checks Keys Exist
        if {'id', 'type', 'name'} <= set(model_result):
            return make_response(jsonify({"status": 200, "data": [model_result]}), 200)
        return make_response(jsonify({"status": 404, "error": "Office Does Not Exist"}), 404)
    except ValueError:
        return make_response(jsonify({"status": 400, "error": "Invalid Office Id"}), 400)
