# Generated by Django 2.0.5 on 2018-06-22 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0108_auto_20180622_0249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='debitnotecustomer',
            old_name='credit_amount',
            new_name='debit_amount',
        ),
        migrations.RenameField(
            model_name='historicaldebitnotecustomer',
            old_name='credit_amount',
            new_name='debit_amount',
        ),
    ]