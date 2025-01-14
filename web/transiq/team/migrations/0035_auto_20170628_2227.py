# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-28 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0005_aahooffice_branch_name'),
        ('team', '0034_nontransactionalexpense'),
    ]

    operations = [
        migrations.AddField(
            model_name='lrnumber',
            name='consignee_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='consignee_city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='consignee_city_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lr_consignee_manual_full', to='utils.City'),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='consignee_cst_tin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='consignee_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='consignee_phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='consignee_pin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='consignor_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='consignor_city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='consignor_city_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lr_consignor_manual_full', to='utils.City'),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='consignor_cst_tin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='consignor_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='consignor_phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='consignor_pin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='from_city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='insurance_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='insurance_policy_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='insurance_provider',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='insurance_risk',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='insured_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='is_insured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='liability_of_service_tax',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='to_city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lrnumber',
            name='unloading_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
