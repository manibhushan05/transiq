# Generated by Django 2.0.5 on 2018-08-02 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_auto_20180802_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingstatuses',
            name='status',
            field=models.CharField(choices=[('confirmed', 'Confirmed'), ('loaded', 'Loaded'), ('lr_generated', 'Lr Generated'), ('advance_paid', 'Advance_Paid'), ('reconciled', 'Reconciled'), ('unloaded', 'Unloaded'), ('pod_uploaded', 'PoD Uploaded'), ('pod_verified', 'PoD Verified'), ('invoice_raised', 'Invoice Raised'), ('invoice_confirmed', 'Invoice Confirmed'), ('balance_paid', 'Balance Paid'), ('party_invoice_sent', 'Party Invoice Sent'), ('inward_followup', 'Inward Followup'), ('complete', 'Complete')], default='confirmed', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='bookingstatusesmapping',
            name='stage',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('done', 'Done'), ('reverted', 'Reverted'), ('planned', 'Planned')], default='in_progress', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='employeeroles',
            name='role',
            field=models.CharField(choices=[('office_data_entry', 'Office Data Entry'), ('ops_executive', 'Ops Executive'), ('accounts_payable', 'Accounts Payable'), ('accounts_receivable', 'Accounts Receivable'), ('sales', 'Sales'), ('traffic', 'Traffic'), ('city_head', 'City Head')], default='office_data_entry', max_length=35, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='historicalbookingstatuses',
            name='status',
            field=models.CharField(choices=[('confirmed', 'Confirmed'), ('loaded', 'Loaded'), ('lr_generated', 'Lr Generated'), ('advance_paid', 'Advance_Paid'), ('reconciled', 'Reconciled'), ('unloaded', 'Unloaded'), ('pod_uploaded', 'PoD Uploaded'), ('pod_verified', 'PoD Verified'), ('invoice_raised', 'Invoice Raised'), ('invoice_confirmed', 'Invoice Confirmed'), ('balance_paid', 'Balance Paid'), ('party_invoice_sent', 'Party Invoice Sent'), ('inward_followup', 'Inward Followup'), ('complete', 'Complete')], default='confirmed', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='historicalbookingstatusesmapping',
            name='stage',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('done', 'Done'), ('reverted', 'Reverted'), ('planned', 'Planned')], default='in_progress', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='historicalemployeeroles',
            name='role',
            field=models.CharField(choices=[('office_data_entry', 'Office Data Entry'), ('ops_executive', 'Ops Executive'), ('accounts_payable', 'Accounts Payable'), ('accounts_receivable', 'Accounts Receivable'), ('sales', 'Sales'), ('traffic', 'Traffic'), ('city_head', 'City Head')], db_index=True, default='office_data_entry', max_length=35, null=True),
        ),
    ]