from api.db_conn import db_connect
import psycopg2


class VoteModel:
    def __init__(self, office_id=0, candidate_id=0, user_id=0):
        self.db_conn = db_connect()
        self.candidate_id = candidate_id
        self.office_id = office_id
        self.user_id = user_id

    def vote(self):
        """Function to vote for a candidate once"""
        query = "INSERT INTO votes(created_by,office,candidate) " \
                "VALUES(%s,%s,%s) RETURNING office,candidate,created_by;"
        data = (self.user_id, self.office_id, self.candidate_id)
        try:
            cursor = self.db_conn.cursor()
            cursor.execute(query, data)
            self.db_conn.commit()
            vote = cursor.fetchall()
            return vote
        except psycopg2.IntegrityError:
            return 'Vote Conflict'
