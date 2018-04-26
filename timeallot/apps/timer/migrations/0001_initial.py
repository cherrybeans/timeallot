# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 21:46
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=10)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='timer.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveSmallIntegerField()),
                ('starttime', models.DateTimeField()),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timer.ProjectTag')),
            ],
        ),
        migrations.CreateModel(
            name='SubTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=10)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtags', to='timer.ProjectTag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='session',
            name='subtags',
            field=models.ManyToManyField(null=True, to='timer.SubTag'),
        ),
    ]
