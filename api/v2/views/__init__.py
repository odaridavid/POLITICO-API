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
    if 'Invalid Data' in db_output:
        return make_response(jsonify({"status": 400, "error": "Check Input Values"}), 400)
    elif 'party' not in resource_type and 'Office Exists' in db_output:
        return make_response(jsonify({"status": 409, "error": "Office Already Exists"}), 409)
    elif 'office' not in resource_type and 'Party Exists' in db_output:
        return make_response(jsonify({"status": 409, "error": "Party Already Exists"}), 409)
    return db_output


class ViewMethods:
    def __init__(self, resource_type, resource):
        self.resource_type = resource_type
        self.resource = resource

    def create_resource(self):
        if 'Requires Admin Privilege' not in check_user():
            db_output = ''
            if 'party' not in self.resource_type and {'type', 'name'} <= set(self.resource):
                db_output = OfficesModelDb().create_office(self.resource)
            elif {'name', 'hqAddress', 'logoUrl'} <= set(self.resource):
                db_output = PartiesModelDb().create_party(self.resource)
            else:
                return 'Missing Key'
            return check_created_resource(db_output, self.resource_type)
        return 'Unauthorized'
