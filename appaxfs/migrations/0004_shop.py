# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-05 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appaxfs', '0003_mustbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=251)),
                ('name', models.CharField(max_length=40)),
                ('trackid', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'axf_shop',
            },
        ),
    ]
