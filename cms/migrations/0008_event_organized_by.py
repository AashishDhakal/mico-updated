# Generated by Django 3.1 on 2020-09-18 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_resource_access_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organized_by',
            field=models.CharField(default='Mico Foundation', max_length=200),
        ),
    ]