# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-14 12:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_s3upload_is_valid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team', '0070_manualbooking_is_print_payment_mode_instruction'),
        ('fileupload', '0017_auto_20180228_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceReceiptFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(blank=True, max_length=50, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('serial', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('s3_upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upload_invoice_receipt', to='api.S3Upload')),
                ('tbb_invoice_receipt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.Invoice')),
                ('to_pay_invoice_receipt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.ToPayInvoice')),
                ('uploaded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
