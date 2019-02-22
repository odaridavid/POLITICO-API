from . import BaseTestCase
import json


class VotesViewTestCase(BaseTestCase):
    def test_vote_success(self):
        """
        Tests Voted Successfully
        """
        self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        }), headers=self.generate_token_admin())
        self.client.post('api/v2/offices', data=json.dumps({
            "type": "Health",
            "name": "Minister for Health"
        }), headers=self.generate_token_admin())
        expected_json = {
            "office": 1,
            "candidate": 1,
            "voter": 1
        }
        self.client.post('api/v2/office/1/register', data=json.dumps({"party": 1, "candidate": 1}),
                         headers=self.generate_token_admin())
        response = self.client.post('api/v2/votes/', data=json.dumps({"voter": 1, "candidate": 1, "office": 1}),
                                    headers=self.generate_token())
        self.assertEqual(response.status_code, 201, "Voting Should Be Successful")
        self.assertEqual(expected_json, response.json['data'][0])

    def test_voter_cant_vote_twice(self):
        """
         Tests Voting cant happen twice by one user for specific office
         """
        self.client.post('api/v2/parties', data=json.dumps({
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        }), headers=self.generate_token_admin())
        self.client.post('api/v2/offices', data=json.dumps({
            "type": "Health",
            "name": "Minister for Health"
        }), headers=self.generate_token_admin())
        self.client.post('api/v2/office/1/register', data=json.dumps({"party": 1, "candidate": 1}),
                         headers=self.generate_token_admin())
        self.client.post('api/v2/votes/', data=json.dumps({"voter": 1, "candidate": 1, "office": 1}),
                         headers=self.generate_token())
        response = self.client.post('api/v2/votes/', data=json.dumps({"voter": 1, "candidate": 1, "office": 1}),
                                    headers=self.generate_token())
        self.assertEqual(response.status_code, 409, "Voting Should Be unsuccessful")
        self.assertEqual("Vote Already Cast or Voting for non existent entities", response.json['error'])

    def test_candidate_cant_register_with_missing_info(self):
        response = self.client.post('api/v2/votes/', data=json.dumps({"voter": 1, "candidate": 1}),
                                    headers=self.generate_token())
        self.assertEqual(response.status_code, 400, "Voting Should Be unsuccessful")
        self.assertEqual("Missing Vote Information", response.json['error'])

    def test_candidate_cant_register_with_invalid_id(self):
        response = self.client.post('api/v2/votes/', data=json.dumps({"voter": 1, "candidate": 1, "office": "office"}),
                                    headers=self.generate_token())
        self.assertEqual(response.status_code, 400, "Voting Should Be unsuccessful")
        self.assertEqual("Invalid Credentials on Vote Request", response.json['error'])
