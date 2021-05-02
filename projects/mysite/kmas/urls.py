from django.urls import path

from .views import base_views

app_name = 'kmas'

urlpatterns = [
    # base_views.py
    path('kmas/', base_views.kmps, name='kmas'),
]