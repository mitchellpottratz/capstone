# Generated by Django 2.2.7 on 2019-12-08 17:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20191207_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 8, 17, 54, 6, 336254, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 8, 17, 54, 6, 336306, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
    ]