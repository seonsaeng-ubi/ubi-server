# Generated by Django 4.2 on 2024-08-04 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0013_problem_real_region_problem_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='color',
        ),
        migrations.AddField(
            model_name='problem',
            name='has_image',
            field=models.BooleanField(default=False),
        ),
    ]