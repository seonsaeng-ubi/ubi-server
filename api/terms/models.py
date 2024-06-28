from django.db import models


class Terms(models.Model):
    title = models.CharField(max_length=512, verbose_name='지역', null=True, blank=True)
    link = models.CharField(max_length=1024, verbose_name='링크', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '약관'
        verbose_name_plural = verbose_name
