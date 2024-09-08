from django.apps import AppConfig
from rest_framework import serializers

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
