# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-17 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_order', '0002_auto_20180717_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='oIsPay',
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='payType',
            field=models.CharField(default='1', max_length=2),
        ),
    ]
