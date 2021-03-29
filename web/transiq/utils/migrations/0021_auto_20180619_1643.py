# Generated by Django 2.0.5 on 2018-06-19 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utils', '0020_auto_20180514_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='aahooffice',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aaho_office_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aahooffice',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aaho_office_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aahooffice',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='aahooffice',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='address',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bank',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bank',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bank',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bank',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bankname',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank_name_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bankname',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank_name_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bankname',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bankname',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='city',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='district',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='district',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='district',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='iddetails',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_details_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='iddetails',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_details_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='iddetails',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='iddetails',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ifscdetail',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ifsc_detail_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ifscdetail',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ifsc_detail_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ifscdetail',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ifscdetail',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='locality',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locality_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='locality',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='locality',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pincode',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pin_code_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pincode',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pincode',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='state_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='state',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='state_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='state',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='state',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subdistrict',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_district_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subdistrict',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subdistrict',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taxationid',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taxation_id_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='taxationid',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taxation_id_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='taxationid',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='taxationid',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehiclebodycategory',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_body_category_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehiclebodycategory',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_body_category_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehiclebodycategory',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vehiclebodycategory',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehiclecategory',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_category_changed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehiclecategory',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_category_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehiclecategory',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vehiclecategory',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='locality',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='locality_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pincode',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pin_code_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subdistrict',
            name='created_by',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_district_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]