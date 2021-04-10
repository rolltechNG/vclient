from django.test import TestCase
from django.urls import reverse


class NinViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        """Test that the nin url returns 200 OK"""
        response = self.client.get('/verify/nin/')
        self.assertEqual(response.status_code, 200)
        print('\n=====================================================')

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('frontend:post_nin'))
        self.assertEqual(response.status_code, 200)
