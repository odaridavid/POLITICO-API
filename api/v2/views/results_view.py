from flask import Blueprint, request, jsonify, make_response
from api.v2.models.results_model import ResultsModel

result_api_v2 = Blueprint('results_v2', __name__, url_prefix="/api/v2")


@result_api_v2.route("/office/<office_id>/result", methods=['GET'])
def api_results(office_id):
    oid = id_conversion(office_id)
    results = ResultsModel(oid).get_results()


def id_conversion(item_id):
    try:
        oid = int(item_id)
        return oid
    except ValueError:
        return 'Invalid'

