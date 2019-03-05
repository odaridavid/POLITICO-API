from . import Model


class PartiesModelDb(Model):

    def get_specific_party(self, party_id):
        query = "SELECT * FROM parties WHERE _id=%s;"
        cursor = self.db_conn.cursor()
        if isinstance(party_id, int):
            cursor.execute(query, (party_id,))
            self.db_conn.commit()
            office_row = cursor.fetchall()
            return office_row
        return 'Invalid Id'
