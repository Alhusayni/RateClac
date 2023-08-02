# Generated by Django 4.2.3 on 2023-08-01 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlatRate', '0005_alter_calculator_price_alter_calculator_salary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculator',
            name='DownPay',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='Price',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='Salary',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='Years',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 1, 15, 12, 51, 275565, tzinfo=datetime.timezone.utc)),
        ),
    ]
