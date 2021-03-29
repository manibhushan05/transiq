# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 17:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsLandingPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Us Landing Page',
            },
        ),
        migrations.CreateModel(
            name='DailyRateEnquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=70, null=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('source_of_information', models.CharField(blank=True, choices=[('transporter', 'Transporter'), ('supplier', 'Broker'), ('traffic_person', 'Traffic Person')], max_length=35, null=True)),
                ('loading_point', models.CharField(blank=True, max_length=200, null=True)),
                ('unloading_point', models.CharField(blank=True, max_length=200, null=True)),
                ('material', models.CharField(blank=True, max_length=150, null=True)),
                ('weight', models.CharField(blank=True, max_length=35, null=True)),
                ('rate', models.CharField(blank=True, max_length=10, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True, verbose_name='datetime')),
                ('number_of_truck', models.CharField(blank=True, max_length=5, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('loading_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loading_city', to='utils.City')),
                ('type_of_vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.VehicleCategory')),
                ('unloading_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unloading_city', to='utils.City')),
            ],
            options={
                'verbose_name_plural': 'Daily Rate Enquiry Record',
            },
        ),
        migrations.CreateModel(
            name='EnquiryForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('phone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('loading_point', models.CharField(blank=True, max_length=200, null=True)),
                ('unloading_point', models.CharField(blank=True, max_length=200, null=True)),
                ('material', models.CharField(blank=True, max_length=200, null=True)),
                ('weight', models.CharField(blank=True, max_length=35, null=True)),
                ('date', models.DateField()),
                ('enquiry_date', models.DateField(auto_now_add=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('loading_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enquiry_loading_city', to='utils.City')),
                ('type_of_vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.VehicleCategory')),
                ('unloading_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enquiry_unloading_city', to='utils.City')),
            ],
            options={
                'verbose_name_plural': 'General Enquiry Record',
            },
        ),
    ]