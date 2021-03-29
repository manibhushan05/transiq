# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0043_remove_topayinvoice_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='manualbooking',
            name='refund_amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='outwardpayment',
            name='is_refund_amount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='outwardpayment',
            name='is_sms_supplier',
            field=models.BooleanField(default=False),
        ),
    ]