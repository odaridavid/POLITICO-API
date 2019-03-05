from api.db_conn import db_connect
import psycopg2
from api.validator import PartyValidator, OfficeValidator, CheckStrings


def check_insert_data(validated, res_type):
    if 'Invalid' in validated:
        return '', '', 'Invalid Data'
    if 'party' not in res_type:
        office_type = validated['type']
        office_name = validated['name']
        data = (office_type, office_name)
        query = "INSERT INTO offices (office_type,office_name) " \
                "VALUES(%s,%s);"
        return data, query, office_name
    party_name = validated['name']
    party_address = validated['hqAddress']
    party_url = validated['logoUrl']
    # Add Office to table
    data = (party_name, party_address, party_url)
    query = "INSERT INTO parties (party_name,hq_address,logo_url) " \
            "VALUES(%s,%s,%s);"
    return data, query, party_name


def check_edit_data(new_name):
    validated_name = CheckStrings(new_name).check_strings()
    if 'Invalid' in validated_name:
        return 'Invalid Data'
    return validated_name


def edit_queries(res_type):
    if 'party' not in res_type:
        query = "UPDATE offices SET office_name = %s WHERE _id = %s;"
        query_check = "SELECT * FROM offices WHERE office_name=%s;"
        confirm_query = "SELECT * FROM offices WHERE _id=%s;"
        return query, query_check, confirm_query
    query = "UPDATE parties SET party_name = %s WHERE _id = %s;"
    query_check = "SELECT * FROM parties WHERE party_name=%s;"
    confirm_query = "SELECT * FROM parties WHERE _id=%s;"
    return query, query_check, confirm_query


class Model(object):
    def __init__(self):
        self.db_conn = db_connect()

    def create_resource(self, resource_type, resource):
        if 'party' not in resource_type:
            validated = OfficeValidator(resource).all_checks()
        else:
            validated = PartyValidator(resource).all_checks()
        return self.insert_data(validated, resource_type)

    def insert_data(self, resource, resource_type):
        data, query, name = check_insert_data(resource, resource_type)
        try:
            if len(data) > 0:
                cursor = self.db_conn.cursor()
                cursor.execute(query, data)
                self.db_conn.commit()
                return name
            return name
        except psycopg2.IntegrityError:
            if 'office' not in resource_type:
                return 'Party Exists'
            return 'Office Exists'

    def get_resource(self, resource_type):
        results = []
        if 'party' not in resource_type:
            query = "SELECT * from offices;"
            rows = self.execute_query(query)
            for row in rows:
                _id = row[0]
                office_type = row[1]
                office_name = row[2]
                office = {
                    "id": _id,
                    "type": office_type,
                    "name": office_name
                }
                results.append(office)
        else:
            query = "SELECT * from parties;"
            rows = self.execute_query(query)
            for row in rows:
                _id = row[0]
                name = row[1]
                hq_address = row[2]
                logo_url = row[3]
                party = {
                    "id": _id,
                    "name": name,
                    "hqAddress": hq_address,
                    "logoUrl": logo_url
                }
                results.append(party)
        return results

    def edit_resource(self, resource_type, new_name, resource_id):
        if isinstance(resource_id, int):
            validated = check_edit_data(new_name)
            if 'Invalid Data' in validated:
                return 'Invalid Data'
            if 'party' not in resource_type:
                return self.edit_query_body('office', validated, new_name, resource_id)
            else:
                return self.edit_query_body('party', validated, new_name, resource_id)

        return 'Invalid Id'

    def edit_query_body(self, res_type, validated, new_name, resource_id):
        try:
            query, query_check, confirm_query = edit_queries(res_type)
            check = self.select_resource_type(res_type, query_check, validated)
            if 'Office Exists' in check or 'Party Exists' in check:
                if 'office' in res_type:
                    return 'Office Exists'
                return 'Party Exists'
            self.execute_edit_query(query, new_name, resource_id)
        except psycopg2.IntegrityError:
            if 'office' in res_type:
                return 'Office Exists'
            return 'Party Exists'
        return self.execute_check_with_db(confirm_query, resource_id)

    def execute_query(self, query):
        cursor = self.db_conn.cursor()
        cursor.execute(query)
        self.db_conn.commit()
        return cursor.fetchall()

    def select_resource_type(self, res_type, query_check, new_name):
        if 'office' in res_type:
            resource_placeholder = 'Office'
        else:
            resource_placeholder = 'Party'
        return self.check_exists(resource_placeholder, query_check, new_name)

    def check_exists(self, placeholder, query_check, new_name):
        cursor = self.db_conn.cursor()
        cursor.execute(query_check, (new_name,))
        self.db_conn.commit()
        row = cursor.fetchall()
        if len(row) > 0:
            return '{} Exists'.format(placeholder)
        return 'Doesnt Exist'

    def execute_edit_query(self, query, new_name, resource_id):
        cursor = self.db_conn.cursor()
        self.db_conn.commit()
        cursor.execute(query, (new_name, resource_id,))
        self.db_conn.commit()

    def execute_check_with_db(self, query, resource_id):
        cursor = self.db_conn.cursor()
        cursor.execute(query, (resource_id,))
        row = cursor.fetchall()
        if len(row) == 0:
            return 'Invalid Id'
        return row
