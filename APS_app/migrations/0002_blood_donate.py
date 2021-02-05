# Generated by Django 3.1.5 on 2021-02-03 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APS_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blood_donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('blood_type', models.CharField(max_length=255)),
                ('medical_hist', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('medical_docs', models.ImageField(upload_to='medical_docs_pic')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]