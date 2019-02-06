from flask import Blueprint, request, jsonify, make_response
from .models import PartiesModel
from .models import OfficesModel

# flask blueprint is a way for you to organize your flask application into smaller and re-usable application
version_1 = Blueprint('apiv1', __name__, url_prefix="/api/v1")


@version_1.route("/parties", methods=['GET', 'POST'])
def api_parties():
    if request.method == 'POST':
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
                response_body = {
                    "status": 201,
                    "data": [{
                        "id": gen_id,
                        "name": party['name']
                    }]
                }
                # Successful
                return make_response(jsonify(response_body), 201)
        else:
            # Missing data bad request response
            # Fail response
            response_body = {
                "status": 400,
                "error": "400 ERROR:BAD REQUEST,Missing Key value"
            }
            # Fail
            return make_response(jsonify(response_body), 400)
    elif request.method == 'GET':
        """Handles Get request"""
        parties = PartiesModel().get_all_political_parties()
        if len(parties) >= 0:
            # If parties list has no items or does
            response_body = {
                "status": 200,
                "data": parties
            }
            # Successful
            return make_response(jsonify(response_body), 200)
        else:
            response_body = {
                "status": 404,
                "error": "404 ERROR:DATA NOT FOUND"
            }
            # Unsuccessful
            return make_response(jsonify(response_body), 404)


@version_1.route("/offices", methods=['GET', 'POST'])
def api_create_office():
    if request.method == 'POST':
        """
        Creates an office on /offices  endpoint with POST response
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
        else:
            # Missing data bad request response
            # Fail response
            response_body = {
                "status": 400,
                "error": "400 ERROR:BAD REQUEST,Missing Key value"
            }
            # Unsuccessful
            return make_response(jsonify(response_body), 400)
    elif request.method == 'GET':
        offices = OfficesModel().get_all_government_offices()
        if len(offices) >= 0:
            # If parties list has no items or does
            response_body = {
                "status": 200,
                "data": offices
            }
            # Successful
            return make_response(jsonify(response_body), 200)

        return make_response(jsonify({"status": 404, "error": "404 ERROR:DATA NOT FOUND"}), 404)
