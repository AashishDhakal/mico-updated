# Generated by Django 3.1 on 2020-10-06 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0017_auto_20201006_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='is_full',
        ),
    ]
