from . import BaseTestCase
import json


class ResultsEndpointsTestCase(BaseTestCase):
    def test_results_invalid_id(self):
        """
        Tests Results Invalid Id
        """
        response = self.client.get('api/v2/office/@/result')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid Office Id', response.json['error'])


