# Generated by Django 4.0.6 on 2022-11-03 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0020_bio_class_commerce_class_homescience_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(null=True),
        ),
    ]