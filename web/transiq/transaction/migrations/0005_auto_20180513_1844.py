# Generated by Django 2.0.2 on 2018-05-13 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_auto_20170219_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='is_insured',
            field=models.CharField(blank=True, choices=[('yes', 'YES'), ('no', 'NO')], max_length=4, null=True),
        ),
    ]
