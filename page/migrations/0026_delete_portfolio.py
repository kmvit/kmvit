# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-12 11:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0025_auto_20170612_1443'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Portfolio',
        ),
    ]