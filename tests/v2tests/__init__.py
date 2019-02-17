import unittest
# Imports create app function to set testing config
from run import app_context
# from api.db_conn import execute_drop_queries
from api.v2.models.user_model import UserModelDb
from api.db_conn import create_tables, drop_tables, close_connection


class BaseTestCase(unittest.TestCase):
    # Base Class for v2 test files
    def setUp(self):
        drop_tables()
        create_tables()
        # setup flask app instance to testing configuration environment
        self.app = app_context()
        # drop existing tables
        self.client = self.app.test_client()
        self.user = UserModelDb(
            user={"firstname": "David",
                  "lastname": "Odari",
                  "othername": "Kiribwa",
                  "email": "odari@gmail.com",
                  "phoneNumber": "0717455945",
                  "passportUrl": "www.googledrive.com/pics?v=jejfek",
                  "password": "12we3e4r",
                  "isAdmin": 'f'
                  })
        self.user_invalid = UserModelDb(
            user={"firstname": "David",
                  "lastname": "Od",
                  "othername": "Kiribwa",
                  "email": "odari@mail.com",
                  "phoneNumber": "0717455945",
                  "passportUrl": "www.googledrive.com/pics?v=jejfek",
                  "password": "12we3e4r"
                  })

    def tearDown(self):
        # execute_drop_queries()
        drop_tables()
        close_connection()
