# Generated by Django 2.0.5 on 2018-06-18 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0009_broker_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='broker',
            options={'ordering': ('-id',), 'verbose_name_plural': 'Broker Basic Info'},
        ),
    ]