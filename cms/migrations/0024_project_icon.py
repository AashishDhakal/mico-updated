# Generated by Django 3.1 on 2020-10-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cms', '0023_contentmanagement_endowment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='icon',
            field=models.ImageField(default='/static/donateclassroom.png',
                                    upload_to='icon'),
        ),
    ]
