from django.apps import AppConfig


class BeautycityAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'beautycity_app'

    def ready(self):
        import beautycity_app.signals