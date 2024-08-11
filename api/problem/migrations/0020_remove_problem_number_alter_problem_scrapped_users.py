# Generated by Django 4.2 on 2024-08-11 00:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problem', '0019_alter_problem_scrapped_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='number',
        ),
        migrations.AlterField(
            model_name='problem',
            name='scrapped_users',
            field=models.ManyToManyField(blank=True, related_name='scrapped_problems', to=settings.AUTH_USER_MODEL, verbose_name='이 문제를 스크랩한 사람들'),
        ),
    ]