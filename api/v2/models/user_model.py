from api.db_conn import db_connection


class UserModel:
    def __init__(self):
        # Setup connection to db
        self.db_con = db_connection()
