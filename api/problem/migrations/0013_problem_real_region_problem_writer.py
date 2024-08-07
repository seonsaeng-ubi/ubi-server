# Generated by Django 4.2 on 2024-08-04 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0012_realregion_delete_problemset'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='real_region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='problem.realregion', verbose_name='기출 출제 지역'),
        ),
        migrations.AddField(
            model_name='problem',
            name='writer',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='출제자'),
        ),
    ]
