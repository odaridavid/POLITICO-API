import unittest
# Imports create app function to set testing config
from run import app


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

    def tearDown(self):
        # Reset Data Structs
        parties_resp = self.client.get('api/v1/parties')
        parties_resp.json['data'].clear()


if __name__ == '__main__':
    unittest.main()
