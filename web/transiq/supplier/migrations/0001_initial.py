# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 23:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(blank=True, max_length=255, null=True)),
                ('account_holder_name', models.CharField(blank=True, max_length=100, null=True)),
                ('beneficiary_code', models.CharField(blank=True, max_length=100, null=True)),
                ('account_number', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('transaction_type', models.CharField(blank=True, choices=[('neft', 'NEFT'), ('rtgs', 'RTGS'), ('both', 'Both'), ('hdfc_internal_account', 'HDFC Internal Account')], max_length=35, null=True)),
                ('account_type', models.CharField(choices=[('SA', 'Saving Account'), ('CA', 'Current Account'), ('RA', 'Recurring Account')], default='SA', max_length=15, null=True)),
                ('ifsc', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=400, null=True)),
                ('city', models.CharField(blank=True, max_length=70, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('is_verified', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=10, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=15, null=True)),
                ('shipment_datetime', models.DateTimeField(null=True)),
                ('source', models.CharField(blank=True, max_length=200, null=True)),
                ('destination', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('material', models.CharField(blank=True, max_length=400, null=True)),
                ('vendor_weight', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('vendor_rate', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('vendor_detention_charge', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('vendor_other_charge', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('vendor_commission', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('vendor_other_deduction', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('total_amount_vendor', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('vendor_rate_remarks', models.TextField(blank=True, null=True)),
                ('transporter_weight', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('transporter_rate', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('transporter_detention_charge', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('transporter_other_charge', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('transporter_other_deduction', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('total_amount_transporter', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('transporter_rate_remarks', models.TextField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('document_bearer_type', models.CharField(choices=[('owner', 'owner'), ('driver', 'driver'), ('vehicle', 'vehicle'), ('supplier', 'supplier')], max_length=50)),
                ('document_bearer_id', models.PositiveIntegerField()),
                ('document_purpose', models.CharField(max_length=100)),
                ('document_type', models.CharField(blank=True, choices=[('PAN', 'PAN Card'), ('DL', 'Driving Licence'), ('EL', 'Election ID'), ('AC', 'Aadhar Card'), ('PT', 'Passport'), ('RC', 'Ration Card'), ('PUC', 'Puc Certificate'), ('FIT', 'Fitness Certificate'), ('REG', 'Registration Certificate'), ('PERM', 'Permission Certificate'), ('INS', 'Insurance Certificate'), ('DEC', 'Declaration')], max_length=100, null=True)),
                ('document_id', models.CharField(blank=True, max_length=100, null=True)),
                ('document', models.CharField(help_text='s3 file key', max_length=255)),
                ('document_thumb', models.CharField(blank=True, help_text='s3 file key', max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_document', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=35, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('phone', models.CharField(max_length=35, unique=True)),
                ('alt_phone', models.CharField(blank=True, db_index=True, max_length=35, null=True)),
                ('driving_licence_number', models.CharField(blank=True, max_length=50, null=True)),
                ('driving_licence_location', models.CharField(blank=True, max_length=50, null=True)),
                ('driving_licence_validity', models.DateField(blank=True, null=True)),
                ('pan', models.CharField(blank=True, max_length=10, null=True)),
                ('aadhaar_number', models.CharField(blank=True, max_length=12, null=True)),
                ('route', models.CharField(blank=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('account_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.BankAccount')),
                ('driving_licence_docs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.Document')),
            ],
        ),
        migrations.CreateModel(
            name='InwardPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_from', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('datetime', models.DateTimeField(null=True)),
                ('payment_mode', models.CharField(choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('neft', 'NEFT'), ('imps', 'IMPS'), ('rtgs', 'RTGS')], max_length=70, null=True)),
                ('tds_deducted', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('invoice_number', models.CharField(blank=True, max_length=70, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('booking', models.ManyToManyField(related_name='inward_payments', to='supplier.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='OutwardPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_to', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('datetime', models.DateTimeField(null=True)),
                ('payment_mode', models.CharField(choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('neft', 'NEFT'), ('imps', 'IMPS'), ('rtgs', 'RTGS')], max_length=70, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('booking', models.ManyToManyField(related_name='outward_payments', to='supplier.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Primary Phone')),
                ('alt_phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Alternate Phone Number')),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('tds_declaration_validity', models.DateField(blank=True, null=True)),
                ('pan', models.CharField(blank=True, max_length=10, null=True)),
                ('aadhaar_number', models.CharField(blank=True, max_length=12, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('account_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='broker_owner', to='supplier.BankAccount')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_code', models.CharField(max_length=4, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('pan', models.CharField(blank=True, max_length=10, null=True)),
                ('aadhaar_number', models.CharField(blank=True, max_length=12, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='truck_supplier', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('contact_person', models.CharField(blank=True, max_length=70, null=True)),
                ('phone', models.CharField(blank=True, max_length=40, null=True)),
                ('alt_phone', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=18)),
                ('permit_validity', models.DateField(blank=True, null=True)),
                ('permit_category', models.CharField(blank=True, max_length=70, null=True)),
                ('vehicle_capacity', models.IntegerField(blank=True, null=True, verbose_name='Exact Vehicle Capacity in Kg')),
                ('body_type', models.CharField(blank=True, choices=[('open', 'open'), ('closed', 'closed'), ('semi', 'semi'), ('half', 'half'), ('containerized', 'containerized')], max_length=50, null=True)),
                ('chassis_number', models.CharField(blank=True, max_length=255, null=True)),
                ('engine_number', models.CharField(blank=True, max_length=255, null=True)),
                ('insurer', models.CharField(blank=True, max_length=100, null=True)),
                ('insurance_number', models.CharField(blank=True, max_length=30, null=True)),
                ('insurance_validity', models.DateField(blank=True, null=True)),
                ('registration_year', models.DateField(blank=True, null=True)),
                ('registration_validity', models.DateField(blank=True, null=True)),
                ('fitness_certificate_validity_date', models.DateField(blank=True, null=True)),
                ('puc_certificate_validity_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], default='unloaded', max_length=20)),
                ('gps_enabled', models.BooleanField(default=False)),
                ('update_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.Driver')),
                ('fitness_certificate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fit_vehicle', to='supplier.Document')),
                ('insurance_certificate_docs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ins_vehicle', to='supplier.Document')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='broker_vehicle', to='supplier.Owner')),
                ('permit_certificate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perm_vehicle', to='supplier.Document')),
                ('puc_certificate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='puc_vehicle', to='supplier.Document')),
                ('registration_certificate_docs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reg_vehicle', to='supplier.Document')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=100)),
                ('capacity', models.CharField(blank=True, max_length=30, null=True)),
                ('truck_body_type', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('priority', models.CharField(blank=True, max_length=10, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='broker_vehicle_info', to='supplier.VehicleCategory'),
        ),
        migrations.AddField(
            model_name='owner',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.Supplier'),
        ),
        migrations.AddField(
            model_name='owner',
            name='tds_declaration_doc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='declaration_broker_owner', to='supplier.Document'),
        ),
        migrations.AddField(
            model_name='driver',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_driver', to='supplier.Supplier'),
        ),
        migrations.AddField(
            model_name='booking',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transporter_bookings', to='supplier.Driver'),
        ),
        migrations.AddField(
            model_name='booking',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transporter_bookings', to='supplier.Owner'),
        ),
        migrations.AddField(
            model_name='booking',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.Supplier'),
        ),
        migrations.AddField(
            model_name='booking',
            name='transporter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transporter_bookings', to='supplier.Transporter'),
        ),
        migrations.AddField(
            model_name='booking',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transporter_bookings', to='supplier.Vehicle'),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.Supplier'),
        ),
    ]