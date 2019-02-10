from . import Model
from api.v1.validator import OfficeValidator

# List DT will hold list of parties and offices represented as dicts
offices = []


class OfficesModel(Model):
    def __init__(self, office=None, office_id=0):
        # Initialise Office Values
        super().__init__(item=office, item_id=office_id, list_of_items=offices)

    def create_government_office(self):
        """
        A function that facilitates creation of a government office and appending to a data structure
        @:return the created office id
        """
        # Generate Unique id
        office_id = super().generate_id()
        office_validator = OfficeValidator(self.item)
        # Validation Response
        validated_office = office_validator.all_checks()
        if isinstance(validated_office, dict):
            # Created Office as dict
            created_office = {
                # Id increments on length of list
                "id": office_id,
                "type": validated_office['type'],
                "name": validated_office['name']
            }
            # Added to list
            offices.append(created_office)
            # Return assigned id response when office successfully created
            return created_office['id']
        return 'Check Input Data'
