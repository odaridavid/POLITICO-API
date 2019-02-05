import unittest
# Imports create app function to set testing config
from api import create_app
from .test_parties_endpoint import PartiesEndpointsTestCase
from .test_offices_endpoint import OfficeEndpointsTestCase


class BaseTestCase(unittest.TestCase):
    # Base Class for all test files
    def setUp(self):
        # setup flask app instance to testing configuration environment
        self.app = create_app(config='testing')
        self.client = self.app.test_client(self)
        # for modularisation and code reuse
        self.office = {
            'id': 1234567890,
            'type': 'Senior',
            'name': 'Permanent Secretary'
        }
        self.party = {
            'id': 1234567890,
            'name': 'Pinnacle Party',
            'hqAddress': 'Nairobi,Kenya 00100',
            'logoUrl': 'https://www.some.url.co.ke'
        }


if __name__ == '__main__':
    unittest.main()
    # Political Parties Test Cases
    parties = PartiesEndpointsTestCase()
    parties.test_create_political_party()
    parties.test_create_political_party_bad_request()
    parties.test_delete_political_party()
    parties.test_delete_political_party_not_found()
    parties.test_edit_political_party()
    parties.test_edit_political_party_bad_request()
    parties.test_view_all_political_parties()
    parties.test_view_all_political_parties_bad_request()
    parties.test_view_political_party()
    parties.test_view_political_party_not_found()
    # Government Ofice Test Cases
    offices = OfficeEndpointsTestCase()
    offices.test_create_office()
    offices.test_create_office_bad_request()
    offices.test_view_all_offices()
    offices.test_view_all_offices_bad_request()
    offices.test_view_specific_office()
    offices.test_view_specific_office_not_found()
