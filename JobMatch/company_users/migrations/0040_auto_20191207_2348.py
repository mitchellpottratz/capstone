# Generated by Django 2.2.7 on 2019-12-07 23:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company_users', '0039_auto_20191207_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 23, 48, 33, 191162, tzinfo=utc)),
        ),
    ]
