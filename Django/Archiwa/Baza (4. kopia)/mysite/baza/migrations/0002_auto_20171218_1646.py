# Generated by Django 2.0 on 2017-12-18 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='database',
            old_name='montaz',
            new_name='projekt',
        ),
    ]
