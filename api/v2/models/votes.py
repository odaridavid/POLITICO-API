from . import Model
import psycopg2


class VoteModel(Model):

    def vote(self, office_id, candidate_id, user_id):
        query = "INSERT INTO votes(created_by,office,candidate) " \
                "VALUES(%s,%s,%s) RETURNING office,candidate,created_by;"
        data = (user_id, office_id, candidate_id)
        try:
            cursor = self.db_conn.cursor()
            cursor.execute(query, data)
            self.db_conn.commit()
            vote = cursor.fetchall()
            return vote
        except psycopg2.IntegrityError:
            return 'Vote Conflict'
