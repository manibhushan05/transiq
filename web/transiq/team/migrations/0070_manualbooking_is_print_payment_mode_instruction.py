# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-13 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0069_auto_20180308_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='manualbooking',
            name='is_print_payment_mode_instruction',
            field=models.BooleanField(default=False),
        ),
    ]
