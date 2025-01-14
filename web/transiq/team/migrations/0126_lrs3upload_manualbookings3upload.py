# Generated by Django 2.0.5 on 2018-10-15 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_remove_s3upload_deleted_on'),
        ('team', '0125_auto_20181003_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='LrS3Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('lr_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.LrNumber')),
                ('s3_upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.S3Upload')),
            ],
        ),
        migrations.CreateModel(
            name='ManualBookingS3Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.ManualBooking')),
                ('s3_upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.S3Upload')),
            ],
        ),
    ]
