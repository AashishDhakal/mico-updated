# Generated by Django 3.1 on 2020-10-20 02:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cms', '0035_auto_20201020_0212'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='category',
        ),
    ]
