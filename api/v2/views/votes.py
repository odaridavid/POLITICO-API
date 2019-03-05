from flask import Blueprint, request, make_response, jsonify
from api.v2.models.votes import VoteModel
from flask_jwt_extended import jwt_required
from . import id_conversion

votes_api_v2 = Blueprint('votes_v2', __name__, url_prefix="/api/v2")


@votes_api_v2.route("/votes/", methods=['POST'])
@jwt_required
def api_cast_vote():
    vote_data = request.get_json(force=True)
    if {'office', 'candidate', 'voter'} <= set(vote_data):
        uid = id_conversion(vote_data['voter'])
        oid = id_conversion(vote_data['office'])
        cid = id_conversion(vote_data['candidate'])
        if 'Invalid' not in [uid, oid, cid]:
            vote_info = VoteModel().vote(oid, cid, uid)
            if not isinstance(vote_info, list):
                return make_response(
                    jsonify({"status": 409, "error": "Vote Already Cast or Voting for non existent entities"}), 409)
            return make_response(
                jsonify(
                    {
                        "status": 201,
                        "data": [{
                            "office": vote_info[0][0],
                            "candidate": vote_info[0][1],
                            "voter": vote_info[0][2]
                        }]}), 201)
        return make_response(jsonify({"status": 400, "error": "Invalid Credentials on Vote Request"}), 400)
    return make_response(jsonify({"status": 400, "error": "Missing Vote Information"}), 400)
