# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 12:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0024_auto_20170303_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lrnumber',
            name='upload',
        ),
    ]