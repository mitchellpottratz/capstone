# Generated by Django 2.2.7 on 2019-12-07 23:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20191207_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 23, 46, 3, 114838, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 23, 46, 3, 114869, tzinfo=utc)),
        ),
    ]
