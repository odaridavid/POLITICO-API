import unittest
# Imports create app function to set testing config
from run import app
from api import models


class BaseTestCase(unittest.TestCase):
    # Base Class for all test files
    def setUp(self):
        # setup flask app instance to testing configuration environment
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        # for modularisation and code reuse
        self.office = {
            'type': 'Senior',
            'name': 'Permanent Secretary'
        }
        self.party = {
            "name": "Pinnacle Party",
            "hqAddress": "Nairobi,Kenya 00100",
            "logoUrl": "https://www.some.url.co.ke"
        }
        self.error_not_found = {
            "error": "404 ERROR:REQUESTED DATA NOT FOUND",
            "status": 404
        }
        self.invalid_id_json = {
            "status": 404,
            "error": "Invalid Id Not Found"
        }

    def tearDown(self):
        # Reset Data Structs after tests back to empty lists
        models.offices = []
        models.parties = []


if __name__ == '__main__':
    unittest.main()
