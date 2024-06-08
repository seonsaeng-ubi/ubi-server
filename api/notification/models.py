from django.utils.translation import gettext_lazy as _
from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=512, verbose_name=_('제목'), null=True, blank=True)
    body = models.CharField(max_length=1024, verbose_name=_('본문 내용'), null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '공지사항'
        verbose_name_plural = verbose_name
