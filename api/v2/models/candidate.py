import psycopg2
from . import Model


class CandidateModel(Model):

    def register_candidate(self, office_id, candidate_id, party_id):
        """Function to register a candidate"""
        query = "INSERT INTO candidates(office,party,candidate) " \
                "VALUES(%s,%s,%s) RETURNING _id;"
        data = (office_id, candidate_id, party_id)
        try:
            cursor = self.db_conn.cursor()
            cursor.execute(query, data)
            candidate_id = cursor.fetchone()[0]
            self.db_conn.commit()
            select_query = "SELECT offices.office_name, parties.party_name, users.firstname " \
                           "FROM candidates " \
                           "INNER JOIN offices ON candidates.office=offices._id " \
                           "INNER JOIN parties ON candidates.party=parties._id " \
                           "INNER JOIN users ON candidates.candidate=users._id" \
                           " WHERE candidates._id=%s; "
            cursor.execute(select_query, (candidate_id,))
            self.db_conn.commit()
            candidate_registered = cursor.fetchall()
            if len(candidate_registered) == 0:
                return 'Empty'
            return candidate_registered
        except psycopg2.IntegrityError:
            return 'Candidate Conflict'

    def get_all_candidates_by_office(self, office_id):
        select_query = "SELECT offices.office_name, parties.party_name, users.firstname " \
                       "FROM candidates " \
                       "INNER JOIN offices ON candidates.office=offices._id " \
                       "INNER JOIN parties ON candidates.party=parties._id " \
                       "INNER JOIN users ON candidates.candidate=users._id" \
                       " WHERE office = %s;"
        cursor = self.db_conn.cursor()
        cursor.execute(select_query, (office_id,))
        self.db_conn.commit()
        return cursor.fetchall()
