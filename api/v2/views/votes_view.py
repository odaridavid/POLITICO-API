from flask import Blueprint, request, make_response, jsonify
from api.v2.models.votes_model import VoteModel

votes_api_v2 = Blueprint('votes_v2', __name__, url_prefix="/api/v2")


@votes_api_v2.route("/votes/", methods=['POST'])
def api_candidate_register():
    register_data = request.get_json(force=True)
    uid = id_conversion(register_data['user'])
    oid = id_conversion(register_data['office'])
    cid = id_conversion(register_data['candidate'])
    if {'party', 'candidate'} <= set(register_data) and 'Invalid' not in [oid, cid, uid]:
        vote_info = VoteModel(oid, cid, uid).vote()
        if isinstance(vote_info, list):
            return make_response(
                jsonify(
                    {
                        "status": 200,
                        "data": [{
                            "office": vote_info[0],
                            "candidate": vote_info[1],
                            "voter": vote_info[2]
                        }]}), 200)
        elif 'Vote Conflict' in vote_info:
            return make_response(jsonify({"status": 400, "error": "Check Data for invalid request"}), 400)
        else:
            return make_response(jsonify({"status": 400, "error": "Bad Request made on voting"}), 400)
    return make_response(jsonify({"status": 400, "error": "Missing Key value"}), 400)


def id_conversion(item_id):
    try:
        oid = int(item_id)
        return oid
    except ValueError:
        return 'Invalid'
