# Generated by Django 2.2.7 on 2019-12-07 23:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0012_auto_20191207_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 23, 49, 18, 969109, tzinfo=utc)),
        ),
    ]
