# Generated by Django 2.0.2 on 2018-05-13 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0021_auto_20180410_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverfile',
            name='document_category',
            field=models.CharField(choices=[('PAN', 'PAN Card'), ('DL', 'Driving Licence'), ('EL', 'Election ID'), ('AC', 'Aadhar Card'), ('PT', 'Passport'), ('RC', 'Ration Card')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='ownerfile',
            name='document_category',
            field=models.CharField(choices=[('PAN', 'PAN Card'), ('DL', 'Driving Licence'), ('EL', 'Election ID'), ('AC', 'Aadhar Card'), ('PT', 'Passport'), ('RC', 'Ration Card'), ('DEC', 'Declaration')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='podfile',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pod_file_uploaded_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='podfile',
            name='verified_by',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pod_file_verified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vehiclefile',
            name='document_category',
            field=models.CharField(choices=[('PUC', 'Puc Certificate'), ('FIT', 'Fitness Certificate'), ('REG', 'Registration Certificate'), ('PERM', 'Permission Certificate'), ('INS', 'Insurance Certificate')], max_length=70, null=True),
        ),
    ]
