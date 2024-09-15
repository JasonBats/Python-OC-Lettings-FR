from django.test import TestCase
from django.urls import reverse_lazy


class IndexTestCase(TestCase):

    def test_index_view(self):
        response = self.client.get(
            reverse_lazy("index")
        )
        response_decoded = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome to Holiday Homes", response_decoded)
