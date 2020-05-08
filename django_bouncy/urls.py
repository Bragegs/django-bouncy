"""URLs for the Django-Bouncy App"""
from django.conf.urls import url
# pylint: disable=invalid-name
from django_bouncy.views import endpoint

from django.urls import path

app_name = 'bouncy'

urlpatterns = [
    url(r'^$', endpoint, name='endpoint')
]
