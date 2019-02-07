# List DT will hold list of parties and offices represented as dicts
parties = []
offices = []


class PartiesModel:
    def __init__(self, party=None, party_id=0):
        # Initialise DT inside model
        self.parties = parties
        self.party = party
        self.party_id = party_id

    def create_political_party(self):
        """A function that facilitates creation of a political party and appending to a data structure
           @:return the created party name with success message
        """
        # Extract data from party dict
        created_party = {
            # Id increments on length of list
            "id": len(parties) + 1,
            "name": self.party['name'],
            "hqAddress": self.party['hqAddress'],
            "logoUrl": self.party['logoUrl']
        }
        # Added to list
        parties.append(created_party)
        # Return assigned id response when party successfully created
        return created_party['id']

    def get_all_political_parties(self):
        # Get List Of Parties
        return self.parties

    def get_specific_political_party_name(self):
        # Get party by passed in id and return party otherwise default to message response
        if self.party_id is not None:
            for party in parties:
                if party['id'] == self.party_id:
                    return party
        return 'Doesnt Exist In Model'

    def get_specific_party(self):
        # Gets Office after series of checks
        return SpecificGeneric(self.party_id, parties).get_specific_item()


class OfficesModel:
    def __init__(self, office=None, office_id=0):
        self.offices = offices
        self.office = office
        self.office_id = office_id

    def create_government_office(self):
        """A function that facilitates creation of a government office and appending to a data structure
           @:return the created office id with success message
        """
        # Extract data from party dict
        # Created Office as dict
        created_office = {
            # Id increments on length of list
            "id": len(parties) + 1,
            "type": self.office['type'],
            "name": self.office['name'],

        }
        # Added to list
        offices.append(created_office)
        # Return assigned id response when office successfully created
        return created_office['id']

    def get_all_government_offices(self):
        # Gets List Of Government offices
        return self.offices

    def get_specific_office(self):
        # Gets Office after series of checks
        return SpecificGeneric(self.office_id, offices).get_specific_item()


class SpecificGeneric:
    def __init__(self, item_id, list_of_items):
        self.id = item_id
        self.list_of_items = list_of_items

    def get_specific_item(self):
        if self.id >= 1:
            for item in self.list_of_items:
                if item['id'] == self.id:
                    return item
        return 'Invalid Id'
