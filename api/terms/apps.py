from django.apps import AppConfig


class TermsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.terms'
    verbose_name = "사용자 약관"
