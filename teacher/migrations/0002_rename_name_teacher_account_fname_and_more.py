# Generated by Django 4.0.6 on 2022-10-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher_account',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='teacher_account',
            name='lname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
