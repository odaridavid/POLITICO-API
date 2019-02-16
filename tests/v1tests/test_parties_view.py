from tests.v1tests import BaseTestCase
import json


class PartiesEndpointsTestCase(BaseTestCase):

    def test_create_political_party(self):
        """Tests valid data on  POST  request on /parties endpoint"""
        # Post, uses party specification model
        response = self.client.post(path='/api/v1/parties', data=json.dumps(self.party))
        expected_data_json = {
            'data': [{
                'id': 1,
                'name': 'Pinnacle Party'
            }],
            "status": 201
        }
        self.assertEqual(response.status_code, 201, "Should Return a 201 HTTP Status Code Response")
        self.assertEqual(expected_data_json, response.json)

    def test_create_office_invalid_forbidden(self):
        """Tests invalid data on POST method request on /parties endpoint"""
        response = self.client.post('api/v1/parties',
                                    json={
                                        'name': 'p',
                                        'hqAddress': 'n',
                                        'logoUrl': 'n'
                                    })
        self.assertEqual(response.status_code, 403, "Should Return a 400 HTTP Status Code Response:Bad Request")
        # Should return error message
        self.assertIn("Check Input Values", response.json['error'])

    def test_create_political_party_bad_request(self):
        """Tests malformed POST Http method request on /parties endpoint"""
        response = self.client.post('api/v1/parties',
                                    json={
                                        # Missing hq address and logo url
                                        'name': 'Pinnacle Party'
                                    })
        self.assertEqual(response.status_code, 400, "Should Return a 400 HTTP Status Code Response:Bad Request")
        # Should return error message
        self.assertIn("Bad Request", response.json['error'], "Should return bad request missing data response")

    def test_edit_political_party(self):
        """Tests PATCH Http method request on /parties/{:id}/name endpoint"""
        # Save Post First
        self.client.post('api/v1/parties', data=json.dumps(self.party))
        edit_request_json = {
            "name": "Dynamo Party"
        }
        # Update Name
        response = self.client.patch('api/v1/parties/{}/name'.format(1),
                                     data=json.dumps(edit_request_json))
        self.assertEqual(response.status_code, 200, "Should Return a 200 HTTP Status Code Response:Updated")
        self.assertEqual(edit_request_json.get('name'), response.json[0]['data'][0]['name'])

    def test_edit_political_party_invalid_id(self):
        """Tests invalid id on PATCH request on /parties/{:id}/name endpoint"""
        edit_request_json = {
            "name": "Dynamo Party"
        }
        response = self.client.patch('api/v1/parties/0/name', data=json.dumps(edit_request_json))
        self.assertEqual(response.status_code, 404, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json['error'], 'Invalid Id Not Found',
                         'Should return invalid id response')

    def test_edit_political_party_not_found(self):
        """Tests valid but non existent id on PATCH request on /parties/{:id}/name endpoint"""
        edit_request_json = {
            "name": "Dynamo Party"
        }
        response = self.client.patch('api/v1/parties/3/name', data=json.dumps(edit_request_json))
        self.assertEqual(response.status_code, 404, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json['error'], 'Invalid Id Not Found',
                         'Should return not found response')

    def test_edit_political_party_invalid_data(self):
        """Tests valid request but invalid data on PATCH request on /parties/{:id}/name endpoint"""
        self.client.post('api/v1/parties', data=json.dumps(self.party))
        edit_request_json = {
            "name": "D"
        }
        response = self.client.patch('api/v1/parties/1/name', data=json.dumps(edit_request_json))
        self.assertEqual(response.status_code, 400, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json['error'], 'Incorrect Data Received,Bad request',
                         'Should return not found response')

    def test_edit_political_party_invalid_id_value_error(self):
        """Tests valid request but invalid data on PATCH request on /parties/{:id}/name endpoint"""
        self.client.post('api/v1/parties', data=json.dumps(self.party))
        edit_request_json = {
            "name": "Dynamo Party"
        }
        response = self.client.patch('api/v1/parties/e/name', data=json.dumps(edit_request_json))
        self.assertEqual(response.status_code, 400, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json['error'], 'Invalid Id',
                         'Should return not found response')

    def test_delete_political_party(self):
        """Tests DELETE Http method request on /parties/{:id} endpoint"""
        # Save Post First
        self.client.post('api/v1/parties', data=json.dumps(self.party))
        # Delete Party
        response = self.client.delete('api/v1/parties/1')
        self.assertEqual(response.status_code, 200, "Should Return a 200 HTTP Status Code Response:Deleted")
        self.assertEqual("Deleted Successfully", response.json['message'])

    def test_delete_political_party_twice(self):
        """Tests DELETE Http method request on /parties/{:id} endpoint twice"""
        # Save Post First
        self.client.post('api/v1/parties', data=json.dumps(self.party))
        # Delete Party Twice
        self.client.delete('api/v1/parties/1')
        response = self.client.delete('api/v1/parties/1')
        self.assertEqual(response.status_code, 404)
        self.assertEqual("Item Not Found", response.json['error'])

    def test_delete_political_party_not_found(self):
        """"Tests malformed DELETE Http method request on /parties/{:id} endpoint invalid negative id"""
        # Save Post First
        response = self.client.delete('api/v1/parties/{0}'.format(-2))
        self.assertEqual(response.status_code, 404, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json['error'], 'Invalid Id Not Found', "Should return resource not found response")

    def test_delete_political_party_invalid_id_value_error(self):
        """Tests valid request but invalid data on DELETE request on /parties/{:id}/name endpoint"""
        self.client.post('api/v1/parties', data=json.dumps(self.party))
        response = self.client.delete('api/v1/parties/e')
        self.assertEqual(response.status_code, 400, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json['error'], 'Invalid Id',
                         'Should return not found response')

    def test_view_political_party(self):
        """Tests GET Http method request on /parties/{:id} endpoint"""
        # Create Party First
        self.client.post('api/v1/parties', data=json.dumps(self.party), content_type="application/json")
        # Get data for specific party
        response = self.client.get('api/v1/parties/1')
        expected_response = {
            "id": 1,
            "name": "Pinnacle Party",
            "hqAddress": "Nairobi,Kenya 00100",
            "logoUrl": "https://www.some.url.co.ke"
        }
        self.assertEqual(response.status_code, 200, "Should Return a 200 HTTP Status Code:Success")
        # Returns Dict as string and compares if its in response
        self.assertEqual(expected_response, response.json['data'][0])

    def test_view_political_party_invalid_id(self):
        """Tests malformed GET Http method request on /parties/{:id} endpoint"""
        response = self.client.get('api/v1/parties/{}'.format(0))
        self.assertEqual(response.status_code, 404, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(self.invalid_id_json, response.json, "Should return resource not found response")

    def test_view_political_party_invalid_id_value_error(self):
        """Tests valid request but invalid data on DELETE request on /parties/{:id}/name endpoint"""
        self.client.post('api/v1/parties', data=json.dumps(self.party))
        response = self.client.get('api/v1/parties/e')
        self.assertEqual(response.status_code, 400, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json['error'], 'Invalid Id',
                         'Should return not found response')

    def test_view_political_party_not_found(self):
        """Tests malformed GET Http method request on /office/{:id} endpoint"""
        response = self.client.get('api/v1/partiess/{}'.format(0))
        self.assertEqual(response.status_code, 404, "Should Return a 404 HTTP Status Code Response:Not Found")
        # Should return error message
        self.assertEqual(response.json, self.error_default_not_found, "Should return resource not found response")

    def test_view_all_political_parties(self):
        """Tests GET Http method request on /parties/ endpoint"""
        # Post, create a political party
        self.client.post('api/v1/parties', data=json.dumps(self.party))
        # Retrieve the office
        response = self.client.get('api/v1/parties')
        expected_response_json = {
            "data": [{
                "id": 1,
                "name": "Pinnacle Party",
                "hqAddress": "Nairobi,Kenya 00100",
                "logoUrl": "https://www.some.url.co.ke"
            }],
            "status": 200
        }
        # Assert - (expected,actual)
        self.assertEqual(response.status_code, 200, "Should Return a 200 HTTP Status Code Response:Success")
        # Converts to string
        self.assertEqual(response.json, expected_response_json)

    def test_view_all_political_parties_empty_list(self):
        """Tests malformed GET Http method request on /parties/ endpoint"""
        response = self.client.get('api/v1/parties')
        self.assertEqual(response.status_code, 200, "Should Return a 200 HTTP Status Code Response:Success")
        expected_response_json = {
            "data": [],
            "status": 200
        }
        # Should return error message
        self.assertEqual(response.json, expected_response_json, "Should return [] empty list")

    def test_view_all_political_parties_wrong_path(self):
        """Tests malformed GET Http method request on /parties/ endpoint"""
        response = self.client.get('api/v1/partis')
        self.assertEqual(response.status_code, 404, "Should Return a 404 HTTP Status Code Response:Resource Not Found")
        # Should return error message
        self.assertEqual(response.json, self.error_default_not_found, "Should return not found Response")

    def test_create_afresh_from_scratch_after_delete(self):
        # Create
        self.client.post('api/v1/parties', data=json.dumps(self.party))
        # Delete
        self.client.delete('api/v1/parties/{0}'.format(1))

        response = self.client.post('api/v1/parties', data=json.dumps(self.party))
        self.assertEqual(response.status_code, 201, "Should Create Party")
        self.assertEqual(response.json['data'][0]['id'], 1, "Should Create Non Duplicate Ids")

    def test_no_duplication(self):
        # Create
        self.client.post('api/v1/parties', data=json.dumps(self.party))

        response = self.client.post('api/v1/parties', data=json.dumps(self.party))
        self.assertEqual(response.status_code, 409, "Should Create Party")
        self.assertEqual(response.json['error'], "Party Already Exists", "Should Create Non Duplicate Ids")
