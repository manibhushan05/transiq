# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 02:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0005_aahooffice_branch_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclecategory',
            name='vehicle_type',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
