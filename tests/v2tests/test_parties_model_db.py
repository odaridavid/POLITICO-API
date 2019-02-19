from . import BaseTestCase
from api.v2.models.parties_model import PartiesModelDb


class PartiesModelDbTestCase(BaseTestCase):
    def test_create_party_successful(self):
        """Tests party was created successfully"""
        party_name = self.party.create_party()
        self.assertEqual(party_name, 'Party Name')

    def test_create_party_duplicate(self):
        """Tests party already exists and cant be added"""
        self.party.create_party()
        integrity_error = self.party.create_party()
        self.assertEqual(integrity_error, 'Party Exists')

    def test_create_party_invalid_data(self):
        """Tests data given is invalid"""
        integrity_error = self.party_invalid.create_party()
        self.assertEqual(integrity_error, 'Invalid Data')

    def test_get_parties(self):
        """Tests gets all data """
        PartiesModelDb({
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture2"}).create_party()
        PartiesModelDb({
            "name": "Party Name2",
            "hqAddress": "Address3",
            "logoUrl": "www.some.url.to.my.picture1"}).create_party()
        PartiesModelDb({
            "name": "Party Name3",
            "hqAddress": "Address2",
            "logoUrl": "www.some.url.to.my.picture3"}).create_party()
        parties = PartiesModelDb().get_all_parties()
        self.assertEqual(len(parties), 3)

    def test_edit_party_edits_item_successfuly(self):
        """Tests user edits an item successfully"""
        self.party.create_party()
        edit_party = PartiesModelDb(party_id=1).edit_party('New Party Name')
        self.assertEqual('New Party Name', edit_party[0][1])

    def test_edit_party_cant_edit_invalid_data(self):
        """Tests user cant put invalid data while editing"""
        self.party.create_party()
        edit_party = PartiesModelDb(party_id=1).edit_party('P')
        self.assertEqual('Invalid Data', edit_party)

    def test_edit_party_cant_edit_similar_existing_data(self):
        """Tests User cant input existing office name"""
        PartiesModelDb({
            "name": "Party Name2",
            "hqAddress": "Address3",
            "logoUrl": "www.some.url.to.my.picture1"}).create_party()
        PartiesModelDb({
            "name": "Party Name3",
            "hqAddress": "Address2",
            "logoUrl": "www.some.url.to.my.picture3"}).create_party()

        edit_party = PartiesModelDb(party_id=2).edit_party('Party Name2')
        self.assertEqual('Party Exists', edit_party)

    def test_edit_party_cant_edit_invalid_id(self):
        """Tests User cant input invalid id"""
        edit_party = PartiesModelDb(party_id='t').edit_party('Party We')
        self.assertEqual('Invalid Id', edit_party)

    def test_gets_specific_item_success(self):
        """Tests can get data with right id"""
        self.party.create_party()
        party = PartiesModelDb(party_id=1).get_specific_party()
        self.assertIn('Party Name', party[0][1])

    def test_gets_specific_item_invalid_id(self):
        """Tests cant get data with invalid id"""
        party = PartiesModelDb(party_id='t').get_specific_party()
        self.assertIn('Invalid Id', party)

    def test_delete_office_success(self):
        """Tests User can delete"""
        self.party.create_party()
        delete_office = PartiesModelDb(party_id=1).delete_party()
        self.assertEqual('Party Name', delete_office[0][0])

    def test_delete_office_failure(self):
        """Tests User delete with wrong id"""
        delete_office = PartiesModelDb(party_id='e').delete_party()
        self.assertEqual('Invalid Id', delete_office)
