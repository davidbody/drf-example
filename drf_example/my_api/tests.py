from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ViewsTest(APITestCase):
    def test_get_total_views(self):
        """
        Get total video views
        """
        url = reverse('total-views')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'total_views': 123456789})
