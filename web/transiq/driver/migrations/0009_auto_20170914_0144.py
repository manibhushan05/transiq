# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0008_auto_20170822_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecuGPSDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('device_id', models.CharField(max_length=50)),
                ('imei', models.CharField(max_length=50)),
                ('driver_name', models.CharField(blank=True, max_length=50, null=True)),
                ('driver_number', models.CharField(blank=True, max_length=20, null=True)),
                ('number_verified', models.BooleanField(default=False)),
                ('driving_licence_number', models.CharField(blank=True, max_length=20, null=True)),
                ('vehicle_number', models.CharField(blank=True, max_length=40, null=True)),
                ('vehicle_type', models.CharField(blank=True, max_length=40, null=True)),
                ('vehicle_status', models.CharField(choices=[(b'unloaded', b'unloaded'), (b'loading', b'loading'), (b'loaded', b'loaded'), (b'unloading', b'unloading')], default=b'unloaded', max_length=20)),
                ('location_time', models.DateTimeField(null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('status', models.CharField(max_length=300, null=True)),
                ('inactive_sms_sent_at', models.DateTimeField(null=True)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='driver.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='SecuGPSDeviceLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('gps_log_id', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(help_text=b'log time')),
                ('vehicle_id', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('speed', models.FloatField(blank=True, null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('status', models.CharField(max_length=300, null=True)),
                ('driver_name', models.CharField(blank=True, max_length=50, null=True)),
                ('driver_number', models.CharField(blank=True, max_length=20, null=True)),
                ('driving_licence_number', models.CharField(blank=True, max_length=20, null=True)),
                ('vehicle_number', models.CharField(blank=True, max_length=40, null=True)),
                ('vehicle_type', models.CharField(blank=True, max_length=40, null=True)),
                ('vehicle_status', models.CharField(blank=True, choices=[(b'unloaded', b'unloaded'), (b'loading', b'loading'), (b'loaded', b'loaded'), (b'unloading', b'unloading')], max_length=20, null=True)),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device_logs', to='driver.SecuGPSDevice')),
            ],
            options={
                'verbose_name': 'Secu GPS Device Log',
                'verbose_name_plural': 'Secu GPS Device Logs',
            },
        ),
        migrations.AlterModelOptions(
            name='tempogogpsdevicelog',
            options={'verbose_name': 'TempoGO GPS Device Log', 'verbose_name_plural': 'TempoGO GPS Device Logs'},
        ),
        migrations.AlterUniqueTogether(
            name='secugpsdevicelog',
            unique_together=set([('gps_log_id', 'datetime')]),
        ),
    ]
