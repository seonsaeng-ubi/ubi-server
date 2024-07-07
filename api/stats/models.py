from django.db import models


class Setting(models.Model):
    class SettingChoices(models.TextChoices):
        NO = 'A', '개발 환경'
        YES = 'B', '실제 환경'

    setting = models.CharField(choices=SettingChoices.choices, max_length=1, blank=True)

    class Meta:
        verbose_name = '설정'
        verbose_name_plural = verbose_name
