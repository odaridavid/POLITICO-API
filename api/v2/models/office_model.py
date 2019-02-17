from api.db_conn import db_connect
import psycopg2
from api.validator import OfficeValidator


class OfficesModelDb:
    """Offices Model Class"""

    def __init__(self, office=None):
        # Setup connection to db
        self.db_conn = db_connect()
        # Office object being worked on
        self.office = office

    def create_office(self):
        validated_office = OfficeValidator(self.office).all_checks()
        if 'Invalid' in validated_office:
            return 'Invalid Data'
        office_type = validated_office['type']
        office_name = validated_office['name']
        # Add Office to table
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
        query = "SELECT * from offices"
        cursor = self.db_conn.cursor()
        cursor.execute(query)
        self.db_conn.commit()
        rows = cursor.fetchall()
        return rows
