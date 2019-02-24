from api.db_conn import db_connect
import psycopg2
from api.validator import PartyValidator


class PartiesModelDb:
    """Parties Model Class"""

    def __init__(self, party=None, party_id=None):
        # Setup connection to db
        self.db_conn = db_connect()
        # Party  object being worked on
        self.party = party
        self.party_id = party_id

    def create_party(self):
        """Function to create a party in db"""
        # Passed to validator
        validated_party = PartyValidator(self.party).all_checks()
        if 'Invalid' in validated_party:
            return 'Invalid Data'
        party_name = validated_party['name']
        party_address = validated_party['hqAddress']
        party_url = validated_party['logoUrl']
        # Add Office to table
        data = (party_name, party_address, party_url)
        query = "INSERT INTO parties (party_name,hq_address,logo_url) " \
                "VALUES(%s,%s,%s);"
        try:
            cursor = self.db_conn.cursor()
            cursor.execute(query, data)
            self.db_conn.commit()
            return party_name
        except psycopg2.IntegrityError:
            return 'Party Exists'

    def get_all_parties(self):
        query = "SELECT * from parties;"
        cursor = self.db_conn.cursor()
        cursor.execute(query)
        self.db_conn.commit()
        # Result of tables in list as tuples
        rows = cursor.fetchall()
        results = []
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

    def edit_party(self, new_name):
        if isinstance(self.party_id, int):
            query = "UPDATE parties SET party_name = %s WHERE _id = %s;"
            cursor = self.db_conn.cursor()
            if len(new_name) < 4 or isinstance(new_name, str) is False:
                return 'Invalid Data'
            try:
                query_check = "SELECT * FROM parties WHERE party_name=%s;"
                cursor.execute(query_check, (new_name,))
                self.db_conn.commit()
                row = cursor.fetchall()
                if len(row) > 0:
                    return 'Party Exists'
                cursor.execute(query, (new_name, self.party_id,))
                self.db_conn.commit()
            except psycopg2.IntegrityError:
                return 'Party Exists'
            query = "SELECT * FROM parties WHERE _id=%s;"
            cursor.execute(query, (self.party_id,))
            party_row = cursor.fetchall()
            return party_row
        return 'Invalid Id'

    def delete_party(self):
        """Deletes a party from db"""
        query = """DELETE FROM parties WHERE _id=%s RETURNING party_name;"""
        cursor = self.db_conn.cursor()
        if isinstance(self.party_id, int):
            cursor.execute(query, (self.party_id,))
            self.db_conn.commit()
            office_row = cursor.fetchall()
            if len(office_row) == 0:
                return 'Empty'
            return office_row
        return 'Invalid Id'

    def get_specific_party(self):
        """Gets a specific party provided by id"""
        query = "SELECT * FROM parties WHERE _id=%s;"
        cursor = self.db_conn.cursor()
        if isinstance(self.party_id, int):
            cursor.execute(query, (self.party_id,))
            self.db_conn.commit()
            office_row = cursor.fetchall()
            return office_row
        return 'Invalid Id'
