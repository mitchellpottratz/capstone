# Generated by Django 2.2.7 on 2019-12-10 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20191209_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='company_users.Company'),
        ),
    ]