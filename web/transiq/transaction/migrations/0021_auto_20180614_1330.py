# Generated by Django 2.0.5 on 2018-06-14 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0020_merge_20180608_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='is_insured',
            field=models.CharField(blank=True, choices=[('yes', 'YES'), ('no', 'NO')], max_length=4, null=True),
        ),
    ]
