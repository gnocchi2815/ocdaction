# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-26 16:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_anxiety-score-card-model-add-time-periods'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 3, 26, 16, 4, 44, 39503, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2017, 3, 26, 16, 4, 58, 789791, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
