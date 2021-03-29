# Generated by Django 2.0.5 on 2018-06-19 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0009_auto_20180619_1643'),
        ('team', '0100_auto_20180618_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingconsignorconsignee',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='changed_by_booking_consignor_consignee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookingconsignorconsignee',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_booking_consignor_consignee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookinginsurance',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='changed_by_booking_booking_insurance', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookinginsurance',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_booking_insurance', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deleteddata',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deleted_data_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deleteddata',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deleteddata',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='invoicesummary',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_summary_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='nontransactionalexpense',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='non_transactional_changed_by', to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='notifycompletedtaskemail',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_complete_task_email_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notifycompletedtaskemail',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_complete_task_email_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rejectedpod',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='changed_by_rejected_pod', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rejectedpod',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_rejected_pod', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='creditnotecustomer',
            name='changed_by',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credit_note_customer_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='creditnotecustomer',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credit_note_customer_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='creditnotecustomerdirectadvance',
            name='changed_by',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credit_note_customer_advance_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='creditnotecustomerdirectadvance',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credit_note_customer_advance_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='creditnotesupplier',
            name='changed_by',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credit_note_supplier_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='creditnotesupplier',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credit_note_supplier_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='debitnotecustomer',
            name='changed_by',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debit_note_customer_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='debitnotecustomer',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debit_note_customer_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='debitnotesupplier',
            name='changed_by',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debit_note_supplier_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='debitnotesupplier',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debit_note_supplier_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='debitnotesupplierdirectadvance',
            name='changed_by',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debit_note_supplier_advance_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='debitnotesupplierdirectadvance',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debit_note_supplier_advance_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invoicesummary',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_summary_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inwardpayment',
            name='changed_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inward_payment_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inwardpayment',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inward_payment_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lrnumber',
            name='changed_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lr_number_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lrnumber',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lr_number_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='manualbooking',
            name='changed_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manual_booking_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='manualbooking',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manual_booking_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='outwardpayment',
            name='changed_by',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outward_payment_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='outwardpayment',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outward_payment_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='outwardpaymentbill',
            name='changed_by',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outward_payment_bill_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='outwardpaymentbill',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outward_payment_bill_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rejectedpod',
            name='rejected_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='rejected_by_rejected_pod', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topayinvoice',
            name='changed_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_pay_invoice_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topayinvoice',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_pay_invoice_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]