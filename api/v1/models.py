# List DT will hold list of parties and offices represented as dicts
parties = []
offices = []


class Model:
    # Generic Class from which models will inherit from
    def __init__(self, item=None, item_id=0, list_of_items=None):
        self.item = item
        self.item_id = item_id
        self.list_of_items = list_of_items

    def get_specific_item(self):
        # Return specific item based on class that was called
        if self.item_id >= 1:
            try:
                self.item = self.list_of_items[self.item_id - 1]
                if self.item is not None:
                    return self.item
                return 'Doesnt Exist'
            except IndexError:
                return "Index Error"
        return 'Invalid Id'

    def get_all_items_in_list(self):
        # Returns list of items for class that was called
        return self.list_of_items


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
        created_party = {
            # Id increments on length of list
            "id": len(self.list_of_items) + 1,
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
                self.item = self.list_of_items[self.item_id - 1]
                if self.item is not None:
                    return self.item['name']
                return 'Doesnt Exist'
            except IndexError:
                return "Index Error"
        return 'Doesnt Exist In Model'


class OfficesModel(Model):
    def __init__(self, office=None, office_id=0):
        # Initialise Office Values
        super().__init__(office, office_id, offices)

    def create_government_office(self):
        """A function that facilitates creation of a government office and appending to a data structure
           @:return the created office id with success message
        """
        # Extract data from party dict
        # Created Office as dict
        created_office = {
            # Id increments on length of list
            "id": len(self.list_of_items) + 1,
            "type": self.item['type'],
            "name": self.item['name'],

        }
        # Added to list
        offices.append(created_office)
        # Return assigned id response when office successfully created
        return created_office['id']
