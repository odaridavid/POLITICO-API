from . import BaseTestCase


class OfficeEndpointsTestCase(BaseTestCase):
    def test_create_office(self):
        """Tests POST Http method request on /office endpoint"""
        pass

    def test_create_office_bad_request(self):
        """Tests malformed POST Http method request on /office endpoint"""
        pass

    def test_view_all_offices(self):
        """Tests GET Http method request on /office endpoint"""
        pass

    def test_view_all_offices_bad_request(self):
        """Tests malformed GET Http method request on /office endpoint"""
        pass

    def test_view_specific_office(self):
        """Tests GET Http method request on /office/{:id} endpoint"""
        pass

    def test_view_specific_office_not_found(self):
        """Tests malformed GET Http method request on /office/{:id} endpoint"""
        pass
