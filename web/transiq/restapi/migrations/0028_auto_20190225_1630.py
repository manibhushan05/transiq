# Generated by Django 2.0.2 on 2019-02-25 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0027_historicalsmepaymentfollowupcomments_smepaymentfollowupcomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsmepaymentfollowupcomments',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smepaymentfollowupcomments',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
