# Generated by Django 4.2 on 2024-07-07 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0005_alter_problem_small_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='presentation_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='제시문 이미지'),
        ),
    ]
