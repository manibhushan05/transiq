# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 19:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_auto_20170301_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseUpdateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_table', models.CharField(max_length=100)),
                ('old_data', models.TextField()),
                ('new_data', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='database_update', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]