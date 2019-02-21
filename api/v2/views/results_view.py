from flask import Blueprint, request, jsonify, make_response
from api.v2.models.results_model import ResultsModel

result_api_v2 = Blueprint('results_v2', __name__, url_prefix="/api/v2")


@result_api_v2.route("/office/<office_id>/result", methods=['GET'])
def api_results(office_id):
    oid = id_conversion(office_id)
    if isinstance(oid, int):
        results = ResultsModel(oid).get_results()
    else:
        return make_response(jsonify({"status": 404, "error": "Invalid Office Id"}), 404)

    if isinstance(results, list):
        return make_response(jsonify({"status": 200, "data": [{
            "office": oid,
            "candidate": results[0][0],
            "results": results[0][1]
        }]}), 200)
    elif 'Empty' in results:
        return make_response(jsonify({"status": 404, "error": "Results Not Found"}), 404)
    return make_response(jsonify({"status": 404, "error": "Results Not Found"}), 404)


def id_conversion(item_id):
    try:
        oid = int(item_id)
        return oid
    except ValueError:
        return 'Invalid'
