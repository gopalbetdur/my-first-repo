# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-05 15:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20161104_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskobjects',
            name='predefinedObjID',
        ),
        migrations.RemoveField(
            model_name='taskobjects',
            name='predefinedTaskName',
        ),
        migrations.DeleteModel(
            name='RegisteredObjects',
        ),
        migrations.DeleteModel(
            name='TaskObjects',
        ),
    ]