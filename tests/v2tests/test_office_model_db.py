from . import BaseTestCase
from api.v2.models.office_model import OfficesModelDb


class OfficeModelDbTestCase(BaseTestCase):
    def test_create_office_successful(self):
        """Tests office was created successfully"""
        office_name = self.office.create_office()
        self.assertEqual(office_name, 'Permernent Secretary')

    def test_create_office_duplicate(self):
        """Tests office already exists and cant be added"""
        self.office.create_office()
        integrity_error = self.office.create_office()
        self.assertEqual(integrity_error, 'Office Exists')

    def test_create_office_invalid_data(self):
        """Tests data given is invalid"""
        integrity_error = self.office_invalid.create_office()
        self.assertEqual(integrity_error, 'Invalid Data')

    def test_get_offices(self):
        """Tests gets all data """
        OfficesModelDb({"name": "Governor", "type": "Government"}).create_office()
        OfficesModelDb({"name": "Senetor", "type": "Government"}).create_office()
        OfficesModelDb({"name": "County Rep", "type": "Private Sec"}).create_office()
        offices = OfficesModelDb().get_all_offices()
        self.assertEqual(len(offices), 3)
