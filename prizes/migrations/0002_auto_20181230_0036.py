# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-29 21:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prizes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile',
            new_name='profile_pic',
        ),
    ]
