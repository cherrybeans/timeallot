# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20171130_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeruser',
            name='email',
            field=models.EmailField(
                max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
