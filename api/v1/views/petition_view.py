from flask import Blueprint, request, jsonify, make_response
from api.v1.models.petition_model import PetitionModel

petition_api = Blueprint('petition_v1', __name__, url_prefix="/api/v1")


@petition_api.route("/petitions", methods=['POST'])
def api_petitions():
    petition = request.get_json(force=True)
    # Make Sure Keys Exist
    if {"createdBy", "office", "body"} <= set(petition):
        # Validation
        validated_petition = PetitionModel(petition=petition).create_petition()
        if 'Invalid Operation' in validated_petition:
            return make_response(jsonify({"status": 400, "error": "Parsing Invalid Data ,Bad Request"}), 400)
        return make_response(
            jsonify(
                {
                    "status": 201,
                    "data": [validated_petition]
                }), 201)
    return make_response(jsonify({"status": 400, "error": "Invalid Request ,Missing Data"}), 400)
