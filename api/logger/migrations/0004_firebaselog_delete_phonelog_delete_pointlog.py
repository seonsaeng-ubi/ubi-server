# Generated by Django 4.2 on 2024-06-08 19:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logger', '0003_alter_emaillog_id_alter_phonelog_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirebaseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True, verbose_name='제목')),
                ('body', models.TextField(blank=True, max_length=1024, null=True, verbose_name='내용')),
                ('status', models.CharField(blank=True, choices=[('S', '성공'), ('F', '실패')], editable=False, max_length=1, null=True, verbose_name='상태')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('to', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='유저')),
            ],
            options={
                'verbose_name': '푸시 알림',
                'verbose_name_plural': '푸시 알림',
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='PhoneLog',
        ),
        migrations.DeleteModel(
            name='PointLog',
        ),
    ]
