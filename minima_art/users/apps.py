from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'minima_art.users'

    def ready(self):
        from .admin import initialize_roles
        initialize_roles()
