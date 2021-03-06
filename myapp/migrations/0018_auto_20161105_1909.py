# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-05 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20161105_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskObjects1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='RegisteredObjects',
            new_name='RegisteredObjects1',
        ),
        migrations.RenameModel(
            old_name='TaskList',
            new_name='TaskList1',
        ),
        migrations.AddField(
            model_name='taskobjects1',
            name='predefinedObjID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.RegisteredObjects1'),
        ),
        migrations.AddField(
            model_name='taskobjects1',
            name='predefinedTaskName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.TaskList1'),
        ),
    ]
