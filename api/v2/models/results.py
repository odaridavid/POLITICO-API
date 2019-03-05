from . import Model


class ResultsModel(Model):

    def get_results(self, office_id):
        query = """SELECT candidate,COUNT(*) FROM votes WHERE office = %s GROUP BY candidate ;"""
        cursor = self.db_conn.cursor()
        cursor.execute(query, (office_id,))
        self.db_conn.commit()
        tally = cursor.fetchall()
        if len(tally) < 1:
            return 'Empty'
        return tally
