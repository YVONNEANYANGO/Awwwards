# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-29 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prizes', '0003_auto_20181230_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(upload_to='profiles/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='landing_page',
            field=models.ImageField(upload_to='projects/'),
        ),
    ]