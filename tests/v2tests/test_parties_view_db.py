from . import BaseTestCase
import json


class PartiesEndpointsTestCase(BaseTestCase):
    def test_party_created_success(self):
        """
        Tests Party Created Successfully
        """
        response = self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        }), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 201, "Party Creation should be Successful")
        self.assertEqual('Party Name', response.json['data'][0]['name'])

    def test_party_created_exists(self):
        """ Tests No Party was Duplicated """
        data = {
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        }
        self.client.post('api/v2/parties', data=json.dumps(data), headers=self.generate_token_admin())
        response = self.client.post('api/v2/parties', data=json.dumps(data), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 409, "Party Should Already Exists")
        self.assertEqual('Party Already Exists', response.json['error'])

    def test_created_party_with_invalid_data(self):
        """
        Tests Party with invalid data
        """
        response = self.client.post('api/v2/parties', data=json.dumps({
            "name": "P",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        }), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 400, "Should be Parsing Invalid Data ,Bad Request")
        self.assertIn('Check Input Values', response.json['error'])

    def test_create_party_with_missing_data(self):
        """
        Tests Party has missing data
        """
        response = self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name",
            "hqAddress": "Address"
        }), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 400, "Should be Parsing Invalid Data ,Bad Request")
        self.assertIn('Please Check All Input Fields Are Filled', response.json['error'])

    def test_get_all_party_empty(self):
        """Tests that the parties in the db are retrived as empty list if none"""
        response = self.client.get('api/v2/parties', headers=self.generate_token())
        self.assertEqual(response.status_code, 200, "Should be getting all parties")
        self.assertEqual(0, len(response.json['data']))

    def test_get_all_parties(self):
        """Tests that all parties are retrieved """
        self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        }), headers=self.generate_token_admin())
        self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name2",
            "hqAddress": "Address2",
            "logoUrl": "www.some.url.to.my.picture2"
        }), headers=self.generate_token_admin())
        response = self.client.get('api/v2/parties', headers=self.generate_token())
        self.assertEqual(response.status_code, 200, "Should be getting all parties")
        self.assertEqual(2, len(response.json['data']))

    def test_party_edited_successfully(self):
        """"Tests that parties are edited successfully"""
        self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name2",
            "hqAddress": "Address2",
            "logoUrl": "www.some.url.to.my.picture2"
        }), headers=self.generate_token_admin())
        response = self.client.patch('api/v2/parties/{}/name'.format(1), data=json.dumps({
            "name": "New Party"
        }), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 200)
        self.assertIn('New Party Updated Successfully', response.json['message'])

    def test_party_edited_unsuccessful_missing_key(self):
        """Test edit with missing key"""
        response = self.client.patch('api/v2/parties/{}/name'.format(1), data=json.dumps({
        }), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 400)
        self.assertIn('Please Check All Input Fields Are Filled', response.json['error'])

    def test_party_edited_exists(self):
        self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        }), headers=self.generate_token_admin())
        self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name2",
            "hqAddress": "Address2",
            "logoUrl": "www.some.url.to.my.picture2"
        }), headers=self.generate_token_admin())
        response = self.client.patch('api/v2/parties/{}/name'.format(1), data=json.dumps({
            "name": "Party Name"
        }), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 409)
        self.assertIn('Party with similar name exists', response.json['error'])

    def test_party_edited_data_invalid(self):
        response = self.client.patch('api/v2/parties/{}/name'.format(1), data=json.dumps({
            "name": "G"
        }), headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid Data ,Check id or data being updated', response.json['error'])

    def test_get_specific_party_success(self):
        """Tests get specific item"""
        self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name2",
            "hqAddress": "Address2",
            "logoUrl": "www.some.url.to.my.picture2"
        }), headers=self.generate_token_admin())
        response = self.client.get("api/v2/parties/1", headers=self.generate_token())
        self.assertEqual(response.status_code, 200)
        self.assertIn('Party Name2', response.json['data'][0]['name'])

    def test_get_specific_party_unsuccessful(self):
        response = self.client.get("api/v2/parties/1", headers=self.generate_token())
        self.assertEqual(response.status_code, 404)
        self.assertIn('Party Not Found', response.json['error'])

    def test_get_specific_party_fail(self):
        response = self.client.get("api/v2/parties/---", headers=self.generate_token())
        self.assertEqual(response.status_code, 404)
        self.assertIn('Party Not Found', response.json['error'])

    def test_delete_party_success(self):
        """Tests delete endpoint"""
        self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name2",
            "hqAddress": "Address2",
            "logoUrl": "www.some.url.to.my.picture2"
        }), headers=self.generate_token_admin())
        response = self.client.delete("api/v2/parties/1", headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Party Name2 Deleted', response.json['message'])

    def test_delete_party_fail(self):
        response = self.client.delete("api/v2/parties/1", headers=self.generate_token_admin())
        self.assertEqual(response.status_code, 404)
        self.assertEqual('Party Not Found', response.json['error'])

    def test_create_party_with_non_admin_token(self):
        response = self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        }), headers=self.generate_token())

        self.assertEqual(response.status_code, 401, "Non Admin Shouldnt Register Candidate")
        self.assertEqual(response.json['error'], 'Unauthorized Access,Requires Admin Rights')

    def test_delete_party_with_non_admin_token(self):
        self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        }), headers=self.generate_token_admin())
        response = self.client.delete("api/v2/parties/1", headers=self.generate_token())
        self.assertEqual(response.status_code, 401, "Non Admin Shouldnt Register Candidate")
        self.assertEqual(response.json['error'], 'Unauthorized Access,Requires Admin Rights')

    def test_edit_party_with_non_admin_token(self):
        self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        }), headers=self.generate_token_admin())
        response = self.client.patch('api/v2/parties/{}/name'.format(1), data=json.dumps({
            "name": "President"
        }), headers=self.generate_token())
        self.assertEqual(response.status_code, 401, "Non Admin Shouldnt Register Candidate")
        self.assertEqual(response.json['error'], 'Unauthorized Access,Requires Admin Rights')
