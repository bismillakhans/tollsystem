# Generated by Django 2.2.6 on 2019-11-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_bank_vehicle_vehiclepass'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='primary',
            field=models.BooleanField(default=False),
        ),
    ]
