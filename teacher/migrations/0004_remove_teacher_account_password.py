# Generated by Django 4.0.6 on 2022-10-10 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_remove_teacher_account_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher_account',
            name='password',
        ),
    ]
