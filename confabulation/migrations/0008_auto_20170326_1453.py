# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('confabulation', '0007_auto_20170326_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recording',
            name='transscription',
        ),
        migrations.RemoveField(
            model_name='story',
            name='transscription',
        ),
        migrations.AddField(
            model_name='transscription',
            name='recording',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='confabulation.Recording'),
        ),
        migrations.AlterField(
            model_name='story',
            name='photos',
            field=models.ManyToManyField(to='confabulation.Photo'),
        ),
    ]