# Generated by Django 4.2 on 2024-08-17 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_setting_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name': '버전', 'verbose_name_plural': '버전'},
        ),
        migrations.RemoveField(
            model_name='setting',
            name='setting',
        ),
    ]
