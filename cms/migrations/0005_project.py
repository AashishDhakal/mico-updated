# Generated by Django 3.1 on 2020-09-17 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='projects')),
                ('project_name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('detail', models.TextField()),
            ],
        ),
    ]
