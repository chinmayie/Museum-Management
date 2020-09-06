# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-21 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180521_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divisions',
            name='type',
            field=models.CharField(blank=True, choices=[('art', 'art'), ('Archealogy', 'Archealogy'), ('Anthropology', 'Anthropology'), ('zoology', 'zoology')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='etype',
            field=models.CharField(blank=True, choices=[('art', 'art'), ('Archealogy', 'Archealogy'), ('Anthropology', 'Anthropology'), ('zoology', 'zoology')], max_length=20, null=True),
        ),
    ]
