# Generated by Django 3.1 on 2020-09-24 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_activitylog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='data',
            field=models.JSONField(help_text='Query parameters and request body data'),
        ),
    ]
