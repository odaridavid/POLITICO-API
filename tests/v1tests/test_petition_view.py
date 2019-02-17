from tests.v1tests import BaseTestCase
from run import app_context
import json


class PetitionEndpointsTestCase(BaseTestCase):
    def setUp(self):
        self.petition = {
            "createdBy": 1,
            "office": 2,
            "body": "This is a petition Against x for the seat yhis is a petition Against x for the seat yhis is a "
                    "petition Against x for the seat yhis is a petition Against x for the seat yhis is a petition "
                    "Against x for the seat yhis is a petition Against x for the seat yhis is a petition Against x "
                    "for the seat this is a petition Against x for the seat y "
        }

        self.petition_invalid_key = {
            "createdBy": 1,
            "office": 2
        }
        self.petition_invalid = {
            "createdBy": 1,
            "office": 2,
            "body": "P"
        }
        self.client = app_context().test_client()

    def test_petition_created_successfully(self):
        """
        Tests Petition Created Successfully
        """
        response = self.client.post('api/v1/petitions', data=json.dumps(self.petition))
        self.assertEqual(response.status_code, 201)
        self.assertTrue(len(response.json['data'][0]['body']) > 0)

    def test_petition_creation_unsuccessful(self):
        """
        Tests Petition Creation Unsuccessful
        """
        response = self.client.post('api/v1/petitions', data=json.dumps(self.petition_invalid_key))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], "Invalid Request ,Missing Data")

    def test_petition_invalidated(self):
        """
        Tests
        """
        response = self.client.post('api/v1/petitions', data=json.dumps(self.petition_invalid))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], "Parsing Invalid Data ,Bad Request")
