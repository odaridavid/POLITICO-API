from . import BaseTestCase
import json


class PartiesEndpointsTestCase(BaseTestCase):
    def test_create_political_party(self):
        """Tests POST Http method request on /parties endpoint"""
        # Post, uses party specification model
        response = self.client.post('/parties', json=self.party)
        # Data section returned as per response specification
        expected_response_data = {
            'data': [{
                'id': 1234567890,
                'name': 'Pinnacle Party'
            }]
        }
        # makes JSON Object a string
        expected_data_json = json.dumps(expected_response_data)
        # Assert - (expected,actual)
        assert 201 == response.status, "Should Return a 201 HTTP Status Code Response"
        assert expected_data_json == str(response.data)

    def test_create_political_party_bad_request(self):
        """Tests malformed POST Http method request on /parties endpoint"""
        response = self.client.post('/parties',
                                    json={
                                        'id': 1234567890,
                                        # Missing hq address and logo url
                                        'name': 'Pinnacle Party'
                                    })
        assert 400 == response.status, "Should Return a 400 HTTP Status Code Response:Bad Request"
        # Should return error message
        assert "Bad Request" in str(response.error), "Should return bad request response"

    def test_edit_political_party(self):
        """Tests PATCH Http method request on /parties/{:id}/name endpoint"""
        # Save Post First
        self.client.post('/parties', json=self.party)
        # Update Name
        response = self.client.patch('/parties/{0}/name'.format(self.party['id']),
                                     json={
                                         'name': 'Dynamo Party',
                                     })
        assert 200 == response.status, "Should Return a 200 HTTP Status Code Response:Updated"
        assert "Dynamo Party" in str(response.data)

    def test_edit_political_party_bad_request(self):
        """Tests malformed PATCH Http method request on /parties/{:id}/name endpoint"""
        response = self.client.patch('/parties/{0}/name'.format(999999))
        assert 400 == response.status, "Should Return a 400 HTTP Status Code Response:Bad Request"
        # Should return error message
        assert "Bad Request" in str(response.error), "Should return bad request response"

    def test_delete_political_party(self):
        """Tests DELETE Http method request on /parties/{:id} endpoint"""
        # Save Post First
        self.client.post('/parties', json=self.party)
        # Delete Post
        response = self.client.delete('/parties/{0}'.format(self.party['id']))
        assert 204 == response.status, "Should Return a 204 HTTP Status Code Response:Deleted"
        assert "Deleted" in str(response.data)

    def test_delete_political_party_not_found(self):
        """"Tests malformed DELETE Http method request on /parties/{:id} endpoint"""
        response = self.client.delete('/parties/0')
        assert 404 == response.status, "Should Return a 404 HTTP Status Code Response:Not Found"
        # Should return error message
        assert "Not Found" in str(response.error), "Should return resource not found response"

    def test_view_political_party(self):
        """Tests GET Http method request on /parties/{:id} endpoint"""
        # Create Party First
        self.client.post('/parties', json=self.party)
        # Get data for specific office
        response = self.client.get('/offices/{0}'.format(self.party['id']))
        assert 200 == response.status, "Should Return a 200 HTTP Status Code:Success"
        # Returns Dict as string and compares if its in response
        assert json.dumps({'data': [self.party]}) in str(response.data)

    def test_view_political_party_not_found(self):
        """Tests malformed GET Http method request on /parties/{:id} endpoint"""
        response = self.client.get('/parties/45789')
        assert 404 == response.status, "Should Return a 404 HTTP Status Code Response:Not Found"
        # Should return error message
        assert "Not Found" in str(response.error), "Should return resource not found response"

    def test_view_all_political_parties(self):
        """Tests GET Http method request on /parties/ endpoint"""
        # Post, create a political party
        self.client.post('/parties', json=self.party)
        # Retrieve the office
        response = self.client.get('/parties')
        # Assert - (expected,actual)
        assert 200 == response.status, "Should Return a 200 HTTP Status Code Response:Success"
        # Converts to string
        assert json.dumps({'data': [self.party]}) in str(response.data)

    def test_view_all_political_parties_bad_request(self):
        """Tests malformed GET Http method request on /parties/ endpoint"""
        response = self.client.get('/partyes')
        assert 404 == response.status, "Should Return a 404 HTTP Status Code Response:Not Found"
        # Should return error message
        assert "Not Found" in str(response.error), "Should return resource not found response"
