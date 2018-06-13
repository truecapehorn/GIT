# Generated by Django 2.0 on 2017-12-12 18:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descriprion', models.TextField(max_length=500)),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('video_id', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=200)),
            ],
        ),
    ]
