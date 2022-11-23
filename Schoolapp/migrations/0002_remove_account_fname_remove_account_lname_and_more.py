# Generated by Django 4.0.6 on 2022-09-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='account',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='account',
            name='mobile',
        ),
        migrations.AddField(
            model_name='account',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
