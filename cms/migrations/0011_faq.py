# Generated by Django 3.1 on 2020-09-21 08:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cms', '0010_auto_20200921_0650'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
        ),
    ]
