from django.apps import AppConfig


class StudentuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'studentuser'

    def ready(self):
        import studentuser.signals