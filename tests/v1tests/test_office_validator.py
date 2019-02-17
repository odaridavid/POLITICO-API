from tests.v1tests import BaseTestCase
from api.validator import OfficeValidator


class OfficeValidatorTest(BaseTestCase):
    def setUp(self):
        self.office = {
            "name": "Permanent Sec",
            "type": "Transport",
        }
        self.office_invalid = {
            "name": "Da",
            "type": "Od",
        }

    def test_created_valid_office(self):
        self.validator_valid = OfficeValidator(self.office)
        validation_response = self.validator_valid.all_checks()
        self.assertEqual(validation_response['type'], self.office['type'])

    def test_created_invalid_office(self):
        self.validator_invalid = OfficeValidator(self.office_invalid)
        validation_response = self.validator_invalid.all_checks()
        self.assertEqual(validation_response, 'Invalid')
