# Generated by Django 2.0.5 on 2018-09-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0020_auto_20180926_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingstatusesmappinglocation',
            name='latitude',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='bookingstatusesmappinglocation',
            name='longitude',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='historicalbookingstatusesmappinglocation',
            name='latitude',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='historicalbookingstatusesmappinglocation',
            name='longitude',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]