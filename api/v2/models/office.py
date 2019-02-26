from api.db_conn import db_connect
import psycopg2
from api.validator import OfficeValidator


class OfficesModelDb:
    """Offices Model Class"""

    def __init__(self, office=None, office_id=None):
        self.db_conn = db_connect()
        self.office = office
        self.office_id = office_id

    def create_office(self):
        """Function to create an office in db"""
        validated_office = OfficeValidator(self.office).all_checks()
        if 'Invalid' in validated_office:
            return 'Invalid Data'
        office_type = validated_office['type']
        office_name = validated_office['name']
        data = (office_type, office_name)
        query = "INSERT INTO offices (office_type,office_name) " \
                "VALUES(%s,%s);"
        try:
            cursor = self.db_conn.cursor()
            cursor.execute(query, data)
            self.db_conn.commit()
            return office_name
        except psycopg2.IntegrityError:
            return 'Office Exists'

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

    def edit_office(self, new_name):
        if isinstance(self.office_id, int):
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
                cursor.execute(query, (new_name, self.office_id,))
                self.db_conn.commit()
            except psycopg2.IntegrityError:
                return 'Office Exists'
            query = "SELECT * FROM offices WHERE _id=%s;"
            cursor.execute(query, (self.office_id,))
            row = cursor.fetchall()
            if len(row) == 0:
                return 'Invalid Id'
            return row
        return 'Invalid Id'

    def delete_office(self):
        """Deletes an office from db"""
        query = """DELETE FROM offices WHERE _id=%s RETURNING office_name;"""
        cursor = self.db_conn.cursor()
        if isinstance(self.office_id, int):
            cursor.execute(query, (self.office_id,))
            self.db_conn.commit()
            office_row = cursor.fetchall()
            if len(office_row) == 0:
                return 'Empty'
            return office_row
        return 'Invalid Id'

    def get_specific_office(self):
        """Gets a specific office provided by id"""
        query = "SELECT * FROM offices WHERE _id=%s;"
        cursor = self.db_conn.cursor()
        if isinstance(self.office_id, int):
            cursor.execute(query, (self.office_id,))
            self.db_conn.commit()
            office_row = cursor.fetchall()
            return office_row
        return 'Invalid Id'
