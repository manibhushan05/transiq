# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0022_auto_20170224_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='manualbooking',
            name='is_advance',
            field=models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=20),
        ),
    ]