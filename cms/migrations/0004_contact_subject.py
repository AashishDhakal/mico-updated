# Generated by Django 3.1.1 on 2020-09-08 12:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20200829_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=datetime.datetime(2020, 9, 8, 12, 39, 38, 654572, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
