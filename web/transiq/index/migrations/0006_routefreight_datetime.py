# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-01 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20170801_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='routefreight',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
