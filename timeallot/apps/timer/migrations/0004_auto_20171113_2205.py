# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0003_auto_20171113_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='subtags',
            field=models.ManyToManyField(to='timer.SubTag'),
        ),
    ]
