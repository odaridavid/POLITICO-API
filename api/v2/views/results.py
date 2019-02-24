from flask import Blueprint, jsonify, make_response
from api.v2.models.results import ResultsModel
from flask_jwt_extended import jwt_required
from . import id_conversion

result_api_v2 = Blueprint('results_v2', __name__, url_prefix="/api/v2")


@result_api_v2.route("/office/<office_id>/result", methods=['GET'])
@jwt_required
def api_results(office_id):
    oid = id_conversion(office_id)
    if not isinstance(oid, int):
        return make_response(jsonify({"status": 400, "error": "Invalid Office Id"}), 400)
    results = ResultsModel(oid).get_results()
    if not isinstance(results, list):
        return make_response(jsonify({"status": 404, "error": "Results Not Found"}), 404)
    return make_response(jsonify({"status": 200,
                                  "data": [{
                                      "office": oid,
                                      "candidate": results[0][0],
                                      "results": results[0][1]
                                  }]}), 200)
