from django.db import models


class Setting(models.Model):
    version = models.CharField(max_length=32, null=True, blank=True, verbose_name='버전')
    is_blocked = models.BooleanField(default=False, verbose_name='블락 상태')

    class Meta:
        verbose_name = '버전'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.version)


class AndroidSetting(models.Model):
    version = models.CharField(max_length=32, null=True, blank=True, verbose_name='버전')
    is_blocked = models.BooleanField(default=False, verbose_name='블락 상태')

    class Meta:
        verbose_name = '안드로이드 버전'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.version)