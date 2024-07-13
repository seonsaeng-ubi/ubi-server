# Generated by Django 4.2 on 2024-07-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0007_alter_problem_presentation_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='height',
            field=models.FloatField(blank=True, null=True, verbose_name='사진 높이'),
        ),
        migrations.AddField(
            model_name='problem',
            name='width',
            field=models.FloatField(blank=True, null=True, verbose_name='사진 넓이'),
        ),
    ]
