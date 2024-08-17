from django.db import models


class Setting(models.Model):
    version = models.CharField(max_length=32, null=True, blank=True)

    class Meta:
        verbose_name = '버전'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.version)
