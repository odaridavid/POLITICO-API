from . import BaseTestCase
import json


class OfficeEndpointsTestCase(BaseTestCase):

    def test_create_office(self):
        """Tests valid data POST Http method request on /offices endpoint"""
        # Post, uses office specification model
        response = self.client.post('api/v1/offices', data=json.dumps(self.office))
        # Data section returned as per response specification
        expected_response_json = {
            'data': [{
                'id': 1,
                'type': 'Senior',
                'name': 'Permanent Secretary'
            }],
            'status': 201
        }
        self.assertEqual(response.status_code, 201, "Should Return a 201 HTTP Status Code Response:Created")
        self.assertEqual(expected_response_json, response.json)

    def test_create_office_invalid_forbidden(self):
        """Tests invalid data on POST method request on /offices endpoint"""
        response = self.client.post('api/v1/offices',
                                    json={
                                        'type': 'n',
                                        'name': 'p'
                                    })
        self.assertEqual(response.status_code, 403, "Should Return a 400 HTTP Status Code Response:Bad Request")
        # Should return error message
        self.assertIn("Check Input Values", response.json['error'])

    def test_create_office_bad_request(self):
        """Tests malformed POST Http method request on /offices endpoint"""
        response = self.client.post('api/v1/offices',
                                    json={
                                        # Missing type key
                                        'name': 'Permanent Secretary'
                                    })
        self.assertEqual(response.status_code, 400, "Should Return a 400 HTTP Status Code Response:Bad Request")
        # Should return error message
        self.assertIn("Missing Key value", response.json['error'])

    def test_view_all_offices(self):
        """Tests GET Http method request on /offices endpoint"""
        # Post, create an office first
        self.client.post('api/v1/offices', data=json.dumps(self.office))
        # Retrieve the office
        response = self.client.get('api/v1/offices')
        self.assertEqual(response.status_code, 200, "Should Return a 200 HTTP Status Code Response:Success")
        expected_response_json = {
            "data": [{
                "id": 1,
                'type': 'Senior',
                'name': 'Permanent Secretary'
            }],
            "status": 200
        }
        # Converts to string
        self.assertEqual(response.json, expected_response_json)

    def test_view_all_offices_bad_request(self):
        """Tests malformed GET Http method request on /office endpoint"""
        response = self.client.get('api/v1/ofices')
        self.assertEqual(response.status_code, 404, "Should Return a 404 HTTP Status Code Response:Resource Not Found")
        # Should return error message
        self.assertEqual(response.json, self.error_default_not_found)

    def test_view_specific_office(self):
        """Tests GET Http method request on /office/{:id} endpoint"""
        # Post, add an office
        self.client.post('api/v1/offices', data=json.dumps(self.office))
        # Get data for specific office
        response = self.client.get('api/v1/offices/1')
        expected_response = {
            "id": 1,
            "name": "Permanent Secretary",
            "type": "Senior"
        }
        self.assertEqual(response.status_code, 200, "Should Return a 200 HTTP Status Code:Success")
        # Returns Dict as string and compares if its in response
        self.assertEqual(response.json['data'][0], expected_response)

    def test_view_specific_office_invalid_id(self):
        """Tests malformed GET Http method request on /office/{:id} endpoint"""
        response = self.client.get('api/v1/offices/{}'.format(4578))
        self.assertEqual(response.status_code, 404, "Should Return a 404 HTTP Status Code Response:Bad Request")
        # Should return error message
        self.assertEqual(response.json['error'], "Invalid Id Not Found", "Should return resource not found response")

    def test_view_specific_office_not_found(self):
        """Tests malformed GET Http method request on /office/{:id} endpoint"""
        response = self.client.get('api/v1/offies/{}'.format(0))
        self.assertEqual(response.status_code, 404, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json, self.error_default_not_found, "Should return resource not found response")

    def test_view_specific_office_invalid_id_value_error(self):
        """Tests valid request but invalid data on DELETE request on /parties/{:id}/name endpoint"""
        self.client.post('api/v1/offices', data=json.dumps(self.office))
        response = self.client.get('api/v1/offices/e')
        self.assertEqual(response.status_code, 400, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json['error'], 'Invalid Id',
                         'Should return not found response')

    def test_edit_government_office(self):
        """Tests PATCH Http method request on /offices/{:id}/name endpoint"""
        # Save Post First
        self.client.post('api/v1/offices', data=json.dumps(self.office))
        edit_request_json = {
            "name": "Secretary General"
        }
        # Update Name
        response = self.client.patch('api/v1/offices/{}/name'.format(1),
                                     data=json.dumps(edit_request_json))
        self.assertEqual(response.status_code, 200, "Should Return a 200 HTTP Status Code Response:Updated")
        self.assertEqual(edit_request_json.get('name'), response.json[0]['data'][0]['name'])

    def test_edit_office_invalid_id(self):
        """Tests invalid id on PATCH request on /offices/{:id}/name endpoint"""
        edit_request_json = {
            "name": "Secretary General"
        }
        response = self.client.patch('api/v1/offices/0/name', data=json.dumps(edit_request_json))
        self.assertEqual(response.status_code, 404, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json['error'], 'Invalid Id Not Found',
                         'Should return invalid id response')

    def test_edit_offices_not_found(self):
        """Tests valid but non existent id on PATCH request on /parties/{:id}/name endpoint"""
        edit_request_json = {
            "name": "Secretary"
        }
        response = self.client.patch('api/v1/offices/3/name', data=json.dumps(edit_request_json))
        self.assertEqual(response.status_code, 404, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json['error'], 'Invalid Id Not Found',
                         'Should return not found response')

    def test_edit_office_invalid_data(self):
        """Tests valid request but invalid data on PATCH request on /offices/{:id}/name endpoint"""
        self.client.post('api/v1/offices', data=json.dumps(self.office))
        edit_request_json = {
            "name": "D"
        }
        response = self.client.patch('api/v1/offices/1/name', data=json.dumps(edit_request_json))
        self.assertEqual(response.status_code, 400, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json['error'], 'Incorrect Data Received,Bad request',
                         'Should return not found response')

    def test_edit_office_invalid_id_value_error(self):
        """Tests valid request but invalid data on PATCH request on /offices/{:id}/name endpoint"""
        self.client.post('api/v1/offices', data=json.dumps(self.office))
        edit_request_json = {
            "name": "Secretary General"
        }
        response = self.client.patch('api/v1/offices/e/name', data=json.dumps(edit_request_json))
        self.assertEqual(response.status_code, 400, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json['error'], 'Invalid Id',
                         'Should return not found response')

    def test_delete_office(self):
        """Tests DELETE Http method request on /offices/{:id} endpoint"""
        # Save Post First
        self.client.post('api/v1/offices', data=json.dumps(self.office))
        # Delete Party
        response = self.client.delete('api/v1/offices/{0}'.format(1))
        self.assertEqual(response.status_code, 200, "Should Return a 200 HTTP Status Code Response:Deleted")
        self.assertEqual("Deleted Successfully", response.json['message'])

    def test_delete_office_not_found(self):
        """"Tests malformed DELETE Http method request on /offices/{:id} endpoint"""
        # Save Post First
        response = self.client.delete('api/v1/offices/{0}'.format(-1))
        self.assertEqual(response.status_code, 404, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json['error'], 'Invalid Id Not Found', "Should return resource not found response")

    def test_delete_office_invalid_id_value_error(self):
        """Tests valid request but invalid data on DELETE request on /offices/{:id}/name endpoint"""
        self.client.post('api/v1/offices', data=json.dumps(self.party))
        response = self.client.delete('api/v1/offices/e')
        self.assertEqual(response.status_code, 400, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json['error'], 'Invalid Id')
