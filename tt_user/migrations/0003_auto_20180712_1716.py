# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-12 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0002_auto_20180711_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uaddname',
            field=models.CharField(default='\u672a\u586b\u5199', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='uaddressee',
            field=models.CharField(max_length=11),
        ),
    ]
