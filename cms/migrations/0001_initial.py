# Generated by Django 3.1 on 2020-08-29 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BOD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='teams')),
                ('designation', models.CharField(max_length=200)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('micomodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.micomodel')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address_line_1', models.TextField()),
                ('address_line_2', models.TextField(blank=True, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state_province', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('message', models.TextField(blank=True, null=True)),
            ],
            bases=('common.micomodel',),
        ),
        migrations.CreateModel(
            name='Endowment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='events')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='history')),
                ('year', models.CharField(max_length=50)),
                ('short_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_by', models.CharField(max_length=300)),
                ('designation', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='messages')),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('micomodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.micomodel')),
                ('title', models.CharField(max_length=300)),
                ('thumbnail', models.ImageField(upload_to='newsposts')),
                ('category', models.CharField(choices=[('Medical', 'Medical'), ('Food', 'Food')], max_length=50)),
                ('time', models.CharField(max_length=200)),
                ('speaker', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('keywords', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
            bases=('common.micomodel',),
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('micomodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.micomodel')),
                ('title', models.CharField(max_length=300)),
                ('published_by', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Annual Reports', 'Annual Reports')], max_length=50)),
                ('resource_file', models.FileField(upload_to='resources')),
                ('description', models.TextField()),
            ],
            bases=('common.micomodel',),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sliders')),
                ('title_1', models.CharField(max_length=200)),
                ('title_2', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='teams')),
                ('designation', models.CharField(max_length=200)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Trustee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='teams')),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='works')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=300)),
                ('detail', models.TextField()),
            ],
        ),
    ]