from api.db_conn import db_connect
import psycopg2


class CandidateModel:
    def __init__(self, office_id=0, candidate_id=0, party_id=0):
        self.db_conn = db_connect()
        self.candidate_id = candidate_id
        self.office_id = office_id
        self.party_id = party_id

    def register_candidate(self):
        """Function to register a candidate"""
        query = "INSERT INTO candidates(office,party,candidate) " \
                "VALUES(%s,%s,%s) RETURNING candidate,party,office;"
        data = (self.office_id, self.candidate_id, self.party_id)
        try:
            cursor = self.db_conn.cursor()
            cursor.execute(query, data)
            self.db_conn.commit()
            candidate = cursor.fetchall()
            candidate_id = candidate[0][0]
            party_id = candidate[0][1]
            office_id = candidate[0][2]
            select_query_user = "SELECT users.firstname FROM users WHERE users._id=%s"
            select_query_party = "SELECT parties.party_name FROM parties WHERE parties._id=%s"
            select_query_office = "SELECT offices.office_name FROM offices WHERE offices._id=%s"
            cursor.execute(select_query_user, (candidate_id,))
            self.db_conn.commit()
            candidate_name = cursor.fetchall()
            cursor.execute(select_query_party, (party_id,))
            self.db_conn.commit()
            party_name = cursor.fetchall()
            cursor.execute(select_query_office, (office_id,))
            self.db_conn.commit()
            office_name = cursor.fetchall()
            return [candidate_name[0][0], party_name[0][0], office_name[0][0]]
        except psycopg2.IntegrityError:
            # Deals with non existent data on primary tables or existent conflicting data
            return 'Candidate Conflict'
