from flask import make_response, jsonify


class Responses:
    def __init__(self, model_result):
        self.model_result = model_result

    def generate_response(self):
        if 'Doesnt Exist' in self.model_result:
            return make_response(jsonify({"status": 404, "error": "Data Not Found"}), 404)
        elif 'Invalid Id' in self.model_result:
            return make_response(jsonify({"status": 404, "error": "Invalid Id Not Found"}), 404)
        else:
            response_body = {
                "status": 200,
                "data": [self.model_result]
            }
        return make_response(jsonify(response_body), 200)
