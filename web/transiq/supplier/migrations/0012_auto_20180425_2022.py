# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-25 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0011_auto_20180425_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactperson',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalcontactperson',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
