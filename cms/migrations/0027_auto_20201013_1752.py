# Generated by Django 3.1 on 2020-10-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0026_contentmanagement_featured_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentmanagement',
            name='facebook_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contentmanagement',
            name='instagram_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contentmanagement',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contentmanagement',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
