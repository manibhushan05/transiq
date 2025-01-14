# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-13 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0087_auto_20180411_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='consignee_address',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='consignee_city',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='consignee_city_fk',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='consignee_cst_tin',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='consignee_name',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='consignee_phone',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='consignee_pin',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='consignor_address',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='consignor_city',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='consignor_city_fk',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='consignor_cst_tin',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='consignor_name',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='consignor_phone',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='consignor_pin',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='from_city',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='insurance_date',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='insurance_policy_number',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='insurance_provider',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='insurance_risk',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='insured_amount',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='is_insured',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='liability_of_service_tax',
        ),
        migrations.RemoveField(
            model_name='historicallrnumber',
            name='to_city',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='consignee_address',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='consignee_city',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='consignee_city_fk',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='consignee_cst_tin',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='consignee_name',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='consignee_phone',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='consignee_pin',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='consignor_address',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='consignor_city',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='consignor_city_fk',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='consignor_cst_tin',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='consignor_name',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='consignor_phone',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='consignor_pin',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='from_city',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='insurance_date',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='insurance_policy_number',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='insurance_provider',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='insurance_risk',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='insured_amount',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='is_insured',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='liability_of_service_tax',
        ),
        migrations.RemoveField(
            model_name='lrnumber',
            name='to_city',
        ),
        migrations.AddField(
            model_name='historicallrnumber',
            name='pod_status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('unverified', 'Unverified'), ('rejected', 'Rejected'), ('completed', 'Delivered')], default='pending', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='pod_status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('unverified', 'Unverified'), ('rejected', 'Rejected'), ('completed', 'Delivered')], default='pending', max_length=20, null=True),
        ),
    ]
