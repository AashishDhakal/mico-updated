# Generated by Django 3.1 on 2020-10-21 14:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('donations', '0014_auto_20201021_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdonation',
            name='method',
            field=models.CharField(
                choices=[('paypal', 'paypal'), ('card', 'card'),
                         ('offline', 'offline')], max_length=50),
        ),
    ]
