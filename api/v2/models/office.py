from . import Model


class OfficesModelDb(Model):

    def get_specific_office(self, office_id):
        query = "SELECT * FROM offices WHERE _id=%s;"
        cursor = self.db_conn.cursor()
        if isinstance(office_id, int):
            cursor.execute(query, (office_id,))
            self.db_conn.commit()
            office_row = cursor.fetchall()
            return office_row
        return 'Invalid Id'
