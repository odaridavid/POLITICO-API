from . import BaseTestCase
from api.v1.validator import PetitionValidator


class PetitionValidatorTest(BaseTestCase):
    def setUp(self):
        self.petition = {
            "createdBy": 1,
            "office": 2,
            "body": "Petition Body is put in here Petition Body is put in here Petition Body is put in herePetition "
                    "Body is put in herePetition Body is put in herePetition Body is put in here Petition Body is put "
                    "in here "
        }
        self.petition_invalid = {
            "createdBy": 0,
            "office": 2,
            "body": "P"
        }

    def test_ids_valid(self):
        validator = PetitionValidator(self.petition).checks('createdBy')
        self.assertEqual(validator, 1)

    def test_ids_invalid(self):
        validator = PetitionValidator(self.petition_invalid).checks('createdBy')
        self.assertEqual(validator, 'Invalid')

    def test_body_valid(self):
        validator = PetitionValidator(self.petition).check_body()
        self.assertEqual(validator, self.petition['body'])

    def test_body_invalid(self):
        validator = PetitionValidator(self.petition_invalid).check_body()
        self.assertEqual(validator, 'Invalid')

    def test_all_checks_valid(self):
        validator = PetitionValidator(self.petition).all_checks()
        self.assertEqual(validator, self.petition)

    def test_all_checks_invalid(self):
        validator = PetitionValidator(self.petition_invalid).check_body()
        self.assertEqual(validator, 'Invalid')
