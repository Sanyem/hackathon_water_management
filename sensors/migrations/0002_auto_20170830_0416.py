# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='temp',
            field=models.FloatField(),
        ),
    ]
