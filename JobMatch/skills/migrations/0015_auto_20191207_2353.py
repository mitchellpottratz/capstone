# Generated by Django 2.2.7 on 2019-12-07 23:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0014_auto_20191207_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 23, 53, 5, 318722, tzinfo=utc)),
        ),
    ]
