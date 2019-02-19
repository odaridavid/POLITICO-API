from . import BaseTestCase
import json


class CandidatesViewTestCase(BaseTestCase):
    def test_candidate_creation_success(self):
        """
        Tests Candidate Created Successfully
        """
        self.client.post('api/v2/auth/signup', data=json.dumps({
            "firstname": "Davied",
            "lastname": "Odari",
            "othername": "Kiribwa",
            "email": "odari@amail.com",
            "phoneNumber": "0717455945",
            "passportUrl": "www.googledrive.com/pics?v=jejfek",
            "password": "1wwjdje3qr",
            "isAdmin": 0
        }))
        self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        }))
        self.client.post('api/v2/offices', data=json.dumps({
            "type": "Health",
            "name": "Minister for Health"
        }))
        expected_json = {
            'office': 'Minister for Health',
            'user': 'Davied'
        }
        response = self.client.post('api/v2/office/1/register', data=json.dumps({"party": 1, "candidate": 1}))
        self.assertEqual(response.status_code, 200, "Candidate Registration should be Successful")
        self.assertEqual(expected_json, response.json['data'][0])

    def test_candidate_cant_register_twice(self):
        """
        Tests Candidate Created Successfully
        """
        self.client.post('api/v2/auth/signup', data=json.dumps({
            "firstname": "Davied",
            "lastname": "Odari",
            "othername": "Kiribwa",
            "email": "odari@amail.com",
            "phoneNumber": "0717455945",
            "passportUrl": "www.googledrive.com/pics?v=jejfek",
            "password": "1wwjdje3qr",
            "isAdmin": 0
        }))
        self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        }))
        self.client.post('api/v2/offices', data=json.dumps({
            "type": "Health",
            "name": "Minister for Health"
        }))
        self.client.post('api/v2/office/1/register', data=json.dumps({"party": 1, "candidate": 1}))
        response = self.client.post('api/v2/office/1/register', data=json.dumps({"party": 1, "candidate": 1}))
        self.assertEqual(response.status_code, 400, "Candidate Registration should be Successful")
        self.assertEqual('Check Data for invalid request', response.json['error'])
