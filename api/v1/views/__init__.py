from flask import jsonify, make_response


def generate_response(model_result):
    if 'Invalid Id' in model_result:
        return make_response(jsonify({"status": 404, "error": "Invalid Id Not Found"}), 404)
    # Fix For Delete Bug If Item Doesnt Exist- FIxes Deleting Twice
    return make_response(jsonify({"status": 404, "error": "Item Not Found"}), 404)


class Methods:
    def __init__(self, model, item_id, item, model_type):
        self.model = model
        self.item_id = item_id
        self.item = item
        self.model_type = model_type

    def patch(self):
        if not self.model_type == 'office':
            model_result = self.model(party_id=self.item_id).get_specific_item()
        else:
            model_result = self.model(office_id=self.item_id).get_specific_item()
        if 'Invalid Id' in model_result:
            # id == 0 or negatives edge case
            return make_response(jsonify({"status": 404, "error": "Invalid Id Not Found"}), 404)
        elif 'Doesnt Exist' in model_result:
            # Id greater than 0 but not found
            return make_response(jsonify({"status": 404, "error": "Item Not Found"}), 404)
        # Check keys in request and string is not null
        if {'name'} <= set(self.item) and len(self.item['name']) >= 3:
            model_result['name'] = self.item['name']
            # Success Response
            return make_response(
                jsonify({"status": 200, "data": [{"id": self.item_id, "name": model_result['name']}]}, 200))
        return make_response(jsonify({"status": 400, "error": "Incorrect Data Received,Bad request"}), 400)
