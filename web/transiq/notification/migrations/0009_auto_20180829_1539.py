# Generated by Django 2.0.5 on 2018-08-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0008_auto_20180619_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmobiledevice',
            name='app',
            field=models.CharField(choices=[('AS', 'Aaho Sales'), ('AC', 'Aaho Customer'), ('AO', 'Aaho Owner'), ('AE', 'Aaho Employee')], default='AC', max_length=2),
        ),
        migrations.AlterField(
            model_name='mobiledevice',
            name='app',
            field=models.CharField(choices=[('AS', 'Aaho Sales'), ('AC', 'Aaho Customer'), ('AO', 'Aaho Owner'), ('AE', 'Aaho Employee')], default='AC', max_length=2),
        ),
    ]
