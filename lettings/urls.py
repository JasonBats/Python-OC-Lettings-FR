from django.urls import path

from . import views

"""
Defines URL patterns for the 'lettings' app, mapping URLs to views.
"""

urlpatterns = [
    path('', views.lettings_index, name='lettings_index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
