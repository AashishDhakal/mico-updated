# Generated by Django 3.1 on 2020-09-24 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_advertisement_popup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='link',
        ),
    ]
