# Generated by Django 5.1.2 on 2024-10-22 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OM_app', '0004_remove_asset_assigned_date_remove_asset_employee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeasset',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Asset', to='OM_app.asset', unique=True),
        ),
    ]
