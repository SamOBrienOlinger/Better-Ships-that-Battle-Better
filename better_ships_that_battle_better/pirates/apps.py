"""
Django app configuration for the pirates application.
This module contains the AppConfig class for the pirates app,
which is part of the Better Ships that Battle Better game.
"""
from django.apps import AppConfig
class PiratesConfig(AppConfig):
    """Django app configuration for the pirates application."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pirates'
