# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-10 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyse', '0002_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='region_id',
            field=models.IntegerField(unique=True, verbose_name='\u533a\u57dfID'),
        ),
    ]
