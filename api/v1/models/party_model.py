from . import Model

# List DT will hold list of parties and offices represented as dicts
parties = []


class PartiesModel(Model):
    def __init__(self, party=None, party_id=0):
        # Initialise Party Values
        super().__init__(party, party_id, parties)

    def create_political_party(self):
        """A function that facilitates creation of a political party and appending to a data structure
           @:return the created party name with success message
        """
        # TODO Validate Party Data
        # Extract data from party dict
        party_id = Model(list_of_items=parties).generate_id()
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

    def get_specific_political_party_name(self):
        # Get party by passed in id and return party otherwise default to message response
        if self.item_id >= 1:
            try:
                item = [item for item in self.list_of_items if item['id'] == self.item_id]
                if len(item) > 0:
                    return item[0]['name']
                return 'Doesnt Exist'
            except IndexError:
                return "Index Error"
        return 'Doesnt Exist In Model'
