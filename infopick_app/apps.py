from django.apps import AppConfig

class InfopickAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'infopick_app'

    def ready(self):
        import infopick_app.signals  # Register signals

