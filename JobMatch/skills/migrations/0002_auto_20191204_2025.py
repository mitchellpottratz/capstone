# Generated by Django 2.2.7 on 2019-12-04 20:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 4, 20, 25, 11, 160760, tzinfo=utc)),
        ),
    ]