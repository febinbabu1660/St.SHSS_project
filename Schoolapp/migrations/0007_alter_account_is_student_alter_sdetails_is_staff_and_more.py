# Generated by Django 4.0.6 on 2022-10-06 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0006_remove_sdetails_email_remove_sdetails_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='sdetails',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sdetails',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
    ]