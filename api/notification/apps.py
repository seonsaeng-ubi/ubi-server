from django.apps import AppConfig


class NotificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.notification'
    verbose_name = '공지 사항'

    def ready(self):
        import api.notification.signals
