# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-06 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appaxfs', '0011_auto_20181106_0955'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FootTypes',
            new_name='FoodTypes',
        ),
        migrations.RenameField(
            model_name='myuser',
            old_name='addresss',
            new_name='address',
        ),
        migrations.AddField(
            model_name='myuser',
            name='icon',
            field=models.ImageField(null=True, upload_to='icons'),
        ),
    ]
