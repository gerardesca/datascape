# Generated by Django 5.0.4 on 2024-04-21 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='device type')),
                ('app_name', models.CharField(max_length=400, unique=True, verbose_name='app name')),
                ('device_class', models.CharField(max_length=400, verbose_name='device class')),
                ('daq_daemon', models.BooleanField(default=True, verbose_name='daq daemon')),
                ('single_thread', models.BooleanField(default=True, verbose_name='single thread')),
            ],
        ),
    ]