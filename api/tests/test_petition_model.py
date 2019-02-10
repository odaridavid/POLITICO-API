from . import BaseTestCase
from api.v1.models.petition_model import PetitionModel
from api.v1.models import petition_model


class PetitionModelTest(BaseTestCase):
    def setUp(self):
        self.petition = PetitionModel(petition={
            "createdBy": 1,
            "office": 2,
            "body": "This is a petition Against x for the seat y"
        })
        self.petition_invalid = PetitionModel(petition={
            "createdBy": 0,
            "office": 2,
            "body": "This is a petition Against x for the seat y"
        })

    def tearDown(self):
        petition_model.petitions.clear()

    def test_create_petition(self):
        """Test Politician Can Create Petition"""
        petition_id = self.petition.create_petition()
        self.assertEqual(petition_id, 1)
        self.assertTrue(len(petition_model.petitions) >= 1)

    def test_create_petition_invalid_user(self):
        """Test Politician Can Create Petition"""
        petition_error_msg = self.petition_invalid.create_petition()
        self.assertEqual(petition_error_msg, 'Invalid Operation')
