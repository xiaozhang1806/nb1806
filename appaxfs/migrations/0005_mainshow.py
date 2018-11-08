# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-05 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appaxfs', '0004_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=251)),
                ('name', models.CharField(max_length=40)),
                ('trackid', models.CharField(max_length=30)),
                ('categoryid', models.CharField(max_length=10)),
                ('brandname', models.CharField(max_length=10)),
                ('img1', models.CharField(max_length=10)),
                ('childcid1', models.CharField(max_length=10)),
                ('productid1', models.CharField(max_length=10)),
                ('longname1', models.CharField(max_length=10)),
                ('price1', models.CharField(max_length=10)),
                ('marketprice1', models.CharField(max_length=10)),
                ('categoryid1', models.CharField(max_length=10)),
                ('brandname1', models.CharField(max_length=10)),
                ('img2', models.CharField(max_length=10)),
                ('childcid2', models.CharField(max_length=10)),
                ('productid2', models.CharField(max_length=10)),
                ('longname2', models.CharField(max_length=10)),
                ('price2', models.CharField(max_length=10)),
                ('marketprice2', models.CharField(max_length=10)),
                ('categoryid3', models.CharField(max_length=10)),
                ('brandname3', models.CharField(max_length=10)),
                ('img3', models.CharField(max_length=10)),
                ('childcid3', models.CharField(max_length=10)),
                ('productid3', models.CharField(max_length=10)),
                ('longname3', models.CharField(max_length=10)),
                ('price3', models.CharField(max_length=10)),
                ('marketprice3', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
