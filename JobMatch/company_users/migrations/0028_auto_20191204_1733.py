# Generated by Django 2.2.7 on 2019-12-04 17:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company_users', '0027_auto_20191204_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 4, 17, 33, 37, 430261, tzinfo=utc)),
        ),
    ]