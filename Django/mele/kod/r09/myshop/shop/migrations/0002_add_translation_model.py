# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
            options={
                'managed': True,
                'db_tablespace': '',
                'db_table': 'shop_category_translation',
                'default_permissions': (),
                'verbose_name': 'category Translation',
            },
        ),
        migrations.CreateModel(
            name='ProductTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'managed': True,
                'db_tablespace': '',
                'db_table': 'shop_product_translation',
                'default_permissions': (),
                'verbose_name': 'product Translation',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories', 'verbose_name': 'category'},
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([]),
        ),
        migrations.AddField(
            model_name='producttranslation',
            name='master',
            field=models.ForeignKey(to='shop.Product', related_name='translations', editable=False, null=True),
        ),
        migrations.AddField(
            model_name='categorytranslation',
            name='master',
            field=models.ForeignKey(to='shop.Category', related_name='translations', editable=False, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='producttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
