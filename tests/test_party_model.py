from . import BaseTestCase
from api.v1.models.party_model import PartiesModel


class PartyModelTest(BaseTestCase):
    def setUp(self):
        self.new_party = PartiesModel(party={"name": "Test Party", "hqAddress": "Address", "logoUrl": "logoUrl"})
        self.specific_party = PartiesModel(party_id=1)
        self.specific_party_invalid = PartiesModel(party_id=0)
        self.specific_party_not_exist = PartiesModel(party_id=67)

    def test_creating_political_party(self):
        # Create Party and get id
        party_id = self.new_party.create_political_party()
        self.assertEqual(party_id, 1)

    def test_gets_specific_party(self):
        self.new_party.create_political_party()
        party = self.specific_party.get_specific_item()
        self.assertEqual(party['name'], 'Test Party')
        self.assertEqual(party['hqAddress'], 'Address')
        self.assertEqual(party['logoUrl'], 'logoUrl')

    def test_gets_specific_party_invalid(self):
        msg = self.specific_party_invalid.get_specific_item()
        self.assertEqual(msg, 'Invalid Id')

    def test_gets_specific_party_not_exist(self):
        self.new_party.create_political_party()
        msg = self.specific_party_not_exist.get_specific_item()
        self.assertEqual(msg, 'Doesnt Exist')

    def test_gets_specific_party_name(self):
        self.new_party.create_political_party()
        party_name = self.specific_party.get_specific_political_party_name()
        self.assertEqual(party_name, "Test Party")

    def tests_gets_all_items_in_list(self):
        # Retrieves List of items
        self.new_party.create_political_party()
        self.new_party.create_political_party()
        current_list = self.new_party.get_all_items_in_list()
        self.assertEqual(len(current_list), 2, "List Length Incorrect")

    def tests_remove_party_from_list(self):
        # Removes item from list
        self.new_party.create_political_party()
        self.specific_party.remove_item()
        current_list = self.new_party.get_all_items_in_list()
        self.assertEqual(len(current_list), 0, "Item Doesnt Exist")

    def tests_remove_party_from_list_invalid(self):
        # If list is empty and id doesnt exist
        msg = self.specific_party_invalid.remove_item()
        self.assertEqual(msg, 'Invalid Id')

    def tests_remove_party_from_list_not_exist(self):
        # If list is not empty but id missing
        self.new_party.create_political_party()
        msg = self.specific_party_not_exist.remove_item()
        self.assertEqual(msg, 'Doesnt Exist')
