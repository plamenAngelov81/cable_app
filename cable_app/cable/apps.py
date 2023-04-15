from django.apps import AppConfig


class CableConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cable_app.cable'
