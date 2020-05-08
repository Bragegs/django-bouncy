from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

admin.autodiscover()

urlpatterns = [
    path('bouncy/', include('django_bouncy.urls')),
]
