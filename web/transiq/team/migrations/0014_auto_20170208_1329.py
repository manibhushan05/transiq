# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-08 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0013_auto_20170206_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manualbooking',
            name='outward_payment_status',
            field=models.CharField(choices=[('no_payment_made', 'NoPaymentMade'), ('partial', 'Partial'), ('complete', 'Complete'), ('excess', 'Excess')], default='no_payment_made', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='manualbooking',
            name='pod_status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('loading', 'Loading'), ('in_transit', 'In-Transit'), ('unloading', 'Unloading'), ('completed', 'Delivered')], default='pending', max_length=20, null=True),
        ),
    ]