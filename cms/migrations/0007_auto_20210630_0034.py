# Generated by Django 3.1.6 on 2021-06-29 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_doctor_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='picture',
            new_name='profile_pic',
        ),
    ]
