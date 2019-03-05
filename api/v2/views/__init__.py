from flask_jwt_extended import get_jwt_identity
from api.v2.models.user import UserModelDb
from api.v2.models.office import OfficesModelDb
from api.v2.models.parties import PartiesModelDb
from flask import jsonify, make_response


def check_user():
    current_user = get_jwt_identity()
    return UserModelDb().get_user_by_id(current_user)


def id_conversion(item_id):
    try:
        oid = int(item_id)
        return oid
    except ValueError:
        return 'Invalid'


def check_created_resource(db_output, resource_type):
    """Validation Checks for values and existence and responses """
    if 'Invalid Data' in db_output:
        return make_response(jsonify({"status": 400, "error": "Check Input Values"}), 400)
    elif 'party' not in resource_type and 'Office Exists' in db_output:
        return make_response(jsonify({"status": 409, "error": "Office Already Exists"}), 409)
    elif 'office' not in resource_type and 'Party Exists' in db_output:
        return make_response(jsonify({"status": 409, "error": "Party Already Exists"}), 409)
    return db_output


def response(db_output):
    """Build Response for resource"""
    if isinstance(db_output, str) and 'Unauthorized' in db_output:
        return make_response(jsonify({"status": 401, "error": "Unauthorized Access,Requires Admin Rights"}), 401)
    if isinstance(db_output, str) and 'Missing Key' in db_output:
        return make_response(jsonify({"status": 400, "error": "Please Check All Input Fields Are Filled"}), 400)
    elif not isinstance(db_output, str):
        return db_output
    response_body = {
        "status": 201,
        "data": [{
            "name": db_output
        }]
    }
    return make_response(jsonify(response_body), 201)


def resource_handler(resource_type, resource):
    """Chooses method to use based on resource type"""
    db_output = ViewMethods(resource_type, resource).create_resource()
    return response(db_output)


class ViewMethods:
    def __init__(self, resource_type, resource):
        self.resource_type = resource_type
        self.resource = resource

    def create_resource(self):
        if 'Requires Admin Privilege' not in check_user():
            db_output = ''
            if 'party' not in self.resource_type and {'type', 'name'} <= set(self.resource):
                db_output = OfficesModelDb().create_resource(self.resource_type, self.resource)
            elif {'name', 'hqAddress', 'logoUrl'} <= set(self.resource):
                db_output = PartiesModelDb().create_resource(self.resource_type, self.resource)
            else:
                return 'Missing Key'
            return check_created_resource(db_output, self.resource_type)
        return 'Unauthorized'
