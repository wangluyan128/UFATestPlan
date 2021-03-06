# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-15 01:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180511_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcase',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='yi_case',
        ),
        migrations.AddField(
            model_name='testcase',
            name='is_yilai',
            field=models.BooleanField(default=False, verbose_name='是否作为项目登录的依赖'),
        ),
        migrations.AlterField(
            model_name='functionallofic',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 15, 9, 8, 18, 226833), verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='yilai',
            field=models.BooleanField(default=False, verbose_name='是否依赖登录'),
        ),
    ]
