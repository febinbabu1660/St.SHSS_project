# Generated by Django 4.0.6 on 2022-10-16 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0014_course_course_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
