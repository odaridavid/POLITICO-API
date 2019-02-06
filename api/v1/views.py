from flask import Blueprint, request, jsonify, make_response
from .models import PartiesModel
from .models import OfficesModel

# flask blueprint is a way for you to organize your flask application into smaller and re-usable application
version_1 = Blueprint('apiv1', __name__, url_prefix="/api/v1")


@version_1.route("/parties", methods=['POST'])
def api_create_party():
    """
    Creates a  party on parties endpoint with POST response
    :return: response depending on post request data
    """
    # get the party as json and save it in the model
    party = request.get_json(force=True)  # Ignore the mimetype and always try to parse JSON.
    # Checks keys exist in given dict
    if {'name', 'hqAddress', 'logoUrl'} <= set(party):
        # Create Party Model instance and add Party to list
        gen_id = PartiesModel(party).create_political_party()
        if gen_id:
            # successful response
            data = {
                "status": 201,
                "data": [{
                    "id": gen_id,
                    "name": party['name']
                }]
            }
            return make_response(jsonify(data), 400)
    else:
        # Missing data bad request response
        # Fail response
        data = {
            "status": 400,
            "error": "400 ERROR:BAD REQUEST,Missing Key value"
        }
        return make_response(jsonify(data), 400)


@version_1.route("/offices", methods=['POST'])
def api_create_office():
    """
    Creates an office on  endpoint with POST response
    :return: response depending on post request data
    """
    # get the office as json and save it in the model
    office = request.get_json(force=True)
    # Checks keys exist in given dict as sets
    if {'type', 'name'} <= set(office):
        # Create Office Model instance and add Party to list
        gen_id = OfficesModel(office).create_government_office()
        if gen_id:
            # successful response
            data = {
                "status": 201,
                "data": [{
                    "id": gen_id,
                    "type": office['type'],
                    "name": office['name']
                }]
            }
            return make_response(jsonify(data), 400)
    else:
        # Missing data bad request response
        # Fail response
        data = {
            "status": 400,
            "error": "400 ERROR:BAD REQUEST,Missing Key value"
        }
        return make_response(jsonify(data), 400)
