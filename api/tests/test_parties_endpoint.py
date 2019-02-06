from . import BaseTestCase
import json


class PartiesEndpointsTestCase(BaseTestCase):
    def test_create_political_party(self):
        """Tests POST Http method request on /parties endpoint"""
        # Post, uses party specification model
        response = self.client.post(path='/api/v1/parties', data=json.dumps(self.party))
        # Assert - (expected,actual)
        expected_data_json = {
            'data': [{
                'id': 1,
                'name': 'Pinnacle Party'
            }],
            "status": 201
        }
        assert response.status_code == 201, "Should Return a 201 HTTP Status Code Response"
        assert expected_data_json == response.json

    def test_create_political_party_bad_request(self):
        """Tests malformed POST Http method request on /parties endpoint"""
        response = self.client.post('api/v1/parties',
                                    json={
                                        # Missing hq address and logo url
                                        'name': 'Pinnacle Party'
                                    })
        assert 400 == response.status_code, "Should Return a 400 HTTP Status Code Response:Bad Request"
        # Should return error message
        assert "BAD REQUEST" in str(response.json), "Should return bad request response"

    def test_edit_political_party(self):
        """Tests PATCH Http method request on /parties/{:id}/name endpoint"""
        # Save Post First
        # self.client.post('/parties', json=self.party)
        # # Update Name
        # response = self.client.patch('/parties/{0}/name'.format(self.party['id']),
        #                              json={
        #                                  'id': 1,
        #                                  'name': 'Dynamo Party',
        #                              })
        # assert 200 == response.status, "Should Return a 200 HTTP Status Code Response:Updated"
        # assert "Dynamo Party" in str(response.data)
        pass

    def test_edit_political_party_bad_request(self):
        """Tests malformed PATCH Http method request on /parties/{:id}/name endpoint"""
        # response = self.client.patch('/parties/{0}/name'.format(999999))
        # assert 400 == response.status, "Should Return a 400 HTTP Status Code Response:Bad Request"
        # # Should return error message
        # assert "Bad Request" in str(response.error), "Should return bad request response"
        pass

    def test_delete_political_party(self):
        """Tests DELETE Http method request on /parties/{:id} endpoint"""
        # Save Post First
        # self.client.post('/parties', json=self.party)
        # # Delete Post
        # response = self.client.delete('/parties/{0}'.format(self.party['id']))
        # assert 204 == response.status, "Should Return a 204 HTTP Status Code Response:Deleted"
        # assert "Deleted" in str(response.data)
        pass

    def test_delete_political_party_not_found(self):
        """"Tests malformed DELETE Http method request on /parties/{:id} endpoint"""
        # response = self.client.delete('/parties/0')
        # assert 404 == response.status, "Should Return a 404 HTTP Status Code Response:Not Found"
        # # Should return error message
        # assert "Not Found" in str(response.error), "Should return resource not found response"
        pass

    def test_view_political_party(self):
        """Tests GET Http method request on /parties/{:id} endpoint"""
        # Create Party First
        # resp = self.client.post('api/v1/parties', json=self.party, content_type='application/json')
        # print(resp.json['data'][''])
        # # Get data for specific office
        # response = self.client.get('/offices/{0}'.format(self.party['id']))
        # assert 200 == response.status, "Should Return a 200 HTTP Status Code:Success"
        # # Returns Dict as string and compares if its in response
        # assert json.dumps({'data': [self.party]}) in str(response.data)
        pass

    def test_view_political_party_not_found(self):
        """Tests malformed GET Http method request on /parties/{:id} endpoint"""
        # response = self.client.get('/parties/45789')
        # assert 404 == response.status, "Should Return a 404 HTTP Status Code Response:Not Found"
        # # Should return error message
        # assert "Not Found" in str(response.error), "Should return resource not found response"

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
        assert 200 == response.status_code, "Should Return a 200 HTTP Status Code Response:Success"
        # Converts to string
        assert expected_response_json == response.json

    def test_view_all_political_parties_empty_list(self):
        """Tests malformed GET Http method request on /parties/ endpoint"""
        response = self.client.get('api/v1/parties')
        assert response.status_code == 200, "Should Return a 200 HTTP Status Code Response:Success"
        expected_response_json = {
            "data": [],
            "status": 200
        }
        # Should return error message
        assert expected_response_json == response.json, "Should return [] empty list"
