# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-11 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=50)),
                ('uemail', models.CharField(max_length=30)),
                ('uphone', models.CharField(max_length=11)),
                ('uaddress', models.CharField(max_length=50)),
                ('upostcode', models.CharField(max_length=6)),
                ('uaddressee', models.CharField(max_length=15)),
            ],
        ),
    ]