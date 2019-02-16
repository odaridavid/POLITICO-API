import unittest
# Imports create app function to set testing config
from run import app
from api.db_conn import execute_creates_queries, execute_drop_queries
from api.v2.models.user_model import UserModel


class BaseTestCase(unittest.TestCase):
    # Base Class for v2 test files
    def setUp(self):
        # setup flask app instance to testing configuration environment
        app.config['TESTING'] = True
        execute_creates_queries()
        self.app = app
        self.client = self.app.test_client()
        self.user = UserModel(
            user={
                "firstname": "David",
                "lastname": "Odari",
                "othername": "Kiribwa",
                "email": "odari@mail.com",
                "phoneNumber": "0717455945",
                "passportUrl": "www.googledrive.com/pics?v=jejfek",
                "password": "12we3e4r"
            })
        self.user_invalid = UserModel(
            user={
                "firstname": "David",
                "lastname": "Od",
                "othername": "Kiribwa",
                "email": "odari@mail.com",
                "phoneNumber": "0717455945",
                "passportUrl": "www.googledrive.com/pics?v=jejfek",
                "password": "12we3e4r"
            })

    def tearDown(self):
        execute_drop_queries()
