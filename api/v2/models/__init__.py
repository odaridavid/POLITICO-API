from api.db_conn import db_connect
import psycopg2
from api.validator import PartyValidator, OfficeValidator


def check_data(validated, res_type):
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
        data, query, name = check_data(resource, resource_type)
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
        query = ''
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

    def execute_query(self, query):
        cursor = self.db_conn.cursor()
        cursor.execute(query)
        self.db_conn.commit()
        return cursor.fetchall()
