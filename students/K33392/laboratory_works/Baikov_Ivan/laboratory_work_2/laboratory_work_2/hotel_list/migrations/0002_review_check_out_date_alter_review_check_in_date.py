# Generated by Django 4.2.7 on 2023-11-14 00:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='check_out_date',
            field=models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='review',
            name='check_in_date',
            field=models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0)),
        ),
    ]
