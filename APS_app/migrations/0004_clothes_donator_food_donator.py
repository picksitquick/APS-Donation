# Generated by Django 3.1.5 on 2021-02-03 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APS_app', '0003_auto_20210204_0208'),
    ]

    operations = [
        migrations.CreateModel(
            name='food_donator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('food_type', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('medical_docs', models.ImageField(upload_to='medical_docs_pic')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='clothes_donator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('clothes_type', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('medical_docs', models.ImageField(upload_to='medical_docs_pic')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]