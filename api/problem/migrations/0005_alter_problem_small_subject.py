# Generated by Django 4.2 on 2024-06-30 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0004_alter_problem_problem_set_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='small_subject',
            field=models.ManyToManyField(to='problem.smallsubject', verbose_name='소주제'),
        ),
    ]