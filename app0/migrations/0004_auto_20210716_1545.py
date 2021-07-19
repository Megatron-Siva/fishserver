# Generated by Django 3.2.5 on 2021-07-16 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app0', '0003_auto_20210716_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='dayStat',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='fishCount',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='fishScore',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='teamName_MembersUserName_dict',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='teamName_leadersUserName_dict',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='userName_teamName_dict',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='userNames_ChannelName_dict',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='room',
            name='userNames_UserGroups_dict',
            field=models.JSONField(default=dict),
        ),
    ]
