# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-25 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0062_auto_20180119_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inwardpayment',
            name='cheque_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pendinginwardpaymententry',
            name='payment_mode',
            field=models.CharField(choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('neft', 'NEFT'), ('rtgs', 'RTGS'), ('hdfc_internal_account', 'HDFC')], max_length=50, null=True),
        ),
    ]
