# Generated by Django 2.2.7 on 2019-12-09 17:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_users', '0017_auto_20191209_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateinfo',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 17, 3, 14, 530779, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='candidateinfo',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 17, 3, 14, 530812, tzinfo=utc)),
        ),
    ]