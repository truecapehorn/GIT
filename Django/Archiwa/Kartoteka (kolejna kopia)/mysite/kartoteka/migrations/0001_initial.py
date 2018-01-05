# Generated by Django 2.0 on 2017-12-21 07:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('dodany', 'Dodany'), ('realizowany', 'Realizowany'), ('zakończony', 'Zakończony')], default='Dodany', max_length=20)),
                ('entry_date', models.DateTimeField(default=datetime.datetime(2017, 12, 21, 7, 9, 36, 5436, tzinfo=utc))),
                ('num', models.IntegerField(blank=True)),
                ('enter_code', models.CharField(blank=True, max_length=30)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('investor', models.CharField(blank=True, max_length=30)),
                ('contract_number', models.CharField(blank=True, max_length=30)),
                ('zip_code', models.CharField(blank=True, max_length=30)),
                ('manager', models.CharField(blank=True, max_length=30)),
                ('invoice', models.CharField(blank=True, max_length=200)),
                ('design', models.CharField(blank=True, max_length=200)),
                ('rcd_date', models.DateField(blank=True, null=True)),
                ('implementation_date', models.DateField(blank=True, null=True)),
                ('doer', models.CharField(blank=True, max_length=30)),
                ('comments', models.TextField(blank=True)),
                ('coutry', models.CharField(blank=True, max_length=30)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='entry_modifiers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-implementation_date',),
            },
        ),
    ]