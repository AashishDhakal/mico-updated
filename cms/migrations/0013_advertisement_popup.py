# Generated by Django 3.1 on 2020-09-24 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20200924_0414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ads')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Popup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='popup')),
                ('title_1', models.CharField(max_length=100)),
                ('title_2', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('button_link', models.URLField(blank=True, null=True)),
                ('button_text', models.CharField(max_length=100)),
            ],
        ),
    ]