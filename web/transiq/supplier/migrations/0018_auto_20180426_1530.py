# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-26 15:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0017_auto_20180426_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalvehicle',
            name='permit_validity',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='permit_validity',
        ),
        migrations.AlterField(
            model_name='driverphone',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter valid phone number', regex='^\\d{10}$')]),
        ),
        migrations.AlterField(
            model_name='historicaldriverphone',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter valid phone number', regex='^\\d{10}$')]),
        ),
        migrations.AlterField(
            model_name='historicalsupplier',
            name='code',
            field=models.CharField(db_index=True, max_length=4, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=4, message='Supplier code must be exactly 4 Letter'), django.core.validators.MaxLengthValidator(limit_value=4, message='Supplier code must be exactly 4 Letter')]),
        ),
        migrations.AlterField(
            model_name='historicalsupplier',
            name='pin',
            field=models.CharField(blank=True, max_length=6, null=True, validators=[django.core.validators.RegexValidator(message='PIN code must be 6 digits', regex='\\d{6}$')]),
        ),
        migrations.AlterField(
            model_name='historicalvehicle',
            name='vehicle_capacity',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Exact Vehicle Capacity in Kg'),
        ),
        migrations.AlterField(
            model_name='historicalvehicle',
            name='vehicle_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Please enter valid vehicle number without any special character or space', regex='^[a-zA-z]{2}\\d{1,2}[a-zA-z]{0,3}\\d{4}$')]),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='aaho_office',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_aaho_office', to='utils.AahoOffice'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='code',
            field=models.CharField(max_length=4, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=4, message='Supplier code must be exactly 4 Letter'), django.core.validators.MaxLengthValidator(limit_value=4, message='Supplier code must be exactly 4 Letter')]),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='pin',
            field=models.CharField(blank=True, max_length=6, null=True, validators=[django.core.validators.RegexValidator(message='PIN code must be 6 digits', regex='\\d{6}$')]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_capacity',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Exact Vehicle Capacity in Kg'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Please enter valid vehicle number without any special character or space', regex='^[a-zA-z]{2}\\d{1,2}[a-zA-z]{0,3}\\d{4}$')]),
        ),
    ]
