# Generated by Django 3.1 on 2020-10-08 04:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('donations', '0009_auto_20201008_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='causesdonation',
            name='method',
            field=models.CharField(
                choices=[('paypal', 'paypal'), ('card', 'card'),
                         ('check', 'check')], max_length=50),
        ),
    ]
