from . import Model
from api.v1.validator import PartyValidator

# List DT will hold list of parties and offices represented as dicts
parties = []


# Use of new style class
class PartiesModel(Model):
    def __init__(self, party=None, party_id=0):
        # Initialise Party Values
        super(PartiesModel, self).__init__(item=party, item_id=party_id, list_of_items=parties)

    def create_political_party(self):
        """A function that facilitates creation of a political party and appending to a data structure
           @:return the created party name with success message
        """

        # Extract data from party dict
        party_id = super(PartiesModel, self).generate_id()
        validated_party = PartyValidator(self.item).all_checks()
        if not validated_party == 'Invalid':
            # Check for duplicates
            for party in parties:
                if party['name'] == validated_party['name']:
                    return 'Party Exists'
            created_party = {
                # Id increments on id of last element in list
                "id": party_id,
                "name": self.item['name'],
                "hqAddress": self.item['hqAddress'],
                "logoUrl": self.item['logoUrl']
            }
            # Added to list
            parties.append(created_party)
            # Return assigned id response when party successfully created
            return created_party['id']
        return 'Check Input Data'
