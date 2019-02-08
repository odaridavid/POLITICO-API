from flask import jsonify, make_response


def generate_response(model_result):
    if 'Doesnt Exist' in model_result:
        return make_response(jsonify({"status": 404, "error": "Data Not Found"}), 404)
    elif 'Invalid Id' in model_result:
        return make_response(jsonify({"status": 404, "error": "Invalid Id Not Found"}), 404)
