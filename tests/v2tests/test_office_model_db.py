from . import BaseTestCase
from api.v2.models.office import OfficesModelDb


class OfficeModelDbTestCase(BaseTestCase):
    def test_create_office_successful(self):
        """Tests office was created successfully"""
        office_name = self.office.create_resource('office', {"type": "Transport", "name": "Permernent Secretary"})
        self.assertEqual(office_name, 'Permernent Secretary')

    def test_create_office_duplicate(self):
        """Tests office already exists and cant be added"""
        office = {"type": "Transport", "name": "Permernent Secretary"}
        self.office.create_resource('office', office)
        integrity_error = self.office.create_resource('office', office)
        self.assertEqual(integrity_error, 'Office Exists')

    def test_create_office_invalid_data(self):
        """Tests data given is invalid"""
        integrity_error = self.office_invalid.create_resource('office', {"type": "Transport", "name": ""})
        self.assertEqual(integrity_error, 'Invalid Data')

    def test_get_offices(self):
        """Tests gets all data """
        OfficesModelDb().create_resource('office', {"name": "Governor", "type": "Government"})
        OfficesModelDb().create_resource('office', {"name": "Senetor", "type": "Government"})
        OfficesModelDb().create_resource('office', {"name": "County Rep", "type": "Private Sec"})
        offices = OfficesModelDb().get_resource('office')
        self.assertEqual(len(offices), 3)

    def test_edit_office_edits_item_successfuly(self):
        """Tests user edits an item successfully"""
        OfficesModelDb().create_resource('office', {"name": "Governor", "type": "Government"})
        edit_office = OfficesModelDb().edit_office('President', office_id=1)
        self.assertEqual('President', edit_office[0][2])

    def test_edit_office_cant_edit_invalid_data(self):
        """Tests user cant put invalid data while editing"""
        OfficesModelDb().create_resource('office', {"name": "Governor", "type": "Government"})
        edit_office = OfficesModelDb().edit_office('P', office_id=1)
        self.assertEqual('Invalid Data', edit_office)

    def test_edit_office_cant_edit_existing_data(self):
        """Tests User cant input existing office name"""
        OfficesModelDb().create_resource('office', {"name": "Governor", "type": "Government"})
        OfficesModelDb().create_resource('office', {"name": "Assembly Speaker", "type": "Government"})
        edit_office = OfficesModelDb().edit_office('Governor', office_id=2)
        self.assertEqual('Office Exists', edit_office)

    def test_edit_office_cant_edit_invalid_id(self):
        """Tests User cant input invalid id"""
        OfficesModelDb().create_resource('office', {"name": "Governor", "type": "Government"})
        OfficesModelDb().create_resource('office', {"name": "Assembly Speaker", "type": "Government"})
        edit_office = OfficesModelDb().edit_office('Governor', office_id='t')
        self.assertEqual('Invalid Id', edit_office)

    def test_gets_specific_item_success(self):
        """Tests can get data with right id"""
        OfficesModelDb().create_resource('office', {"name": "Governor", "type": "Government"})
        office = OfficesModelDb().get_specific_office(office_id=1)
        self.assertIn('Government', office[0][1])

    def test_gets_specific_item_invalid_id(self):
        """Tests cant get data with invalid id"""
        office = OfficesModelDb().get_specific_office(office_id='t')
        self.assertIn('Invalid Id', office)

    def test_delete_office_success(self):
        OfficesModelDb().create_resource('office', {"name": "Governor", "type": "Government"})
        delete_office = OfficesModelDb().delete_office(office_id=1)
        self.assertEqual('Governor', delete_office[0][0])

    def test_delete_office_failure(self):
        delete_office = OfficesModelDb().delete_office(office_id='e')
        self.assertEqual('Invalid Id', delete_office)
