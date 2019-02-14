from flask import Blueprint, request, jsonify, make_response
from api.v1.models.office_model import OfficesModel
from . import Methods

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
            if not isinstance(gen_id, int):
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
    # If parties list has no items or does  Successful
    return make_response(jsonify({"status": 200, "data": offices}), 200)


@office_api.route("/offices/<office_id>", methods=['GET'])
def api_specific_office_get(office_id):
    # Pass in office id and option to distinguish between other requests in the method
    return Methods(office_id, None, 'office').method_requests(1)


@office_api.route("/offices/<offices_id>/name", methods=['PATCH'])
def api_edit_office(offices_id):
    # Get Json Request Data
    updated_office_data = request.get_json(force=True)
    # Pass in office id and office data to be used
    return Methods(offices_id, updated_office_data, 'office').method_requests(0)


@office_api.route("/offices/<office_id>", methods=['DELETE'])
def api_specific_office_delete(office_id):
    # Pass in office id and option to distinguish between other requests in the method
    return Methods(office_id, None, 'office').method_requests(2)
