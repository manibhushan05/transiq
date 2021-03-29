# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-06 13:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utils', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentEmploymentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_job_responsibilities', models.TextField(blank=True, null=True, verbose_name='Outline briefly current job responsibilities')),
                ('present_salary', models.IntegerField(default=0, help_text='CTC P.A.')),
                ('role', models.CharField(blank=True, max_length=200, null=True)),
                ('e_shops', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_acquisition', models.CharField(blank=True, max_length=15, null=True)),
                ('date_of_vesting', models.CharField(blank=True, max_length=15, null=True)),
                ('date_of_selling', models.CharField(blank=True, max_length=15, null=True)),
                ('pan', models.CharField(blank=True, max_length=15, null=True)),
                ('id_type', models.CharField(blank=True, max_length=70, null=True)),
                ('id_number', models.CharField(blank=True, max_length=25, null=True)),
                ('pf_account', models.CharField(blank=True, max_length=35, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FitnessDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(decimal_places=2, default=0.0, help_text='Height in Inches', max_digits=8)),
                ('weight', models.DecimalField(decimal_places=2, default=0.0, help_text='Weight in Kgs', max_digits=8)),
                ('blood_group', models.CharField(blank=True, choices=[('o_pos', 'O+'), ('o_neg', 'O-'), ('a_pos', 'A+'), ('a_neg', 'A-'), ('b_pos', 'B+'), ('b_neg', 'B-'), ('ab_pos', 'AB+'), ('ab_neg', 'AB-')], max_length=10, null=True)),
                ('medical_fitness', models.TextField(blank=True, null=True)),
                ('emergency_contact_person_name', models.CharField(blank=True, max_length=35, null=True)),
                ('emergency_contact_person_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('emergency_contact_person_email', models.EmailField(blank=True, max_length=35, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PastEmployment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('leaving_date', models.DateField(blank=True, null=True)),
                ('organisation', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('reporting_manager', models.CharField(blank=True, max_length=100, null=True)),
                ('gross_compensation', models.CharField(blank=True, max_length=20, null=True)),
                ('reason_for_change', models.TextField(blank=True, null=True)),
                ('total_experience', models.CharField(blank=True, help_text='In year and months', max_length=20, null=True)),
                ('relevant_experience', models.CharField(blank=True, help_text='In year and months', max_length=20, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='bankaccount',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='currentaddress',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='currentemployeedetails',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='educationalqualification',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='educationalqualification',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='family',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='joiningdetails',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='pastemployee',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='personaldetail',
            name='employee',
        ),
        migrations.RenameField(
            model_name='employmentagency',
            old_name='name',
            new_name='agency_name',
        ),
        migrations.RenameField(
            model_name='nominee',
            old_name='address_line_1',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='permanentaddress',
            old_name='address_line_1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='alternate_phone',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='mother_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='employmentagency',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='nominee',
            name='address_line_2',
        ),
        migrations.RemoveField(
            model_name='nominee',
            name='address_line_3',
        ),
        migrations.RemoveField(
            model_name='nominee',
            name='state',
        ),
        migrations.RemoveField(
            model_name='permanentaddress',
            name='address_line_2',
        ),
        migrations.RemoveField(
            model_name='permanentaddress',
            name='address_line_3',
        ),
        migrations.RemoveField(
            model_name='permanentaddress',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='permanentaddress',
            name='name',
        ),
        migrations.RemoveField(
            model_name='permanentaddress',
            name='state',
        ),
        migrations.RemoveField(
            model_name='referral',
            name='employee',
        ),
        migrations.AddField(
            model_name='educationaldegree',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='educational_degree', to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='aadhaar',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='bank',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.Bank'),
        ),
        migrations.AddField(
            model_name='employee',
            name='date_of_joining',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='date_of_leaving',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='employment_agency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emp_agency_employee', to='employee.EmploymentAgency'),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('married', 'Married'), ('unmarried', 'Unmarried'), ('divorcee', 'Divorcee')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='pan',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='passport',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='permanent_address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permanent_address_employee', to='employee.PermanentAddress'),
        ),
        migrations.AddField(
            model_name='employee',
            name='referral',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referral_employee', to='employee.Referral'),
        ),
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_designation', to='employee.Designation'),
        ),
        migrations.AlterField(
            model_name='nominee',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.City'),
        ),
        migrations.AlterField(
            model_name='nominee',
            name='percentage_share',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Max share is 100.00', max_digits=8),
        ),
        migrations.AlterField(
            model_name='permanentaddress',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.City'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='food_allowance',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='D. Food Allowance'),
        ),
        migrations.DeleteModel(
            name='BankAccount',
        ),
        migrations.DeleteModel(
            name='CurrentAddress',
        ),
        migrations.DeleteModel(
            name='CurrentEmployeeDetails',
        ),
        migrations.DeleteModel(
            name='EducationalQualification',
        ),
        migrations.DeleteModel(
            name='Family',
        ),
        migrations.DeleteModel(
            name='JoiningDetails',
        ),
        migrations.DeleteModel(
            name='PastEmployee',
        ),
        migrations.DeleteModel(
            name='PersonalDetail',
        ),
        migrations.AddField(
            model_name='currentemploymentdetails',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_employee_department', to='employee.Department'),
        ),
        migrations.AddField(
            model_name='currentemploymentdetails',
            name='designation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_employee_designation', to='employee.Designation'),
        ),
        migrations.AddField(
            model_name='currentemploymentdetails',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_emp_details', to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_department', to='employee.Department'),
        ),
        migrations.AddField(
            model_name='employee',
            name='fitness_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.FitnessDetail'),
        ),
        migrations.AddField(
            model_name='employee',
            name='past_employment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='past_emp_employee', to='employee.PastEmployment'),
        ),
    ]