from . import Model
import psycopg2


class PartiesModelDb(Model):

    def get_all_parties(self):
        query = "SELECT * from parties;"
        cursor = self.db_conn.cursor()
        cursor.execute(query)
        self.db_conn.commit()
        # Result of tables in list as tuples
        rows = cursor.fetchall()
        results = []
        for row in rows:
            _id = row[0]
            name = row[1]
            hq_address = row[2]
            logo_url = row[3]
            party = {
                "id": _id,
                "name": name,
                "hqAddress": hq_address,
                "logoUrl": logo_url
            }
            results.append(party)
        return results

    def edit_party(self, new_name, party_id):
        if isinstance(party_id, int):
            query = "UPDATE parties SET party_name = %s WHERE _id = %s;"
            cursor = self.db_conn.cursor()
            if len(new_name) < 4 or isinstance(new_name, str) is False:
                return 'Invalid Data'
            try:
                query_check = "SELECT * FROM parties WHERE party_name=%s;"
                cursor.execute(query_check, (new_name,))
                self.db_conn.commit()
                row = cursor.fetchall()
                if len(row) > 0:
                    return 'Party Exists'
                cursor.execute(query, (new_name, party_id,))
                self.db_conn.commit()
            except psycopg2.IntegrityError:
                return 'Party Exists'
            query = "SELECT * FROM parties WHERE _id=%s;"
            cursor.execute(query, (party_id,))
            party_row = cursor.fetchall()
            return party_row
        return 'Invalid Id'

    def delete_party(self, party_id):
        query = """DELETE FROM parties WHERE _id=%s RETURNING party_name;"""
        cursor = self.db_conn.cursor()
        if isinstance(party_id, int):
            cursor.execute(query, (party_id,))
            self.db_conn.commit()
            office_row = cursor.fetchall()
            if len(office_row) == 0:
                return 'Empty'
            return office_row
        return 'Invalid Id'

    def get_specific_party(self, party_id):
        query = "SELECT * FROM parties WHERE _id=%s;"
        cursor = self.db_conn.cursor()
        if isinstance(party_id, int):
            cursor.execute(query, (party_id,))
            self.db_conn.commit()
            office_row = cursor.fetchall()
            return office_row
        return 'Invalid Id'
