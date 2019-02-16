import unittest
# Imports create app function to set testing config
from run import app
from api.db_conn import execute_creates_queries, execute_drop_queries


class BaseTestCase(unittest.TestCase):
    # Base Class for v2 test files
    def setUp(self):
        # setup flask app instance to testing configuration environment
        app.config['TESTING'] = True
        execute_creates_queries()
        self.app = app
        self.client = self.app.test_client()

    def tearDown(self):
        execute_drop_queries()
