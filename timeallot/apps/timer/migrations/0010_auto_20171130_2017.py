# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 20:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0009_auto_20171115_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttag',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='timer.Category'),
        ),
    ]
