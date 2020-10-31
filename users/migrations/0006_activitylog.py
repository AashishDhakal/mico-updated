# Generated by Django 3.1 on 2020-09-24 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_delete_activitylog'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(help_text='Request method get post put or patch', max_length=20)),
                ('data', models.JSONField(help_text='Query parameters and request body data')),
                ('url_path', models.TextField(help_text='Url requested')),
                ('status_code', models.CharField(default='0', help_text='Status code returned from server', max_length=10)),
                ('device_used', models.TextField(default='', help_text='Deviced used by user to request')),
                ('ip_address', models.CharField(default='', help_text='IP address of user', max_length=255)),
                ('browser_used', models.TextField(default='', help_text='Browser used by user')),
                ('accessed_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, help_text='User to whom activity belongs to.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='activity', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
