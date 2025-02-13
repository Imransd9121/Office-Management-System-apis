# Generated by Django 5.1.2 on 2024-10-21 13:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('position', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('asset_id', models.AutoField(primary_key=True, serialize=False)),
                ('asset_type', models.CharField(choices=[('Laptop', 'Laptop'), ('Phone', 'Phone'), ('Monitor', 'Monitor'), ('Other', 'Other')], max_length=50)),
                ('asset_description', models.CharField(blank=True, max_length=255, null=True)),
                ('serial_number', models.CharField(max_length=100, unique=True)),
                ('assigned_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OM_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bonus', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('deductions', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('net_pay', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('pay_period_start', models.DateField()),
                ('pay_period_end', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OM_app.employee')),
            ],
        ),
    ]
