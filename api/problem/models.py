from django_summernote.utils import get_attachment_storage, get_attachment_upload_to
from django_summernote import models as summermodel
from api.user.models import User
from django.db import models


class Region(models.Model):
    title = models.CharField(max_length=512, verbose_name='지역', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '지역'
        verbose_name_plural = verbose_name


class RealRegion(models.Model):
    title = models.CharField(max_length=512, verbose_name='지역', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '기출 출제 지역'
        verbose_name_plural = verbose_name


class BigSubject(models.Model):
    title = models.CharField(max_length=512, verbose_name='대주제', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '대주제'
        verbose_name_plural = verbose_name


class SmallSubject(models.Model):
    big_subject = models.ForeignKey(BigSubject, max_length=512, verbose_name='대주제',
                                    on_delete=models.CASCADE, null=True, blank=True, related_name='big_small_subjects')
    title = models.CharField(max_length=512, verbose_name='소주제', null=True, blank=True)
    color = models.CharField(max_length=10, verbose_name='색상', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '소주제'
        verbose_name_plural = verbose_name


# 실전 문제 세트 설명
class TestSet(models.Model):
    region = models.ForeignKey(Region, verbose_name='지역', null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='출제 문항 설명', null=True, blank=True)
    time_description = models.TextField(verbose_name='제한시간 설명', null=True, blank=True)

    def __str__(self):
        return str(self.region.title)

    class Meta:
        verbose_name = '실전 모의고사'
        verbose_name_plural = verbose_name


class Problem(models.Model):
    class PracticeChoice(models.TextChoices):
        PRACTICE = 'P', '연습'
        ACTUAL = 'A', '실전'

    problem_type = models.CharField(choices=PracticeChoice.choices, max_length=1, blank=True)

    class TypeChoices(models.TextChoices):
        CONCEPTION = 'A', '구상'
        IMMEDIATE = 'B', '즉답'
        ADDITIONAL = 'C', '추가질문'

    number = models.CharField(max_length=32, verbose_name='고유 번호', null=True, blank=True)
    title = models.CharField(max_length=512, verbose_name='제목', null=True, blank=True)
    type = models.CharField(choices=TypeChoices.choices, max_length=1, blank=True)
    region = models.ForeignKey(Region, verbose_name='지역', null=True, on_delete=models.SET_NULL)
    big_subject = models.ForeignKey(BigSubject, verbose_name='대주제', null=True, on_delete=models.SET_NULL)
    small_subject = models.ManyToManyField(SmallSubject, verbose_name='소주제')
    presentation = models.TextField(verbose_name='제시문', null=True, blank=True)
    question = models.TextField(verbose_name='문제', null=True, blank=True)
    answer = models.TextField(verbose_name='정답', null=True, blank=True)
    scrapped_users = models.ManyToManyField(User, related_name='scrapped_problems', verbose_name='이 문제를 스크랩한 사람들')
    height = models.FloatField(null=True, blank=True, verbose_name='사진 높이')
    width = models.FloatField(null=True, blank=True, verbose_name='사진 넓이')
    presentation_image = models.ImageField(null=True, blank=True, verbose_name='제시문 이미지', height_field='height', width_field='width')
    image_url = models.URLField(null=True, blank=True, verbose_name='사진 url 링크')
    has_image = models.BooleanField(default=False)
    # color = models.CharField(max_length=10, verbose_name='색상', null=True, blank=True)
    year = models.IntegerField(verbose_name='연도', null=True, blank=True)
    real_region = models.ForeignKey(RealRegion, verbose_name='기출 출제 지역', null=True, blank=True, on_delete=models.SET_NULL)
    writer = models.CharField(max_length=64, verbose_name='출제자', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '문제'
        verbose_name_plural = verbose_name


class Summernote(summermodel.AbstractAttachment):
    problem = summermodel.models.ForeignKey(Problem, null=True, blank=True, verbose_name='문제',
                                              on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='원본파일명',
                            help_text="Defaults to filename, if left blank")
    file = models.FileField(
        upload_to=get_attachment_upload_to(),
        storage=get_attachment_storage(),
        unique=True
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '첨부 이미지'
        verbose_name_plural = '첨부 이미지'


class Color(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목', null=True, blank=True)
    color = models.CharField(max_length=6, verbose_name='색상 코드', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '색상'
        verbose_name_plural = '색상'
