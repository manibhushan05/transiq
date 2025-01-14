# Generated by Django 2.0.5 on 2018-11-17 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0128_datatablesfilter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatablesfilter',
            name='table_name',
            field=models.CharField(choices=[('MBS', 'Manual Bookings'), ('INV', 'Invoices'), ('OWP', 'Outward Payments'), ('IWP', 'Inward Payments'), ('CUS', 'Customers'), ('SUP', 'Suppliers'), ('OWN', 'Owners'), ('VEH', 'Vehicles'), ('DRV', 'Driver'), ('BAC', 'Bank Account'), ('INS', 'Invoice Summary'), ('POD', 'POD List'), ('OPR', 'Outward Payment Receipt'), ('LRD', 'Lorry Receipt'), ('GPS', 'GPS Devices')], max_length=15, unique=True),
        ),
    ]
