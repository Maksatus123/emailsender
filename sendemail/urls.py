from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', contact_view, name='contact'),
    path('success/', success_view, name='success'),
]