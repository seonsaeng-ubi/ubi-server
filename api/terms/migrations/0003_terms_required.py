# Generated by Django 4.2 on 2024-07-18 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terms', '0002_alter_terms_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='terms',
            name='required',
            field=models.BooleanField(blank=True, null=True, verbose_name='필수'),
        ),
    ]
