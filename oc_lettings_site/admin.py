from django.contrib import admin

from lettings.models import Letting
from lettings.models import Address
from profiles.models import Profile

"""
Registers models with the Django admin site for the 'lettings' and 'profiles' apps.
"""

admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
