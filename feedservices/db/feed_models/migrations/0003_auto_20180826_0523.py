# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-26 05:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed_models', '0002_auto_20180819_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='downvote',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='upvote',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 26, 5, 23, 42, 271137)),
        ),
        migrations.AlterField(
            model_name='downvote',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 26, 5, 23, 42, 279093)),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 26, 5, 23, 42, 273142)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 26, 5, 23, 42, 269219)),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 26, 5, 23, 42, 277268)),
        ),
    ]
