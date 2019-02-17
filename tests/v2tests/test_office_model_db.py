from . import BaseTestCase


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
