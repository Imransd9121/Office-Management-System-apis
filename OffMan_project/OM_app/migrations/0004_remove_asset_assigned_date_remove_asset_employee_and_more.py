# Generated by Django 5.1.2 on 2024-10-22 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OM_app', '0003_alter_asset_employee_employeepayroll_delete_payroll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='assigned_date',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='return_date',
        ),
        migrations.CreateModel(
            name='EmployeeAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Asset', to='OM_app.asset')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Employee_assets', to='OM_app.employee')),
            ],
        ),
    ]