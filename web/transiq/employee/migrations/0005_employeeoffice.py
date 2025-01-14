# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-20 12:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0003_databaseupdatelog_fieldchangelog'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0004_auto_20170407_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_office', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_office', to='employee.Employee')),
                ('office', models.ManyToManyField(to='utils.AahoOffice')),
            ],
        ),
    ]
