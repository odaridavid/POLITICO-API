from api.db_conn import db_connect
import psycopg2


class ResultsModel:
    def __init__(self, office_id):
        self.office_id = office_id
        self.db_conn = db_connect()

    def get_results(self):
        query = """SELECT office,candidate,COUNT(candidate) FROM votes WHERE office=%s"""
        cursor = self.db_conn.cursor()
        cursor.execute(query, (self.office_id,))
        self.db_conn.commit()
        row = cursor.fetchall()
        return row
