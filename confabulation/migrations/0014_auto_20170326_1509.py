# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('confabulation', '0013_auto_20170326_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='story',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='confabulation.Story'),
        ),
    ]