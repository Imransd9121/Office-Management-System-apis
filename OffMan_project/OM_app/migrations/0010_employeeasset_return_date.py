# Generated by Django 5.1.2 on 2024-10-22 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OM_app', '0009_remove_employeeasset_return_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeasset',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]