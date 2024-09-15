from django.test import TestCase, Client
from django.urls import reverse_lazy
from lettings.models import Address, Letting


class LettingsViewsTestCase(TestCase):

    def setUp(self):
        # Créer un utilisateur et un profil pour les tests
        self.address = Address.objects.create(
            number=9,
            street="Rue des mouettes",
            city="Annecy",
            state="Haute-Savoie",
            zip_code=74000,
            country_iso_code="FRA"
        )
        self.letting = Letting.objects.create(
            title="Adresse Letting",
            address=self.address
        )
        self.client = Client()

    def test_lettings_index_view(self):
        response = self.client.get(
            reverse_lazy("lettings:lettings_index")
        )
        response_decoded = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.letting.__str__(), response_decoded)

    def test_letting_details(self):
        response = self.client.get(
            reverse_lazy("lettings:letting", kwargs={"letting_id": self.letting.id})
        )
        response_decoded = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.letting.address.__str__(), response_decoded)
