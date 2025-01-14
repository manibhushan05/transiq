# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170222_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('summary', models.BooleanField(default=False)),
                ('successful', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='s3upload',
            name='uuid',
            field=models.CharField(max_length=22, unique=True),
        ),
        migrations.AddField(
            model_name='paymentfile',
            name='upload',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.S3Upload'),
        ),
    ]
