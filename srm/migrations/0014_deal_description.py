# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-22 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0013_auto_20170923_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='description',
            field=models.TextField(blank=True, verbose_name='Примечания'),
        ),
    ]
