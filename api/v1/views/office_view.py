from flask import Blueprint, request, jsonify, make_response
from api.v1.models.office_model import OfficesModel
from . import generate_response, Methods

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


@office_api.route("/offices/<office_id>", methods=['GET', 'DELETE'])
def api_specific_office(office_id):
    # Pass in office id and option to distinguish between other requests in the method
    return method_requests(office_id, 1, None)


@office_api.route("/offices/<offices_id>/name", methods=['PATCH'])
def api_edit_office(offices_id):
    # Get Json Request Data
    updated_office_data = request.get_json(force=True)
    # Pass in office id and office data to be used
    return method_requests(offices_id, None, updated_office_data)


def office_id_conversion(offices_id):
    try:
        # Convert in try except and return an id
        oid = int(offices_id)
        return oid
    except ValueError:
        # Use of Letters as ids edge case
        return make_response(jsonify({"status": 400, "error": "Invalid Office Id"}), 400)


# Channel for method requests
def method_requests(office_id, option, office):
    # Conversion of id
    oid = office_id_conversion(office_id)
    # Check that id is int for either patch or get or delete
    if isinstance(oid, int):
        if option == 1 and office is None:
            # Option 1 for delete and get
            return delete_and_get(oid)
        # Update Office
        return Methods(OfficesModel, oid, office, 'office').patch()
    return oid


def delete_and_get(oid):
    if not request.method == 'DELETE':
        model_result = OfficesModel(office_id=oid).get_specific_item()
        # Checks Keys Exist
        if {'id', 'type', 'name'} <= set(model_result):
            return make_response(jsonify({"status": 200, "data": [model_result]}), 200)
        return make_response(jsonify({"status": 404, "error": "Office Does Not Exist"}), 404)
    # Delete
    model_result = OfficesModel(office_id=oid).remove_item()
    if model_result is None:
        return make_response(
            jsonify({"status": 200, "message": "Deleted Successfully"}), 200)
    return generate_response(model_result)
