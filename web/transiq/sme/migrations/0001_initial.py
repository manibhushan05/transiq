# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 17:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsignorConsignee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('consignor', 'consignor'), ('consignee', 'consignee')], max_length=30)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('pin', models.CharField(blank=True, max_length=6, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('tax_id', models.CharField(blank=True, max_length=40, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.City')),
            ],
            options={
                'verbose_name_plural': 'SME Consignor & Consignee Details',
            },
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('primary', 'primary'), ('secondary', 'secondary')], default='secondary', max_length=35, null=True)),
                ('name', models.CharField(blank=True, max_length=70, null=True)),
                ('phone', models.CharField(blank=True, max_length=17, null=True)),
                ('alternate_phone', models.CharField(blank=True, max_length=17, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('alternate_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'SME Contact Details',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('loading', 'loading'), ('unloading', 'unloading')], max_length=30, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('material', models.TextField(blank=True, null=True)),
                ('latitude', models.CharField(blank=True, max_length=30, null=True)),
                ('longitude', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.City')),
                ('contact', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sme.ContactDetails')),
            ],
            options={
                'verbose_name_plural': 'SME Loading & Unloading Points',
            },
        ),
        migrations.CreateModel(
            name='PreferredVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sme_preffered_vehicle', to='utils.VehicleCategory')),
            ],
            options={
                'verbose_name_plural': 'SME Preferred Vehicles',
            },
        ),
        migrations.CreateModel(
            name='Sme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_code', models.CharField(max_length=4, null=True, unique=True)),
                ('latest_transaction_id', models.CharField(blank=True, default='000000000', max_length=30, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('account_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.Bank')),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.Address')),
                ('id_proof', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.IDDetails')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('taxation_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.TaxationID')),
            ],
            options={
                'verbose_name_plural': 'SME Basic Info',
            },
        ),
        migrations.CreateModel(
            name='SmeEnquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('sme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sme.Sme')),
            ],
            options={
                'verbose_name_plural': 'SME Enquiry',
            },
        ),
        migrations.AddField(
            model_name='preferredvehicle',
            name='sme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sme.Sme'),
        ),
        migrations.AddField(
            model_name='location',
            name='sme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sme_loading_unloading', to='sme.Sme'),
        ),
        migrations.AddField(
            model_name='contactdetails',
            name='sme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sme_contact_details', to='sme.Sme'),
        ),
        migrations.AddField(
            model_name='consignorconsignee',
            name='sme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sme.Sme'),
        ),
    ]