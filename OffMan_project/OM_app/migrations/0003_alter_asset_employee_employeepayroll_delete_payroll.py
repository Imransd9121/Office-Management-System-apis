# Generated by Django 5.1.2 on 2024-10-22 05:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OM_app', '0002_remove_asset_asset_description_asset_asset_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='OM_app.employee'),
        ),
        migrations.CreateModel(
            name='EmployeePayroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctc', models.DecimalField(decimal_places=2, max_digits=12)),
                ('basic_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bonus', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pf', models.DecimalField(decimal_places=2, max_digits=10)),
                ('esi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField(default=django.utils.timezone.now)),
                ('is_paid', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payrolls', to='OM_app.employee')),
            ],
        ),
        migrations.DeleteModel(
            name='Payroll',
        ),
    ]
