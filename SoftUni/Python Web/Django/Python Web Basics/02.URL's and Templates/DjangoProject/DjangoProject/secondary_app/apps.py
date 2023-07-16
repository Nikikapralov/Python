from django.apps import AppConfig


class SecondaryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DjangoProject.secondary_app'
