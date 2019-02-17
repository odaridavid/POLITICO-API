from . import BaseTestCase
import json


class OfficeEndpointsTestCase(BaseTestCase):
    def test_office_created_success(self):
        """
        Tests Office Created Successfully
        """
        response = self.client.post('api/v2/offices', data=json.dumps({
            "type": "Health",
            "name": "Senior Medical Staff"
        }))
        self.assertEqual(response.status_code, 201, "Office Creation should be Successful")
        self.assertEqual('Senior Medical Staff', response.json['data'][0]['name'])

    def test_office_created_exists(self):
        """ Tests No office was Duplicated """
        data = {
            "type": "Health",
            "name": "Senior Medical Staff"
        }
        self.client.post('api/v2/offices', data=json.dumps(data))
        response = self.client.post('api/v2/offices', data=json.dumps(data))
        self.assertEqual(response.status_code, 409, "Office Should Already Exists")
        self.assertEqual('Office Already Exists', response.json['error'])

    def test_created_office_with_invalid_data(self):
        """
        Tests Office with invalid data
        """
        response = self.client.post('api/v2/offices', data=json.dumps({
            "name": "r",
            "type": "yu"
        }))
        self.assertEqual(response.status_code, 400, "Should be Parsing Invalid Data ,Bad Request")
        self.assertIn('Check Input Values', response.json['error'])

    def test_create_office_with_missing_data(self):
        """
        Tests User Signed Up with missing
        """
        response = self.client.post('api/v2/offices', data=json.dumps({
            "name": "Attorney General"
        }))
        self.assertEqual(response.status_code, 400, "Should be Parsing Invalid Data ,Bad Request")
        self.assertIn('Missing Key value', response.json['error'])

    def test_get_all_offices_empty(self):
        response = self.client.get('api/v2/offices')
        self.assertEqual(response.status_code, 200, "Should be getting all offices")
        self.assertEqual(0, len(response.json['data']))

    def test_get_all_offices(self):
        self.client.post('api/v2/offices', data=json.dumps({
            "name": "Goverment Official",
            "type": "Patrol"
        }))
        self.client.post('api/v2/offices', data=json.dumps({
            "name": "Government Steward",
            "type": "Patrol"
        }))
        response = self.client.get('api/v2/offices')
        self.assertEqual(response.status_code, 200, "Should be getting all offices")
        self.assertEqual(2, len(response.json['data']))
