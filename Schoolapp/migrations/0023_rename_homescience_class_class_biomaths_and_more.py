# Generated by Django 4.0.6 on 2022-11-17 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Schoolapp', '0022_alter_sdetails_dob'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomeScience_class',
            new_name='class_Biomaths',
        ),
        migrations.RenameModel(
            old_name='Bio_class',
            new_name='class_Commerce',
        ),
        migrations.RenameModel(
            old_name='Commerce_class',
            new_name='class_HomeScience',
        ),
        migrations.RenameModel(
            old_name='Humanities_class',
            new_name='class_Humanities',
        ),
    ]
