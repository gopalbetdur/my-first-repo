# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-03 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20161102_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activeobjects',
            name='id',
        ),
        migrations.RemoveField(
            model_name='taskobjects',
            name='id',
        ),
        migrations.AlterField(
            model_name='activeobjects',
            name='activeObjID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.RegisteredObjects'),
        ),
        migrations.AlterField(
            model_name='taskobjects',
            name='predefinedObjID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.RegisteredObjects'),
        ),
    ]
