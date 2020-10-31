# Generated by Django 3.1 on 2020-10-07 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_auto_20201007_0250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endowment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('endowment_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cms.faq')),
            ],
        ),
    ]
