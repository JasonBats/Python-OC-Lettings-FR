from django.contrib.auth.models import User
from django.db import models

"""
Defines the Profile model for extending user information with a favorite city.
"""


class Profile(models.Model):
    """
    Represents a user profile with a favorite city.
    Linked to a Django User via a OneToOneField.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_in_profiles')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
