# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-05 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appaxfs', '0005_mainshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='FootTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=20)),
                ('typename', models.CharField(max_length=30)),
                ('childtypenames', models.CharField(max_length=255)),
                ('typesort', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
        migrations.RemoveField(
            model_name='mainshow',
            name='brandname1',
        ),
        migrations.RemoveField(
            model_name='mainshow',
            name='brandname3',
        ),
        migrations.RemoveField(
            model_name='mainshow',
            name='categoryid1',
        ),
        migrations.RemoveField(
            model_name='mainshow',
            name='categoryid3',
        ),
        migrations.AlterField(
            model_name='mainshow',
            name='brandname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='mainshow',
            name='img1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mainshow',
            name='img2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mainshow',
            name='img3',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mainshow',
            name='longname1',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='mainshow',
            name='longname2',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='mainshow',
            name='longname3',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterModelTable(
            name='mainshow',
            table='axf_mainshow',
        ),
    ]