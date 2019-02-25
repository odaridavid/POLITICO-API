from flask import jsonify, make_response
from api.v1.models.office_model import OfficesModel
from api.v1.models.party_model import PartiesModel


def generate_response(model_result):
    if 'Invalid Id' in model_result:
        return make_response(jsonify({"status": 404, "error": "Invalid Id Not Found"}), 404)
    # Fix For Delete Bug If Item Doesnt Exist- FIxes Deleting Twice
    return make_response(jsonify({"status": 404, "error": "Item Not Found"}), 404)


class Methods:
    def __init__(self, item_id, item, model_type):
        self.item_id = item_id
        self.item = item
        self.model_type = model_type

    @staticmethod
    def id_conversion(item_id):
        try:
            return int(item_id)
        except ValueError:
            # Use of Letters as ids edge case
            return {"status": 400, "error": "Invalid Id"}

    # Channel for method requests
    def method_requests(self, option):
        # Conversion of id
        oid = self.id_conversion(self.item_id)
        # Check that id is int for either patch or get or delete
        if isinstance(oid, int) and option == 1:
            # Option 1 for  and get
            return self.get(oid)
        elif isinstance(oid, int) and option == 2:
            # Option 2 for delete
            return self.delete(oid)
        elif isinstance(oid, int) and option == 0:
            # Option 0 for update
            return self.patch(oid)
        else:
            return make_response(jsonify(oid), 400)

    def patch(self, oid):
        """Method that handles update"""
        if not self.model_type == 'office':
            model_result = PartiesModel(party_id=oid).get_specific_item()
        else:
            model_result = OfficesModel(office_id=oid).get_specific_item()

        if 'Invalid Id' in model_result:
            # id == 0 or negatives edge case
            return make_response(jsonify({"status": 404, "error": "Invalid Id Not Found"}), 404)
        elif 'Doesnt Exist' in model_result or 'Error' in model_result:
            # Id greater than 0 but not found
            return make_response(jsonify({"status": 404, "error": "Item Not Found"}), 404)
        else:
            # Check keys in request and string is not null
            if {'name'} <= set(self.item) and len(self.item['name']) >= 3:
                model_result['name'] = self.item['name']
                # Success Response
                return make_response(
                    jsonify({"status": 200, "data": [{"id": self.item_id, "name": model_result['name']}]}, 200))
            return make_response(jsonify({"status": 400, "error": "Incorrect Data Received,Bad request"}), 400)

    def get(self, oid):
        """Gets specific item depending on model type variable"""
        model_result = self.model_result_get_specific(oid)
        if isinstance(model_result, dict):
            # Checks keys for party
            if {'id', 'name', 'hqAddress', 'logoUrl'} <= set(model_result):
                return make_response(jsonify({"status": 200, "data": [model_result]}), 200)
            # Checks Keys for office
            elif {'id', 'type', 'name'} <= set(model_result):
                return make_response(jsonify({"status": 200, "data": [model_result]}), 200)
        return generate_response(model_result)

    def delete(self, oid):
        """Delete item method"""
        if self.model_type == 'office':
            # Delete Party
            model_result = OfficesModel(office_id=oid).remove_item()
        else:
            # Delete Office
            model_result = PartiesModel(party_id=oid).remove_item()
        if model_result is None:
            return make_response(
                jsonify({"status": 200, "message": "Deleted Successfully"}), 200)
        return generate_response(model_result)

    def model_result_get_specific(self, oid):
        """Method that gets a specific item whether office or party depending on passed type"""
        if self.model_type == 'office':
            model_result = OfficesModel(office_id=oid).get_specific_item()
        else:
            model_result = PartiesModel(party_id=oid).get_specific_item()
        return model_result
