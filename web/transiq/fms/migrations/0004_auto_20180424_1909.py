# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-24 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0003_auto_20180419_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalrequirement',
            name='material',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='material',
            field=models.CharField(max_length=35, null=True),
        ),
    ]
