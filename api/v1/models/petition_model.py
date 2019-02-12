from . import Model
from time import localtime
from api.v1.validator import PetitionValidator

petitions = []


class PetitionModel(Model, object):
    def __init__(self, petition=None, petition_id=0):
        super(PetitionModel, self).__init__(item=petition, item_id=petition_id, list_of_items=petitions)

    def create_petition(self):
        """Creates A Petition"""
        petition_id = super(PetitionModel, self).generate_id()
        validated_petition = PetitionValidator(self.item).all_checks()
        # Checks If user exists
        if not validated_petition == 'Invalid':
            created_petition = {
                # Auto Gen id and timestamp
                "id": petition_id,
                "createdOn": "{0}/{1}/{2} at {3}:{4}".format(localtime().tm_year, localtime().tm_mon,
                                                             localtime().tm_mday, localtime().tm_hour,
                                                             localtime().tm_min),
                "createdBy": validated_petition['createdBy'],
                "office": validated_petition['office'],
                "body": validated_petition['body']
            }
            petitions.append(created_petition)
            return created_petition
        return 'Invalid Operation'
