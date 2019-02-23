from . import BaseTestCase
import json


class ResultsEndpointsTestCase(BaseTestCase):

    def test_results_success(self):
        """
        Tests Results Accurate

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
            "candidate": 1,
            "office": 1,
            "results": 1
        }
        self.client.post('api/v2/office/1/register', data=json.dumps({"party": 1, "candidate": 1}),
                         headers=self.generate_token_admin())
        self.client.post('api/v2/votes/', data=json.dumps({"voter": 1, "candidate": 1, "office": 1}),
                         headers=self.generate_token())
        response = self.client.get('api/v2/office/1/result', headers=self.generate_token())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_json, response.json['data'][0])

    def test_results_invalid_id(self):
        """
        Tests Results Invalid Id
        """
        response = self.client.get('api/v2/office/@/result', headers=self.generate_token())
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid Office Id', response.json['error'])
