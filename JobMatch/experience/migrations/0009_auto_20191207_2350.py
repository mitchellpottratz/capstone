# Generated by Django 2.2.7 on 2019-12-07 23:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0008_auto_20191207_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 23, 50, 41, 61180, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='experience',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 23, 50, 41, 61228, tzinfo=utc)),
        ),
    ]
