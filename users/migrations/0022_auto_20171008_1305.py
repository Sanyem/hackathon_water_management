# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-08 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_users_currentreservoir'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='currentreservoir',
            field=models.IntegerField(default=0),
        ),
    ]
