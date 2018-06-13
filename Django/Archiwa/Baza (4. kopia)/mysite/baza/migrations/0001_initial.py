# Generated by Django 2.0 on 2017-12-18 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_dodania', models.DateTimeField(auto_now_add=True)),
                ('uaktualniony', models.DateTimeField(auto_now=True)),
                ('data_realizacji', models.DateField(blank=True, null=True)),
                ('inwestor', models.CharField(blank=True, max_length=31)),
                ('nr_umowy', models.DecimalField(blank=True, decimal_places=0, max_digits=30)),
                ('kod', models.CharField(blank=True, max_length=30)),
                ('kierownik', models.CharField(blank=True, max_length=30)),
                ('fv', models.CharField(blank=True, max_length=200)),
                ('montaz', models.CharField(blank=True, max_length=200)),
                ('uwagi', models.TextField(blank=True)),
                ('kraj', models.CharField(blank=True, max_length=30)),
                ('status', models.CharField(choices=[('dodany', 'Dodany'), ('realizowany', 'Realizowany'), ('zakończony', 'Zakończony')], default='Dodany', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='baza_rekord', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-data_dodania',),
            },
        ),
    ]
