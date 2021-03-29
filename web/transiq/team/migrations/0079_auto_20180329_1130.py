# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-29 11:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0078_auto_20180328_1204'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalTBBInvoice',
            new_name='HistoricalInvoice',
        ),
        migrations.RenameModel(
            old_name='TBBInvoice',
            new_name='Invoice',
        ),
        migrations.AlterModelOptions(
            name='historicalinvoice',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical invoice'},
        ),
    ]