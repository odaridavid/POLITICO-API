from . import BaseTestCase
from api.v2.models.parties import PartiesModelDb


class PartiesModelDbTestCase(BaseTestCase):
    def test_create_party_successful(self):
        """Tests party was created successfully"""
        party_name = self.party.create_resource('party', {
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        })
        self.assertEqual(party_name, 'Party Name')

    def test_create_party_duplicate(self):
        """Tests party already exists and cant be added"""
        self.party.create_resource('party', {
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        })
        integrity_error = self.party.create_resource('party', {
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        })
        self.assertEqual(integrity_error, 'Party Exists')

    def test_create_party_invalid_data(self):
        """Tests data given is invalid"""
        integrity_error = self.party_invalid.create_resource('party', {
            "name": "",
            "hqAddress": "A",
            "logoUrl": "www.some.url.to.my.picture"
        })
        self.assertEqual(integrity_error, 'Invalid Data')

    def test_get_parties(self):
        """Tests gets all data """
        PartiesModelDb().create_resource('party', {
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture2"})
        PartiesModelDb().create_resource('party', {
            "name": "Party Name2",
            "hqAddress": "Address3",
            "logoUrl": "www.some.url.to.my.picture1"})
        PartiesModelDb().create_resource('party', {
            "name": "Party Name3",
            "hqAddress": "Address2",
            "logoUrl": "www.some.url.to.my.picture3"})
        parties = PartiesModelDb().get_resource('party')
        self.assertEqual(len(parties), 3)

    def test_edit_party_edits_item_successfuly(self):
        """Tests user edits an item successfully"""
        self.party.create_resource('party', {
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        })
        edit_party = PartiesModelDb().edit_resource('party', 'New Party Name', 1)
        self.assertEqual('New Party Name', edit_party[0][1])

    def test_edit_party_cant_edit_invalid_data(self):
        """Tests user cant put invalid data while editing"""
        self.party.create_resource('party', {
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        })
        edit_party = PartiesModelDb().edit_resource('party', 'P', 1)
        self.assertEqual('Invalid Data', edit_party)

    def test_edit_party_cant_edit_similar_existing_data(self):
        """Tests User cant input existing office name"""
        PartiesModelDb().create_resource('party', {
            "name": "Party Name2",
            "hqAddress": "Address3",
            "logoUrl": "www.some.url.to.my.picture1"})
        PartiesModelDb().create_resource('party', {
            "name": "Party Name3",
            "hqAddress": "Address2",
            "logoUrl": "www.some.url.to.my.picture3"})

        edit_party = PartiesModelDb().edit_resource('party', 'Party Name2', 2)
        self.assertEqual('Party Exists', edit_party)

    def test_edit_party_cant_edit_invalid_id(self):
        """Tests User cant input invalid id"""
        edit_party = PartiesModelDb().edit_resource('party', 'Party We', 't')
        self.assertEqual('Invalid Id', edit_party)

    def test_gets_specific_item_success(self):
        """Tests can get data with right id"""
        self.party.create_resource('party', {
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        })
        party = PartiesModelDb().get_specific_party(party_id=1)
        self.assertIn('Party Name', party[0][1])

    def test_gets_specific_item_invalid_id(self):
        """Tests cant get data with invalid id"""
        party = PartiesModelDb().get_specific_party(party_id='t')
        self.assertIn('Invalid Id', party)

    def test_delete_office_success(self):
        """Tests User can delete"""
        self.party.create_resource('party', {
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        })
        delete_office = PartiesModelDb().delete_party(party_id=1)
        self.assertEqual('Party Name', delete_office[0][0])

    def test_delete_office_failure(self):
        """Tests User delete with wrong id"""
        delete_office = PartiesModelDb().delete_party(party_id='e')
        self.assertEqual('Invalid Id', delete_office)
