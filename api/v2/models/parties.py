from . import Model


class PartiesModelDb(Model):

    def delete_party(self, party_id):
        query = """DELETE FROM parties WHERE _id=%s RETURNING party_name;"""
        cursor = self.db_conn.cursor()
        if isinstance(party_id, int):
            cursor.execute(query, (party_id,))
            self.db_conn.commit()
            office_row = cursor.fetchall()
            if len(office_row) == 0:
                return 'Empty'
            return office_row
        return 'Invalid Id'

    def get_specific_party(self, party_id):
        query = "SELECT * FROM parties WHERE _id=%s;"
        cursor = self.db_conn.cursor()
        if isinstance(party_id, int):
            cursor.execute(query, (party_id,))
            self.db_conn.commit()
            office_row = cursor.fetchall()
            return office_row
        return 'Invalid Id'
