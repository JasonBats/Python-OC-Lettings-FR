from django.urls import path

from . import views

"""
Defines URL patterns for the profiles app, mapping URLs to views.
"""

urlpatterns = [
    path('', views.profiles_index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]
