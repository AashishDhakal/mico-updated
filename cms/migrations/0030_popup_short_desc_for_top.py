# Generated by Django 3.1 on 2020-10-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0029_auto_20201014_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='popup',
            name='short_desc_for_top',
            field=models.TextField(default=''),
        ),
    ]
