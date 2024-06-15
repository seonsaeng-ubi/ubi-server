from django.db import models
from api.user.models import User


class Region(models.Model):
    title = models.CharField(max_length=512, verbose_name='지역', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '지역'
        verbose_name_plural = verbose_name


class BigSubject(models.Model):
    title = models.CharField(max_length=512, verbose_name='대주제', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '주제'
        verbose_name_plural = verbose_name


class SmallSubject(models.Model):
    big_subject = models.ForeignKey(BigSubject, max_length=512, verbose_name='대주제', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=512, verbose_name='소주제', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '주제'
        verbose_name_plural = verbose_name


class ProblemSet(models.Model):
    title = models.CharField(max_length=512, verbose_name='문제 셋 이름', null=True, blank=True)
    description = models.TextField(verbose_name='설명', null=True, blank=True)
    region = models.ForeignKey(Region, verbose_name='지역', on_delete=models.SET_NULL)

    class PracticeChoice(models.TextChoices):
        PRACTICE = 'P', '연습'
        ACTUAL = 'A', '실전'

    type = models.CharField(choices=PracticeChoice.choices, max_length=1, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '문제 세트'
        verbose_name_plural = verbose_name


class Problem(models.Model):
    class TypeChoices(models.TextChoices):
        CONCEPTION = 'A', '구상'
        IMMEDIATE = 'B', '즉답'
        ADDITIONAL = 'C', '추가질문'

    number = models.CharField(max_length=32, verbose_name='고유 번호', null=True, blank=True)
    title = models.CharField(max_length=512, verbose_name='제목', null=True, blank=True)
    type = models.CharField(choices=TypeChoices.choices, max_length=1, blank=True)
    region = models.ForeignKey(Region, verbose_name='지역', on_delete=models.SET_NULL)
    big_subject = models.ForeignKey(BigSubject, verbose_name='대주제', on_delete=models.SET_NULL)
    small_subject = models.ManyToManyField(SmallSubject, verbose_name='소주제')
    presentation = models.TextField(verbose_name='제시문', null=True, blank=True)
    question = models.TextField(verbose_name='문제', null=True, blank=True)
    answer = models.TextField(verbose_name='정답', null=True, blank=True)
    scrapped_users = models.ManyToManyField(User, related_name='scrapped_problems', verbose_name='이 문제를 스크랩한 사람들')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '문제'
        verbose_name_plural = verbose_name