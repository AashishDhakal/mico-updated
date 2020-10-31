# Generated by Django 3.1 on 2020-10-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0015_gallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Galleries'},
        ),
        migrations.AddField(
            model_name='project',
            name='goal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='is_full',
            field=models.BooleanField(default=True),
        ),
    ]
