# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-11 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uname',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]