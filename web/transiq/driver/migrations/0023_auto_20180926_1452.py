# Generated by Django 2.0.5 on 2018-09-26 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0022_driver_pan'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ('-id',), 'verbose_name_plural': 'Driver Basic Info'},
        ),
    ]