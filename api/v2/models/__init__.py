from api.db_conn import db_connect


class Model(object):
    def __init__(self):
        self.db_conn = db_connect()
