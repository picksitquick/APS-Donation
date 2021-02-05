# Generated by Django 3.1.5 on 2021-02-04 21:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('APS_app', '0004_clothes_donator_food_donator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothes_donator',
            name='medical_docs',
        ),
        migrations.RemoveField(
            model_name='food_donator',
            name='medical_docs',
        ),
        migrations.AddField(
            model_name='food_donator',
            name='cooking_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='clothes_donator',
            name='user_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='food_donator',
            name='user_name',
            field=models.CharField(max_length=255),
        ),
    ]