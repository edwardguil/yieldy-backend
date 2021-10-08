from django.apps import AppConfig


class PredictionsConfig(AppConfig):
    """Specifies the name of the 'app'. Register this app in parent settings.py"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predictions'
