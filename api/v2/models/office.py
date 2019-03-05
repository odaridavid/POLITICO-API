import psycopg2
from api.validator import CheckStrings
from . import Model


class OfficesModelDb(Model):

    def delete_office(self, office_id):
        query = """DELETE FROM offices WHERE _id=%s RETURNING office_name;"""
        cursor = self.db_conn.cursor()
        if isinstance(office_id, int):
            cursor.execute(query, (office_id,))
            self.db_conn.commit()
            office_row = cursor.fetchall()
            if len(office_row) == 0:
                return 'Empty'
            return office_row
        return 'Invalid Id'

    def get_specific_office(self, office_id):
        query = "SELECT * FROM offices WHERE _id=%s;"
        cursor = self.db_conn.cursor()
        if isinstance(office_id, int):
            cursor.execute(query, (office_id,))
            self.db_conn.commit()
            office_row = cursor.fetchall()
            return office_row
        return 'Invalid Id'
