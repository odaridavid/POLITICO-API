import psycopg2
from api.validator import OfficeValidator
from . import Model


class OfficesModelDb(Model):

    def get_all_offices(self):
        query = "SELECT * from offices;"
        cursor = self.db_conn.cursor()
        cursor.execute(query)
        self.db_conn.commit()
        rows = cursor.fetchall()
        results = []
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
        return results

    def edit_office(self, new_name, office_id):
        if isinstance(office_id, int):
            query = "UPDATE offices SET office_name = %s WHERE _id = %s;"
            cursor = self.db_conn.cursor()
            if len(new_name) < 4 or isinstance(new_name, str) is False:
                return 'Invalid Data'
            try:
                query_check = "SELECT * FROM offices WHERE office_name=%s;"
                cursor.execute(query_check, (new_name,))
                self.db_conn.commit()
                row = cursor.fetchall()
                if len(row) > 0:
                    return 'Office Exists'
                cursor.execute(query, (new_name, office_id,))
                self.db_conn.commit()
            except psycopg2.IntegrityError:
                return 'Office Exists'
            query = "SELECT * FROM offices WHERE _id=%s;"
            cursor.execute(query, (office_id,))
            row = cursor.fetchall()
            if len(row) == 0:
                return 'Invalid Id'
            return row
        return 'Invalid Id'

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
