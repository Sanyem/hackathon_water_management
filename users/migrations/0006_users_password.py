# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-15 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
    ]