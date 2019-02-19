from flask import Blueprint, request, make_response, jsonify
from api.v2.models.candidate_model import CandidateModel

candidate_api_v2 = Blueprint('candidate_v2', __name__, url_prefix="/api/v2")


@candidate_api_v2.route("/office/<office_id>/register", methods=['POST'])
def api_candidate_register(office_id):
    oid = id_conversion(office_id)
    register_data = request.get_json(force=True)
    cid = id_conversion(register_data['party'])
    pid = id_conversion(register_data['candidate'])
    ids = [oid, cid, pid]
    if {'party', 'candidate'} <= set(register_data) and 'Invalid' not in ids:
        candidate_info = CandidateModel(oid, cid, pid).register_candidate()
        if isinstance(candidate_info, list):
            return make_response(
                jsonify({"status": 200, "data": [{"office": candidate_info[2], "user": candidate_info[0]}]}), 200)
        elif 'Candidate Conflict' or 'Empty' in candidate_info:
            return make_response(jsonify({"status": 400, "error": "Check Data for invalid request"}), 400)
    return make_response(jsonify({"status": 400, "error": "Missing Key value"}), 400)


def id_conversion(item_id):
    try:
        oid = int(item_id)
        return oid
    except ValueError:
        return 'Invalid'
