# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0033_auto_20170612_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='link',
            field=models.CharField(blank=True, max_length=200, verbose_name='Ссылка на страницу'),
        ),
    ]
