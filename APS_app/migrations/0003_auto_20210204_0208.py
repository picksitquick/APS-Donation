# Generated by Django 3.1.5 on 2021-02-03 20:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APS_app', '0002_blood_donate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blood_donate',
            new_name='blood_donator',
        ),
    ]
