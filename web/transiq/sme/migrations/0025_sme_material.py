# Generated by Django 2.0.5 on 2018-09-06 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sme', '0024_auto_20180711_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='sme',
            name='material',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
