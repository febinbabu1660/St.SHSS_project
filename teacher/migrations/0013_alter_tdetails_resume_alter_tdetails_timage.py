# Generated by Django 4.0.6 on 2022-11-20 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0012_alter_tdetails_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tdetails',
            name='resume',
            field=models.FileField(upload_to='media/resume/'),
        ),
        migrations.AlterField(
            model_name='tdetails',
            name='timage',
            field=models.FileField(upload_to='media/T_image/'),
        ),
    ]