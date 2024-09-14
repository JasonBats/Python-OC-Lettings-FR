from django.contrib import admin
from django.urls import path, include

from . import views

"""
Defines URL patterns for the main app, mapping URLs to views.
"""

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include(("lettings.urls", "lettings"), namespace="lettings")),
    path('profiles/', include(("profiles.urls", "profiles"), namespace="profiles")),
    path('admin/', admin.site.urls),
    path('500/', views.trigger_error),  # Test route erreur 500 - à déplacer dans tests
]
