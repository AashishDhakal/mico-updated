# Generated by Django 3.1 on 2020-10-07 06:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cms', '0022_contentmanagement_sponsorship_workwithus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentmanagement',
            name='endowment_text',
            field=models.TextField(default=''),
        ),
    ]
