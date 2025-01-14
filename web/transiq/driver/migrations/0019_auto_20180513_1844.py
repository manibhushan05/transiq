# Generated by Django 2.0.2 on 2018-05-13 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0018_historicalgpsdevice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverappuser',
            name='vehicle_status',
            field=models.CharField(choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], default='unloaded', max_length=20),
        ),
        migrations.AlterField(
            model_name='gpsdevice',
            name='vehicle_status',
            field=models.CharField(choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], default='unloaded', max_length=20),
        ),
        migrations.AlterField(
            model_name='gpsdevicelog',
            name='datetime',
            field=models.DateTimeField(help_text='log time'),
        ),
        migrations.AlterField(
            model_name='gpsdevicelog',
            name='vehicle_id',
            field=models.CharField(help_text='imei or uuid generated on phone', max_length=50),
        ),
        migrations.AlterField(
            model_name='gpsdevicelog',
            name='vehicle_status',
            field=models.CharField(blank=True, choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='gpslognew',
            name='datetime',
            field=models.DateTimeField(help_text='log time'),
        ),
        migrations.AlterField(
            model_name='gpslognew',
            name='device_id',
            field=models.CharField(help_text='imei or uuid generated on phone', max_length=50),
        ),
        migrations.AlterField(
            model_name='gpslognew',
            name='vehicle_status',
            field=models.CharField(blank=True, choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='historicalgpsdevice',
            name='vehicle_status',
            field=models.CharField(choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], default='unloaded', max_length=20),
        ),
        migrations.AlterField(
            model_name='mahindragpsdevice',
            name='vehicle_status',
            field=models.CharField(choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], default='unloaded', max_length=20),
        ),
        migrations.AlterField(
            model_name='mahindragpsdevicelog',
            name='datetime',
            field=models.DateTimeField(help_text='log time'),
        ),
        migrations.AlterField(
            model_name='mahindragpsdevicelog',
            name='vehicle_status',
            field=models.CharField(blank=True, choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='secugpsdevice',
            name='vehicle_status',
            field=models.CharField(choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], default='unloaded', max_length=20),
        ),
        migrations.AlterField(
            model_name='secugpsdevicelog',
            name='datetime',
            field=models.DateTimeField(help_text='log time'),
        ),
        migrations.AlterField(
            model_name='secugpsdevicelog',
            name='vehicle_status',
            field=models.CharField(blank=True, choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tempogogpsdevice',
            name='vehicle_status',
            field=models.CharField(choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], default='unloaded', max_length=20),
        ),
        migrations.AlterField(
            model_name='tempogogpsdevicelog',
            name='datetime',
            field=models.DateTimeField(help_text='log time'),
        ),
        migrations.AlterField(
            model_name='tempogogpsdevicelog',
            name='vehicle_status',
            field=models.CharField(blank=True, choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tracknovategpsdevice',
            name='vehicle_status',
            field=models.CharField(choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], default='unloaded', max_length=20),
        ),
        migrations.AlterField(
            model_name='tracknovategpsdevicelog',
            name='datetime',
            field=models.DateTimeField(help_text='log time'),
        ),
        migrations.AlterField(
            model_name='tracknovategpsdevicelog',
            name='vehicle_status',
            field=models.CharField(blank=True, choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='waytrackergpsdevice',
            name='vehicle_status',
            field=models.CharField(choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], default='unloaded', max_length=20),
        ),
        migrations.AlterField(
            model_name='waytrackergpsdevicelog',
            name='datetime',
            field=models.DateTimeField(help_text='log time'),
        ),
        migrations.AlterField(
            model_name='waytrackergpsdevicelog',
            name='vehicle_status',
            field=models.CharField(blank=True, choices=[('unloaded', 'unloaded'), ('loading', 'loading'), ('loaded', 'loaded'), ('unloading', 'unloading')], max_length=20, null=True),
        ),
    ]
