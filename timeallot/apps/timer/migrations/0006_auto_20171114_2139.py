# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 21:39
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0005_auto_20171114_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttag',
            name='category',
            field=models.ForeignKey(
                default=None, on_delete=django.db.models.deletion.CASCADE, related_name='projects',
                to='timer.Category'
            ),
        ),
    ]
