# Generated by Django 4.2.3 on 2023-08-01 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlatRate', '0002_calculator_price_calculator_salary_calculator_years_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculator',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 1, 14, 10, 59, 763104, tzinfo=datetime.timezone.utc)),
        ),
    ]
