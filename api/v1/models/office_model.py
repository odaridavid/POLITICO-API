from . import Model

# List DT will hold list of parties and offices represented as dicts
offices = []


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
        office_id = Model(list_of_items=offices).generate_id()
        created_office = {
            # Id increments on length of list
            "id": office_id,
            "type": self.item['type'],
            "name": self.item['name'],

        }
        # Added to list
        offices.append(created_office)
        # Return assigned id response when office successfully created
        return created_office['id']
