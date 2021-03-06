# Generated by Django 3.1 on 2020-09-20 02:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cms', '0008_event_organized_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='contact',
            name='address_line_1',
            field=models.CharField(default='address line 1', max_length=500),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address_line_2',
            field=models.CharField(default='address line 2', max_length=500),
        ),
    ]
