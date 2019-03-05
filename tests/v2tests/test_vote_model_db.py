from . import BaseTestCase
from api.v2.models.votes import VoteModel


class VotesModelTestCase(BaseTestCase):
    def test_user_can_vote_successfully(self):
        self.party.create_party({
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        })
        self.office.create_office({"type": "Transport", "name": "Permernent Secretary"})
        self.user.user_sign_up({"firstname": "David",
                                "lastname": "Odari",
                                "othername": "Kiribwa",
                                "email": "odari@gmail.com",
                                "phoneNumber": "0717455945",
                                "passportUrl": "www.googledrive.com/pics?v=jejfek",
                                "password": "12we3e4r",
                                "isAdmin": 'f'
                                })
        self.candidate.register_candidate(1, 1, 1)
        vote = self.vote.vote(office_id=1, candidate_id=1, user_id=1)
        self.assertEqual(vote, [(1, 1, 1)])

    def test_user_cant_vote_twice_same_office(self):
        self.party.create_party({
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        })
        self.office.create_office({"type": "Transport", "name": "Permernent Secretary"})
        self.user.user_sign_up({"firstname": "David",
                                "lastname": "Odari",
                                "othername": "Kiribwa",
                                "email": "odari@gmail.com",
                                "phoneNumber": "0717455945",
                                "passportUrl": "www.googledrive.com/pics?v=jejfek",
                                "password": "12we3e4r",
                                "isAdmin": 'f'
                                })
        self.candidate.register_candidate(1, 1, 1)
        self.vote.vote(office_id=1, candidate_id=1, user_id=1)
        vote_again = self.vote.vote(office_id=1, candidate_id=1, user_id=1)
        self.assertEqual('Vote Conflict', vote_again)

    def test_user_cant_vote_for_non_existent_items(self):
        vote = VoteModel().vote(0, 0, 0)
        self.assertEqual(vote, 'Vote Conflict')
