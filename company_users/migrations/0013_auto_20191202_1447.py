# Generated by Django 2.2.7 on 2019-12-02 14:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company_users', '0012_auto_20191201_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 2, 14, 47, 5, 291111, tzinfo=utc)),
        ),
    ]