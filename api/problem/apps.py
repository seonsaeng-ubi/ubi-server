from django.apps import AppConfig


class ProblemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.problem'
    verbose_name = "문제 은행"
