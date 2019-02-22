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
        }), headers=self.generate_token())
        self.client.post('api/v2/offices', data=json.dumps({
            "type": "Health",
            "name": "Minister for Health"
        }), headers=self.generate_token())
        expected_json = {
            'office': 'Minister for Health',
            'user': 'Davied'
        }
        response = self.client.post('api/v2/office/1/register', data=json.dumps({"party": 1, "candidate": 1}),
                                    headers=self.generate_token())
        self.assertEqual(response.status_code, 201, "Candidate Registration should be Successful")
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
        }), headers=self.generate_token())
        self.client.post('api/v2/offices', data=json.dumps({
            "type": "Health",
            "name": "Minister for Health"
        }), headers=self.generate_token())
        self.client.post('api/v2/office/1/register', data=json.dumps({"party": 1, "candidate": 1}),
                         headers=self.generate_token())
        response = self.client.post('api/v2/office/1/register', data=json.dumps({"party": 1, "candidate": 1}),
                                    headers=self.generate_token())
        self.assertEqual(response.status_code, 409, "Candidate Registration should be unsuccessful")
        self.assertEqual('Candidate Already Registered or Doesnt Exist', response.json['error'])

    def test_candidate_cant_register_with_missing_info(self):
        """
        Tests Candidate Cant register with missing info
        """
        response = self.client.post('api/v2/office/1/register', data=json.dumps({"candidate": 1}),
                                    headers=self.generate_token())
        self.assertEqual(response.status_code, 400, "Candidate Registration should be unsuccessful")
        self.assertEqual('Missing Input Values', response.json['error'])

    def test_candidate_cant_register_with_invalid_id(self):
        """
        Tests Candidate Cant register with invalid id
        """
        response = self.client.post('api/v2/office/1/register', data=json.dumps({"party": 'f', "candidate": 'f'}),
                                    headers=self.generate_token())
        self.assertEqual(response.status_code, 400, "Candidate Registration should be unsuccessful")
        self.assertEqual('Input of Invalid Id', response.json['error'])

    def test_get_list_of_candidates_success(self):
        """
        Tests Candidates Retrieved
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
        }), headers=self.generate_token())
        self.client.post('api/v2/offices', data=json.dumps({
            "type": "Health",
            "name": "Minister for Health"
        }), headers=self.generate_token())
        self.client.post('api/v2/office/1/register', data=json.dumps({"party": 1, "candidate": 1}),
                         headers=self.generate_token())
        response = self.client.get('api/v2/office/1/register', headers=self.generate_token())
        self.assertEqual(response.status_code, 200, "Candidate List Should be returned")
        self.assertEqual(response.json['data'][0]['candidate name'], 'Davied')
