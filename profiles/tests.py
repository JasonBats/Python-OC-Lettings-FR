from django.test import TestCase, Client
from django.urls import reverse_lazy
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfileViewsTestCase(TestCase):

    def setUp(self):
        # Créer un utilisateur et un profil pour les tests
        self.user = User.objects.create_user(username='john_doe', password='password123')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Paris')
        self.client = Client()

    def test_profiles_index_view(self):
        response = self.client.get(
            reverse_lazy("profiles:profiles_index")
        )
        response_decoded = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.profile.user.username, response_decoded)

    def test_profile_details(self):
        response = self.client.get(
            reverse_lazy("profiles:profile", kwargs={"username": self.profile.user.username})
        )
        response_decoded = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.profile.__str__(), response_decoded)
