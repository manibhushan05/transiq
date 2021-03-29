# Generated by Django 2.0.5 on 2019-03-13 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0028_auto_20190313_0105'),
        ('fms', '0022_merge_20180927_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalrequirementquote',
            name='supplier',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='supplier.Supplier'),
        ),
        migrations.AddField(
            model_name='requirementquote',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_quote', to='supplier.Supplier'),
        ),
    ]