# Generated by Django 3.1 on 2020-10-08 04:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('donations', '0008_auto_20201007_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='causesdonation',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='projectdonation',
            name='duration',
        ),
        migrations.AddField(
            model_name='causesdonation',
            name='donation_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='projectdonation',
            name='donation_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
