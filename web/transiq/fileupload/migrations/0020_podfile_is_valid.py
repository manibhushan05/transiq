# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-10 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0019_auto_20180329_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='podfile',
            name='is_valid',
            field=models.BooleanField(default=False),
        ),
    ]