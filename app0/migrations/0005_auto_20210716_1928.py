# Generated by Django 3.2.5 on 2021-07-16 13:58

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app0', '0004_auto_20210716_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='current_UserNames',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), default=None, null=True, size=None),
        ),
        migrations.AddField(
            model_name='room',
            name='fishTotalScore',
            field=models.JSONField(default=dict, null=True),
        ),
    ]
