# Generated by Django 2.0.5 on 2018-06-22 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0021_auto_20180619_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Address'},
        ),
    ]