# Generated by Django 3.1 on 2020-09-29 06:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('donations', '0004_auto_20200929_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdonation',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
