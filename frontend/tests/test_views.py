from django.test import TestCase


class NinViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        """Test that the nin url returns 200 OK"""
        response = self.client.get('/verify/nin/')
        self.assertEqual(response.status_code, 200)
        print('\n=====================================================')
