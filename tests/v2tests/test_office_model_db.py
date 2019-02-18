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

    def test_edit_office_edits_item_successfuly(self):
        """Tests user edits an item successfully"""
        OfficesModelDb({"name": "Governor", "type": "Government"}).create_office()
        edit_office = OfficesModelDb(office_id=1).edit_office('President')
        self.assertEqual('President', edit_office[0][2])

    def test_edit_office_cant_edit_invalid_data(self):
        """Tests user cant put invalid data while editing"""
        OfficesModelDb({"name": "Governor", "type": "Government"}).create_office()
        edit_office = OfficesModelDb(office_id=1).edit_office('P')
        self.assertEqual('Invalid Data', edit_office)

    def test_edit_office_cant_edit_existing_data(self):
        """Tests User cant input existing office name"""
        OfficesModelDb({"name": "Governor", "type": "Government"}).create_office()
        OfficesModelDb({"name": "Assembly Speaker", "type": "Government"}).create_office()
        edit_office = OfficesModelDb(office_id=2).edit_office('Governor')
        self.assertEqual('Office Exists', edit_office)

    def test_edit_office_cant_edit_invalid_id(self):
        """Tests User cant input invalid id"""
        OfficesModelDb({"name": "Governor", "type": "Government"}).create_office()
        OfficesModelDb({"name": "Assembly Speaker", "type": "Government"}).create_office()
        edit_office = OfficesModelDb(office_id='t').edit_office('Governor')
        self.assertEqual('Invalid Id', edit_office)

    def test_gets_specific_item_success(self):
        """Tests can get data with right id"""
        OfficesModelDb({"name": "Governor", "type": "Government"}).create_office()
        office = OfficesModelDb(office_id=1).get_specific_office()
        self.assertIn('Government', office[0][1])

    def test_gets_specific_item_invalid_id(self):
        """Tests cant get data with invalid id"""
        office = OfficesModelDb(office_id='t').get_specific_office()
        self.assertIn('Invalid Id', office)
