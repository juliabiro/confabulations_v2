# Generated by Django 2.0.1 on 2018-01-21 20:51

import colorful.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confabulation', '0010_remove_era_connection_range'),
    ]

    operations = [
        migrations.CreateModel(
            name='EraPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('color_code', colorful.fields.RGBColorField()),
            ],
        ),
        migrations.RemoveField(
            model_name='era',
            name='stories',
        ),
        migrations.RemoveField(
            model_name='storyinera',
            name='story',
        ),
        migrations.RemoveField(
            model_name='storyinera',
            name='theme',
        ),
        migrations.DeleteModel(
            name='Era',
        ),
        migrations.DeleteModel(
            name='StoryInEra',
        ),
    ]
