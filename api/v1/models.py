from flask import jsonify

# List DT will hold list of parties represented as dicts
parties = []


class PartiesModel:
    def __init__(self, party):
        # Initialise DT inside model
        self.parties = parties
        self.party = party

    def create_political_party(self):
        """A function that facilitates creation of a political party and appending to a data structure
           @:return the created party name with success message
        """
        # Extract data from party dict
        # Created Party as dict
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


class OfficesModel:
    pass
