# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-25 20:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0010_auto_20180425_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactperson',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contactperson',
            name='name',
        ),
        migrations.RemoveField(
            model_name='historicalcontactperson',
            name='email',
        ),
        migrations.RemoveField(
            model_name='historicalcontactperson',
            name='name',
        ),
    ]
